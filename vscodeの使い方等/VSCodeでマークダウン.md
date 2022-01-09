# VS Codeでmarkdownを共同編集

## Step1:VS Codeをインストール

1. [Webページ](https://azure.microsoft.com/products/visual-studio-code/)からVS Codeをインストールする。

## Step2:VSCodeを日本語化

1. VS Codeの左側の**Extensions**を選択
2. **Japanese Language Pack for VS Code**を検索
3. インストールを実行
4. Viewタブの**Command Palette**を選択
5. **Configure Display Package**を選択
6. **ja**を選択

## Step3:Markdown All in One/Code Spell Checker/docs-markdown/markdownlint/markdown pdfをインストール

1. VS Codeの左側の**Extensions**を選択
2. **Markdown All in One**を検索
3. インストールを実行
4. 以下同様にして、次の拡張機能をインストール
   * **Code Spell Checker**
   * **docs-markdown**
   * **markdownlint**
   * **markdown pdf**

## Step4:Live Share Extension Packをインストール

1. VS Codeの左側の**Extensions**を選択
2. **Live Share Extension Pack**を検索
3. インストールを実行

## Step5:Live Shareの開始

1. 左側の**Live Share**を選択
2. コラボレーション セッションの開始
3. **Share now**を選択
4. **Sign in to Github**を選択
5. **Authorize**を選択
6. **Participants**を選択
7. クリップボードの中身を送付
8. 受信側はurlを開くか、コラボレーション　セッションの参加を選択してurlを入力
9. ホスト側で開いているファイルが共有される
10. チャットや通話も可能

## Step6:Markdownの開始

1. ファイル->名前を付けて保存->拡張子を.mdにして保存すると、マークダウン編集用モードになる
2. [Ctrl]+[V] [K]でプレビュー表示
3. [Ctrl]+[Shift]+[V]でhtmlビュー
4. コマンドパレット[Ctrl]+[Shift]+[P]でMarkdownと入力すれば、コマンドが一覧で表示される

## Step7.Githubの利用

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

## Step