# VS CodeでPython

## Step1:VS Codeをインストール

1. [Webページ](https://azure.microsoft.com/products/visual-studio-code/)からVS Codeをインストールする。

## Step2:VSCodeを日本語化

1. VS Codeの左側の**Extensions**を選択
2. **Japanese Language Pack for VS Code**を検索
3. インストールを実行
4. Viewタブの**Command Palette**を選択
5. **Configure Display Package**を選択
6. **ja**を選択

## Step3.Githubの利用

1. Gitをインストール
   1. [サイト](https://git-scm.com/download/win)からGitをインストール
   2. VSCodeでターミナルを選択し、次を実行

   ```PowerShell
   git config --global user.email [githubで登録したメールアドレス]
   ```

2. Githubにリポジトリを作成する。
   1. ブラウザで[Github](https://github.com/login)にサインイン
   2. 左上のボタンから自分のIDのページを開き、Repositoriesを選択
   3. Newを選択
   4. Privateを選択
   5. Initialize this repository with a READMEにチェックを入れ、readmeを自動生成
   6. Create repositoryをクリック
3. リポジトリをVS Codeに関連付ける
   1. 適当なローカルフォルダを作成
   2. 左側のソース管理を選択
   3. リポジトリのクローンを選択
   4. 作成したリポジトリのurlを入力
   5. リポジトリの内容がコピーされる
   6. 編集した後は、ソース管理からコミット（保存）→プッシュ（アップロード）でweb上に保存される

## Step4.Pythonのインストール

1. VS Codeの左側の**拡張機能**を選択
2. **Python**を検索し、「Python」アドインをインストール
3. (linterの設定)ファイル-ユーザー設定-設定 から、次の設定を追加する
   * python.linting.enabled Lint機能を有効にするかどうか true
   * python.linting.pylintEnabled Linterにpylintを使用するかどうか false
   * python.linting.flake8Enabled Linterにflake8を使用するかどうか true
   * python.linting.lintOnSave ファイル保存時にLintを実行するか true
   * python.formatting.provider Pythonコードの整形に何を使用するか autopep8
   * editor.formatOnSave ファイル保存時に自動整形するかどうか false(好みに応じてtrueでもよい)
4. ターミナル-新しいターミナル を選択て開いたターミナルに、次を入力
   * python -m pip install --user numpy
   * python -m pip install --user pandas
   * python -m pip install --user scipy
   * python -m pip install --user matplotlib
   * python -m pip install --user opencv-python
   * その他、必要になったライブラリ

5. ワークスペース内(Step3で作成したフォルダ)にある.vscode\setings.jsonを開き、次を記載

```foo
{
    "python.analysis.extraPaths": [
        "./source"
    ]
}
```

## STEP5その他拡張機能

* 拡張機能**Code Spell Checker**をインストールする(スペルチェッカー)
* 拡張機能**Tabnine**をインストールする（AIによる自動補完）
* 拡張機能**Python Docstring Generator**をインストールする（Docstring自動生成）
* 拡張機能**Python Indent**をインストールする
* 拡張機能**Trailing Spaces**をインストールする(無駄な空白表示)

## STEP6その他

* [Python Windows] Pythonバージョンを指定してpip install
  * https://qiita.com/Qiitaman/items/f874fb87273d1fa459c8
