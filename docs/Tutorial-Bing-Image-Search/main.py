import configparser
import os
import datetime
import argparse
import json
from typing import Dict

import requests
from PIL import Image
from io import BytesIO


parser = argparse.ArgumentParser(
    description="A script for the Bing Image Search"
)
num_downloads_default = 35
parser.add_argument(
    "-n", "--num-downloads", default=num_downloads_default,
    help=f"The number of fetching images. The actual number delivered may be less than requested. The default is {num_downloads_default}. The maximum value is 150. Set 0 to download all estimated images"
)
keyword_default = 'soccer game'
parser.add_argument(
    "-k", "--keyword", default=keyword_default,
    help=f"A search keyword. default: {keyword_default}"
)
parser.add_argument(
    "-s", "--skip-downloading-images", action="store_true", help="Skip downloading images"
)
args = parser.parse_args()


class BingImageSearchAPI:
    save_dir = ''
    json_result = {}
    image_urls = []

    def __init__(self, options: Dict) -> None:
        self.subscription_key = options['subscription_key']
        self.endpoint = options['endpoint']
        self.keyword = options['keyword']
        self.num_downloads = options['num_downloads']
        self.is_skip_downloading_images = options['is_skip_downloading_images']

    def get_json(self) -> None:
        headers = {'Ocp-Apim-Subscription-Key' : self.subscription_key}
        params  = {'q': self.keyword, 'license': 'public', 'imageType': 'photo', 'count': self.num_downloads}
        response = requests.get(self.endpoint, headers=headers, params=params)
        response.raise_for_status()
        self.json_result = response.json()

    def get_image_urls(self) -> None:
        self.image_urls = [img['thumbnailUrl'] for img in self.json_result['value'][:self.num_downloads]]

    def generate_save_dir_name(self) -> None:
        dt_now = datetime.datetime.now()
        self.save_dir = 'downloads/images_' + dt_now.strftime('%Y%m%d_%H%M%S')

    def create_save_dir(self) -> None:
        self.generate_save_dir_name()
        os.makedirs(self.save_dir)

    def save_json(self) -> None:
        with open(f'{self.save_dir}.json', 'w') as f:
            json.dump(self.json_result, f)

    def download_images(self) -> None:
        for image_count in range(num_downloads):
            image_data = requests.get(self.image_urls[image_count])
            image_data.raise_for_status()
            image = Image.open(BytesIO(image_data.content))
            image.save(f'{self.save_dir}/image_{image_count}.jpg')

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


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.ini')
    subscription_key = config['azure']['subscription_key']
    endpoint = config['azure']['endpoint']

    num_downloads = int(args.num_downloads)
    if num_downloads < 0:
        print(f'Invalid input number of fetching images: {num_downloads}')
        exit(1)

    options: Dict = {
        'subscription_key': subscription_key,
        'endpoint': endpoint,
        'keyword': args.keyword,
        'num_downloads': num_downloads,
        'is_skip_downloading_images': args.skip_downloading_images
    }
    api = BingImageSearchAPI(options)
    api.save_images()
