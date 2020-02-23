import pathlib
import datetime
import hashlib

# ハッシュ値生成の参考URL
# https://qiita.com/5zm/items/4592f1b0e036bd9505c8
# https://qiita.com/maboy/items/8ee4c408640700e52274


# 出力用の文字列
msg = 'name : {0}, datetime : {1}, hash : {2}'

path = pathlib.Path('.')

for file in path.iterdir():
    if file.match('*.py'):
        # ファイルから必要とする情報を取得
        name = file.name
        ts1 = file.stat().st_mtime
        ts2 = datetime.datetime.fromtimestamp(ts1)
        lastupdate = ts2.strftime('%Y-%m-%d-%H%M%S')
        hashstr = ''

        # ハッシュ値の生成準備(md5)
        h = hashlib.new('md5')
            
        with open(file, 'rb') as f:
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

        # デバッグ用にファイル情報取得結果を出力
        print(msg.format(name, lastupdate, digestFirst))

