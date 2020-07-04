import argparse
import configparser
import datetime
import json
import os
from io import BytesIO
from typing import Dict

import requests
from PIL import Image

API_MAX_COUNT = 150

parser = argparse.ArgumentParser(description="A script for the Bing Image Search")
keyword_default = "soccer game"
parser.add_argument(
    "-k", "--keyword", default=keyword_default, help=f"A search keyword. default: {keyword_default}"
)
parser.add_argument(
    "-s", "--skip-downloading-images", action="store_true", help="Skip downloading images"
)
args = parser.parse_args()


class BingImageSearchAPI:
    save_dir = ""
    json_results = []
    image_urls = []

    def __init__(self, options: Dict) -> None:
        self.subscription_key = options["subscription_key"]
        self.endpoint = options["endpoint"]
        self.keyword = options["keyword"]
        self.is_skip_downloading_images = options["is_skip_downloading_images"]

    def send_request(self, offset: int, count: int):
        headers = {"Ocp-Apim-Subscription-Key": self.subscription_key}
        params = {
            "q": self.keyword,
            "license": "public",
            "imageType": "photo",
            "offset": offset,
            "count": count,
        }
        response = requests.get(self.endpoint, headers=headers, params=params)
        response.raise_for_status()
        json = response.json()
        self.json_results.append(json)
        total_num_images = json["totalEstimatedMatches"]
        next_offset = json["nextOffset"]
        return total_num_images, next_offset

    def get_json(self) -> None:
        total_num_images, next_offset = self.send_request(offset=0, count=API_MAX_COUNT)
        print(f"{total_num_images=}, {next_offset=}")
        while next_offset < total_num_images:
            _, next_offset = self.send_request(offset=next_offset, count=API_MAX_COUNT)
            print(f"{total_num_images=}, {next_offset=}")

    def get_image_urls(self) -> None:
        for json_result in self.json_results:
            for img in json_result["value"]:
                self.image_urls.append(img["thumbnailUrl"])

    def generate_save_dir_name(self) -> None:
        dt_now = datetime.datetime.now()
        self.save_dir = "downloads/images_" + dt_now.strftime("%Y%m%d_%H%M%S")

    def create_save_dir(self) -> None:
        self.generate_save_dir_name()
        os.makedirs(self.save_dir)

    def save_json(self) -> None:
        for num, result in enumerate(self.json_results):
            with open(f"{self.save_dir}_{num}.json", "w") as f:
                json.dump(result, f)

    def download_images(self) -> None:
        for num, url in enumerate(self.image_urls):
            image_data = requests.get(url)
            # image_data.raise_for_status()
            if image_data.status_code == requests.codes.ok:
                print(f"{num}: Downloaded {url}")
            else:
                print(f"{num}: Failed to download {url}")
            image = Image.open(BytesIO(image_data.content))
            image.save(f"{self.save_dir}/image_{num}.jpg")

    def save_images(self) -> None:
        self.generate_save_dir_name()
        self.create_save_dir()
        self.get_json()
        self.save_json()
        if self.is_skip_downloading_images:
            return
        else:
            self.get_image_urls()
            self.download_images()


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("settings.ini")
    subscription_key = config["azure"]["subscription_key"]
    endpoint = config["azure"]["endpoint"]

    options: Dict = {
        "subscription_key": subscription_key,
        "endpoint": endpoint,
        "keyword": args.keyword,
        "is_skip_downloading_images": args.skip_downloading_images,
    }
    api = BingImageSearchAPI(options)
    api.save_images()
