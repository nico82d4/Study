import pathlib
import hashlib



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



def show_recursive(path):
    msg = '{0}, {1}'
    for po in path.iterdir():
        if po.is_dir():
            show_recursive(po)
        elif po.is_file():
            print(msg.format(po, create_hash(po)))



path = pathlib.Path('.')
show_recursive(path)
