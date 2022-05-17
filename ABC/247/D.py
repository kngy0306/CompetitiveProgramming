# x: ある数, c: その個数
# 上記の場合、xをc分配列に突っ込みたくなったが、[[x, c], ...]という形式で格納することで
# 取り出して計算するときはx*cでその数が算出できる
# ↑　ランレングス符号化

from collections import deque
d = deque()

Q = int(input())

for _ in range(Q):
    q = input().split()
    if q[0] == "1":
        x = int(q[1])
        c = int(q[2])
        d.append([x, c])
    else:
        res = 0
        count = int(q[1])
        while count > 0:
            if d[0][1] > count:
                res += d[0][0]*count
                d[0][1] -= count
                count = 0
            else:
                x, c = d.popleft()
                res += x * c
                count -= c
        print(res)