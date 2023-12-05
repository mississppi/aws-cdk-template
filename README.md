# 概要
vpc
 - az: 2つ
 - subnet: publicとprivate


```
$ source .venv/bin/activate
$ pip install -r requirements.txt
```

```
差分チェック
$ cdk diff

初回は必要
$ cdk bootstrap

シンタックスのチェック
$ cdk synth

デプロイ
$ cdk deploy

削除
$ cdk destroy
```
