# GitHub Packages



## Docker Login

### Create your personal token

[Personal Access Tokens] で `read:packages` を持つ token を作成する。

[Personal Access Tokens]: https://github.com/settings/tokens

### Docker login

```sh
docker login 'docker.pkg.github.com' -u 'YOUR_GITHUB_USERNAME' --password 'YOUR_TOKEN'
```

これで GitHub Packages から Docker image を Pull できるようになる。
