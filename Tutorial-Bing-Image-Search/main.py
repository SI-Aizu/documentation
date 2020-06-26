import configparser
import os
import datetime
import argparse

import requests
from PIL import Image
from io import BytesIO


parser = argparse.ArgumentParser(
    description="A script for the Bing Image Search"
)
num_downloads_default = 35
parser.add_argument(
    "-n", "--num-downloads", default=num_downloads_default,
    help=f"The number of images to return in the response. The actual number delivered may be less than requested. The default is {num_downloads_default}. The maximum value is 150."
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
    if 150 < num_downloads:
        print('The maximum value is 150.')
        exit(1)

    headers = {'Ocp-Apim-Subscription-Key' : subscription_key}
    search_term = args.keyword
    params  = {'q': search_term, 'license': 'public', 'imageType': 'photo', 'count': num_downloads}
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    image_urls = [img['thumbnailUrl'] for img in search_results['value'][:num_downloads]]

    dt_now = datetime.datetime.now()
    save_dir = 'downloads_' + dt_now.strftime('%Y%m%d_%H%M%S')
    os.makedirs(save_dir)
    image_count = 0
    for i in range(num_downloads):
        image_data = requests.get(image_urls[image_count])
        image_data.raise_for_status()
        image = Image.open(BytesIO(image_data.content))
        image.save(f'{save_dir}/image_{image_count}.jpg')
        image_count += 1
