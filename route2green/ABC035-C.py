# https://atcoder.jp/contests/abc035/tasks/abc035_c

n,q = list(map(int, input().split()))

dp=[0]*n
for i in range(q):
  l, r = map(int, input().split())
  dp[l-1] += 1
  if (r-1)+1 != n:
    dp[r] -= 1

ans=[0]*n
ans[0]=dp[0]
for i in range(1, n):
  ans[i]=dp[i]+ans[i-1]

for i in ans:
  print(i%2, end="")
print()