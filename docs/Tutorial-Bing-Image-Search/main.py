import configparser
import os
import datetime
import math

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.ini')
    subscription_key = config['azure']['subscription_key']
    endpoint = config['azure']['endpoint']

    num_downloads = 25

    headers = {'Ocp-Apim-Subscription-Key' : subscription_key}
    search_term = 'soccer game'
    params  = {'q': search_term, 'license': 'public', 'imageType': 'photo'}
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    thumbnail_urls = [img['thumbnailUrl'] for img in search_results['value'][:num_downloads]]

    dt_now = datetime.datetime.now()
    save_dir = 'downloads_' + dt_now.strftime('%Y%m%d_%H%M%S')
    os.makedirs(save_dir, exist_ok=True)
    num_downloads_sqrt = int(math.sqrt(num_downloads))
    f, axes = plt.subplots(num_downloads_sqrt, num_downloads_sqrt)
    for i in range(num_downloads_sqrt):
        for j in range(num_downloads_sqrt):
            image_data = requests.get(thumbnail_urls[i+num_downloads_sqrt*j])
            image_data.raise_for_status()
            image = Image.open(BytesIO(image_data.content))
            axes[i][j].imshow(image)
            axes[i][j].axis('off')
            image.save(f'{save_dir}/thumbnail_{i}_{j}.jpg')
