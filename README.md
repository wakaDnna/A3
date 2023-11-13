# A3
<p align="center">
    <img src="https://github.com/wakaDnna/A3/assets/147518230/f2d04341-0199-4be1-80c0-d690543a84d0"/>
</p>

# 開発環境
Python 3.11.5  
alembic 1.12.1  
pydantic 2.4.2  

# デバッグ実行
```
uvicorn main:app --reload
```
http://127.0.0.1:8000
にて起動する

## swagger
http://127.0.01:8000/docs

## alembic

1. はじめに
alembic.iniのscript_locationのパスを変更  
実行ディレクトリからenv.pyのあるディレクトリを指定する

```
script_location = ./db/
```

2. マイグレーションファイルを作成

```
alembic --config ./db/alembic.ini revision --autogenerate
```

3. マイグレーションの実施
```
alembic upgrade head
```


# ER Diagram

```mermaid

erDiagram
    users{
        string id PK
        string(50) name
        string(50) display_id 
        int followers_count
        int following_count
        date birthday
        text bio
        mediumblob image
        timestamp created_at
        timestamp updated_at
    }

```

## 各種ルータについて
usersやpostsルータに関して

```
db.query(ここ！)
```
queryに渡すのは**SQLAlchemyのモデル**を渡すようにすること！
schemaはresponse_modelとして指定するもので、あくまでレスポンスの型を指定してあげるもの

コードファーストでいく
fastapi crud generate　自動で
swaggerはfastapi
swagger から typescript client 自動生成ライブラリがある