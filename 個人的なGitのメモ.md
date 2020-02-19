# 基本

## ローカルリポジトリの作成
`git init`

## GitHubなどからGitのクローンを取得
`git clone git@github.com:[ユーザーID]/[リポジトリ名].git`
<br>
<br>

### 【例１】基本的なcloneコマンド
`git clone git@github.com:nico82d4/study.git`
<br>
<br>

### 【例２】 ~/.ssh/config に GitHubの接続情報を記述している場合
GitHubへの接続に使用するSSH秘密鍵の名前が、デフォルトのid_rsaなどではない場合に、~/.ssh/configを利用する。

`git clone github:nico82d4/study.git`

※ 例１の、[ユーザー名]@[ホスト名] の部分を、~/.ssh/config 内に指定している Host の名称と置き換える。

> 【 参考：~/.ssh/config の例 】  
> Host github  
>    HostName github.com  
>    User git  
>    IdentityFile ~/.ssh/github_ed25519  
> 
> ※ SSH秘密鍵のファイル名については、自身が生成したファイル名に置き換えること。

