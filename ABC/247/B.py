from collections import defaultdict

N = int(input())

# 辞書は初期値がないとkeyでアクセスできないから、int(0)で初期化
di = defaultdict(int)
li = []

for i in range(N):
    a, b = input().split()
    if a == b:
        di[a] += 1
    else:
        di[a] += 1
        di[b] += 1
    li.append([a, b])
    

res = "Yes"
for a, b in li:
    if di[a] != 1 and di[b] != 1:
        res = "No"
        break


print(res)