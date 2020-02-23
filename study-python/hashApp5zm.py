# 参考
# Pythonで巨大ファイルのハッシュ値（チェックサム）を求める方法 (Qiita)
# https://qiita.com/5zm/items/4592f1b0e036bd9505c8


import hashlib
import argparse

# main
if __name__ == "__main__":

    # ★ポイント1
    parser = argparse.ArgumentParser(description='hashApp')
    parser.add_argument('input', help='Input file path')
    parser.add_argument('--alg', help='Input algorithm (md5, sha1, sha224, sha256, sha384, sha512)', default = 'sha1')
    args = parser.parse_args()

    filePath = args.input
    alg = args.alg

    # ★ポイント2
    if 'md5' == alg:
        hash = hashlib.md5()
    elif 'sha224' == alg:
        hash = hashlib.sha224()
    elif 'sha256' == alg:
        hash = hashlib.sha256()
    elif 'sha384' == alg:
        hash = hashlib.sha384()
    elif 'sha512' == alg:
        hash = hashlib.sha512()
    else:
        hash = hashlib.sha1()

    # ★ポイント3
    with open(filePath, 'rb') as f:
        while True:
            chunk = f.read(2048 * hash.block_size)
            if len(chunk) == 0:
                break

            hash.update(chunk)

    # ★ポイント4
    digest = hash.hexdigest()
    print("{0}({1}) : {2}".format(filePath, alg, digest))
