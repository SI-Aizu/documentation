# Tutorial Bing Image Search

- [Bing Image Search API | Microsoft Azure](https://azure.microsoft.com/en-us/services/cognitive-services/bing-image-search-api/)



## Start with docker-compose

```sh
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

### Donload Size

```sh
python main.py -n 4
```

### Search Keyword

```sh
python main.py -k 'cat'
```
