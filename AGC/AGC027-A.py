# https://atcoder.jp/contests/agc027/tasks/agc027_a

# 要求数が少ない子から順番に配り、あまりがある場合は-1する

N, x = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

happy = 0
for i in a:
    if x >= i:
        happy += 1
        x -= i
    

if x > 0 and happy == N:
    happy -= 1
print(happy)