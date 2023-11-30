# DreamDirector

# フォルダに関する簡単な説明文
- config : settings.pyとかが入っているフォルダ
- account_app : アカウント管理機能
- diagnosis_app : まだ未定だけど、openaiをdjangoに組み込むときに使うフォルダ
- general_app : トップページとか、こまごました機能を入れる
- templates : htmlファイルの格納場所

# セットアップ
```bash


# 必要なpythonモジュールをインストール
pip install -r requirements.txt 

# SECRET_KEYを生成
# これを実行するとconfig/local.pyにSECRET_KEY変数が作成される
python regenerateSecretKey.py
```
