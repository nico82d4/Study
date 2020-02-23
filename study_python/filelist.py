from pathlib import Path
import datetime
import hashlib



# # カレントパス内のファイル一覧を表示
# p = Path("./")
# print(list(p.glob("*")))

# # 区切り線
# print('==='*3)

## こちらは通らない
#print(Path('.').glob('*.py'))

# 出力用の文字列
msg = 'name : {0}, ts : {1}, hash {2}'

# 調査するパス
p = Path("./")

for child in p.iterdir():

    # print(child.stat().st_atime_ns)
    name = child
    ts1 = child.stat().st_mtime
    ts2 = datetime.datetime.fromtimestamp(ts1)
    lastupdate = ts2.strftime('%Y-%m-%d-%H%M%S')
    hashstr = ""

    # h = hashlib.new('md5')
        
    # with open(child, 'rb') as f:
        
    #     # データがなくなるまでループします
    #     while binaryData:
    #         binaryData = f.read(2048 * h.block_size)
            
    #         if len(binaryData) == 0:
    #             break
                
    #         h.update(binaryData)

    # # ハッシュオブジェクトを16進数で出力します
    # hashstr = h.hexdigest()
    
    # 結果の出力
    print(msg.format(name, lastupdate, hashstr))

