import configparser
import os

import requests
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO


if __name__ == '__main__':
    config = configparser.ConfigParser()
    config.read('settings.ini')
    subscription_key = config['azure']['subscription_key']
    endpoint = config['azure']['endpoint']
    # print(f'{subscription_key=}')
    # print(f'{endpoint=}')

    headers = {'Ocp-Apim-Subscription-Key' : subscription_key}
    search_term = 'soccer game'
    params  = {'q': search_term, 'license': 'public', 'imageType': 'photo'}
    response = requests.get(endpoint, headers=headers, params=params)
    response.raise_for_status()
    search_results = response.json()
    thumbnail_urls = [img['thumbnailUrl'] for img in search_results['value'][:16]]

    save_dir = 'downloads'
    os.makedirs(save_dir, exist_ok=True)
    f, axes = plt.subplots(4, 4)
    for i in range(4):
        for j in range(4):
            image_data = requests.get(thumbnail_urls[i+4*j])
            image_data.raise_for_status()
            image = Image.open(BytesIO(image_data.content))
            axes[i][j].imshow(image)
            axes[i][j].axis('off')
            image.save(f'{save_dir}/thumbnail_{i}_{j}.jpg')
