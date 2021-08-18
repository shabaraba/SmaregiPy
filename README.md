# smaregi py
# CAUTION
個人が開発しているパッケージで非公式です。  
株式会社スマレジとは全く関係ありません。

また、開発中のため、APIとして足りていないものも多く、また破壊的変更もあり得ます。

# OverView
スマレジのプラットフォームAPIを実施するためのpython3用パッケージです。  
pydanticを用いた型定義と、asyncメソッドを用いています。

# Install
pipコマンドを用いてインストールできます。

```sh
pip install git+https://github.com/shabaraba/SmaregiPy
```

# Usage
## init
初めに使用するアプリの情報をセットします。  
```python3
from smaregipy import SmaregiPy
SmaregiPy.init_by_dict(
    {
        'env_division': "DEV or PROD",
        'contract_id':contract_id,
        'smaregi_client_id':smaregi_client_id,
        'smaregi_client_secret':smaregi_client_secret
    }
)
```

## authorize
contract_idとscopeのリストを引数にauthorizeメソッドを呼び出します。
```python3
account = Account.authorize(
    contract_id,
    [
        'pos.stores:read',
        'pos.stores:write',
        'pos.products:read',
        'pos.transactions:read',
    ]
)
```
成功すればaccountデータを取得できます。
```python3
from smaregipy.account import Account
if account is not None:
    print(account.access_token.access_token)
```
accountのメンバは下記を参照のこと。
https://github.com/shabaraba/SmaregiPy/blob/main/smaregipy/entities/account.py

## models
**Record**と**Collection**の2種類のモデルを用意しており、それぞれ下記の通りです。

- **Record**: 単体のモデル。単体を取得したり更新する際に使用。
- **Collection**: Recordモデルをリストとしてまとめたモデル。一覧取得や一括更新系はこちらを使用。

## methods
| method | sync / async | description |
| ---- | ---- | ---- |
| id | sync | Record専用。どのデータを取得/更新するかを指定するためのメソッド。商品ならproduct_id、店舗ならstore_idを指定します。 |
| find | sync | Collection専用。取得済みのCollectionの中から、指定したidを持つRecordを取得します。 |
| fetch | async | Record専用。id()で指定したidを持つモデルをAPIを通じて取得します。`where`をdict型で引数にとれます。 |
| fetch_list | async | Collection専用。指定した`limit`、`page`、`where`に則ったデータをリストとして取得します。 |
| fetch_all | async | Collection専用。fetch_listを全ページにわたって実行し、全データを取得します。 |
| save | async | Record専用。現在自身が持っているフィールドの値でAPIを通じて作成/更新します。作成の場合はidが付与されます。 |

fetch系に関して、with_*系はすべてallとして扱っています。

### examples
```python3
from smaregipy import pos


all_stores = await pos.StoreCollection().get_all()
store = all_stores.find(1)
store.store_name = 'updated'
updated_store = await store.save()

transaction = await pos.Transaction().id(165).get()

transaction_list = await pos.TransactionCollection().get_list(limit=5, page=2)

response = await pos.TransactionDetailCollection().create_csv(
    transactionDateTimeFrom='2021-02-01T00:00:00+0900',
    transactionDateTimeTo='2021-02-20T00:00:00+0900',
    callbackUrl='https://path/your/uri'
)
```

## NoData type
スマレジプラットフォームAPIではデータ更新時、

- NULL(None)をフィールドに入れる
- フィールド自体を指定しない

の2者で意味が異なる仕様のため、データ自体が存在しない（ != None ）の状態を保持する必要があります。  
この、データ自体が存在しない状態を**NoData**型として定義し、各フィールドが初期化されています。
