# Tutorial

- [Bing Image Search API | Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/bing-image-search-api/)
- [Quickstart: Search for images using the Bing Image Search REST API and Python - Azure Cognitive Services | Microsoft Docs](https://docs.microsoft.com/en-us/azure/cognitive-services/Bing-Image-Search/quickstarts/python)



## Start with docker-compose

```sh
cd docs/Tutorial-Bing-Image-Search
docker-compose build
docker-compose run --rm dev bash
```



## Create your Subscription Key

1. Go to Azure
1. Create a Resource group
1. Create a service of the Cognitive Services

!!! note "Check the latest information"
    ここらへんの手順は頻繁に変わるので公式ドキュメントを参照して最新の情報を確認すること。
    ここでは解説しない。
    Check the latest official Azure documentation.

- [Pricing - Bing Search API v7 | Microsoft Azure](https://azure.microsoft.com/en-us/pricing/details/cognitive-services/search-api/)

INSTANCE を Free で作成すれば 1000回/月 まで無料で利用できる。



## Set Your Subscription Key

Create your `settings.ini`.

```ini
[azure]
subscription_key = YOUR_KEY
endpoint = https://YOUR_ENDPOINT.cognitiveservices.azure.com/bing/v7.0/images/search
```

!!! warning "Make your subscription key private"
    subscription_key を間違って Git 管理下に含めて、全世界に大公開しないように気をつけること。
    誤って公開されているトークンはすぐに悪用されます。
    ちなみにこのディレクトリでは `settings.ini` は `.gitignore` に書かれています。



## Run the main.py

### Show Usage

```sh
python main.py --help
```

### Search Keyword

```sh
python main.py -k 'cat'
```

### Skip donwloading images

```sh
python main.py -k 'cat' --skip-downloading-images
```
