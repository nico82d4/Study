import sys
import pathlib
import hashlib
import datetime
import re


# 引数のパスからハッシュ値を生成して、先頭8文字だけを返す関数。
def create_hash(path):
    digestFirst = ''

    if path.is_file():
        # ハッシュ値の生成準備(md5)
        h = hashlib.new('md5')
            
        with open(path, 'rb') as f:
            while True:
                # 巨大なファイルに対応するように
                # 一定サイズに分割してハッシュ値を生成
                binaryData = f.read(2048 * h.block_size)
                if len(binaryData) == 0:
                    break
                h.update(binaryData)

        # 生成したハッシュ値を16進数に変換
        digest = h.hexdigest()

        # ハッシュ値の先頭から8文字を取得
        digestFirst = str(digest)[:8]

    return digestFirst



# リネーム用の関数
def file_rename(path):
    for tmpfile in path.iterdir():

        # ディレクトリの場合、関数を再帰的に呼び出す。
        if tmpfile.is_dir():
            file_rename(tmpfile)

        # ファイルの場合
        elif tmpfile.is_file():
            # ファイル名の取得
            name_old = tmpfile.name

            # 拡張子の取得
            suffix = tmpfile.suffix

            # 処理を行う拡張子を正規表現でチェック
            # （今回はマジックナンバーではなく、拡張子で。）
            result = re.match(r'\.(?:py|txt|md)$', suffix)

            # 対象の拡張子である場合
            if result is not None:

                # 最終更新日付の取得と表示形式の変更
                ts1 = tmpfile.stat().st_mtime
                ts2 = datetime.datetime.fromtimestamp(ts1)
                timestamp = ts2.strftime('%Y-%m-%d-%H%M%S')

                # ファイルのハッシュ値を取得
                digest = create_hash(tmpfile)

                # 新しいファイル名の生成
                # （joinメソッドの区切りなしで生成。）
                name_new = ''.join([timestamp, '_', digest, suffix])

                # デバッグ用に取得した情報を出力
                print(name_old, '=>', name_new)



# コマンドライン引数が1つだけの場合は、カレントパスを対象とする。
if len(sys.argv) == 1:
    path = pathlib.Path('.')
    file_rename(path)

# コマンドライン引数が2つの場合は、引数のパスを対象とする。
elif len(sys.argv) == 2:
    path = pathlib.Path(sys.argv[1])

    # 引数に指定されたパスが存在する場合は、処理を続行。
    if path.exists():
        file_rename(path)

    # 引数に指定されたパスが存在しない場合、メッセージを出力する。
    else:
        print('パスが存在しません。', sys.argv[1])

# コマンドライン引数が1と2以外の場合は、メッセージだけ出力する。
else:
    print(sys.argv[0], '[path]')

