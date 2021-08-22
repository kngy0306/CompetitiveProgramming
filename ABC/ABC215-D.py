# https://www.youtube.com/watch?v=NxuL8oOwIvM

#TLEで✕

import math
 
n, m = map(int, input().split())
a = list(map(int, input().split()))

A = 100001
x = [0]*A
for i in range(A):
  if i in a:
    x[i] = 1
x[1]=0

# 1除く全ての約数をチェックする
y = []
for i in range(2, A):
  num = i
  flag = False
  while num < A:
    if x[num]:
      flag = True
      break
    num += i
  if flag:
    y.append(i)

# ↑で求めた約数の倍数の箇所をすべて1で埋める
for i in y:
  j = i
  while j < A:
    x[j] = 1
    j += i

cnt=0
ans=[]
for i in range(1, m+1):
  if x[i] == 0:
    ans.append(i)
    cnt+=1

print(cnt)
for i in ans:
  print(i)



# cnt = 0
# ans = []
 
# for i in range(m):
#     c = 0
#     for j in range(n):
#         if math.gcd(a[j], i) != 1: 
#             break
#         else:
#             c += 1
#     if c == n:
#         cnt += 1
#         ans.append(i)
 
# print(cnt)
# for i in ans:
#     print(i)