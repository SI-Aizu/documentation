import configparser
import os
import datetime
import math
import argparse

import requests
from PIL import Image
from io import BytesIO


parser = argparse.ArgumentParser(
    description="A script for the Bing Image Search"
)
num_downloads_default = 4
parser.add_argument(
    "-n", "--num-downloads", default=num_downloads_default,
    help=f"A number of download images. default: {num_downloads_default}"
)
keyword_default = 'soccer game'
parser.add_argument(
    "-k", "--keyword", default=keyword_default,
    help=f"A search keyword. default: {keyword_default}"
)
args = parser.parse_args()


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.ini')
    subscription_key = config['azure']['subscription_key']
    endpoint = config['azure']['endpoint']

    num_downloads = int(args.num_downloads)

    headers = {'Ocp-Apim-Subscription-Key' : subscription_key}
    search_term = args.keyword
    params  = {'q': search_term, 'license': 'public', 'imageType': 'photo'}
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    thumbnail_urls = [img['thumbnailUrl'] for img in search_results['value'][:num_downloads]]

    dt_now = datetime.datetime.now()
    save_dir = 'downloads_' + dt_now.strftime('%Y%m%d_%H%M%S')
    os.makedirs(save_dir, exist_ok=True)
    num_downloads_sqrt = int(math.sqrt(num_downloads))
    for i in range(num_downloads_sqrt):
        for j in range(num_downloads_sqrt):
            image_data = requests.get(thumbnail_urls[i+num_downloads_sqrt*j])
            image_data.raise_for_status()
            image = Image.open(BytesIO(image_data.content))
            image.save(f'{save_dir}/thumbnail_{i}_{j}.jpg')
