# DreamDirector

# フォルダに関する簡単な説明文
- config : settings.pyとかが入っているフォルダ
- account : アカウント管理機能
- app_openai : まだ未定だけど、openaiをdjangoに組み込むときに使うフォルダ
- general : トップページとか、こまごました機能を入れる

# セットアップ
```bash


# 必要なpythonモジュールをインストール
pip install -r requirements.txt 

# SECRET_KEYを生成
# これを実行するとconfig/local.pyにSECRET_KEY変数が作成される
python regenerateSecretKey.py
```
