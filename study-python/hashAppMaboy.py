# 参考
# Python3でファイルのハッシュを計算する。(Qiita)
# https://qiita.com/maboy/items/8ee4c408640700e52274



# モジュールをインポートします
import hashlib

# ハッシュアルゴリズムを決めます
algo = 'md5'

# ハッシュオブジェクトを作ります
h = hashlib.new(algo)

# 分割する長さをブロックサイズの整数倍に決めます
Length = hashlib.new(algo).block_size * 0x800

# 大きなバイナリデータを用意します
path = 'test.zip'
with open(path,'rb') as f:
    BinaryData = f.read(Length)

    # データがなくなるまでループします
    while BinaryData:

        # ハッシュオブジェクトに追加して計算します。
        h.update(BinaryData)

        # データの続きを読み込む
        BinaryData = f.read(Length)

# ハッシュオブジェクトを16進数で出力します
print(algo,h.hexdigest())
