N, K = map(int, input().split())
h = list(map(int, input().split()))

dp = [0]*N

for i in range(1, N):
    tmp = 1000000001
    for j in range(1, K+1):
        if i-j < 0:
            break
        tmp = min(abs(h[i]-h[i-j])+dp[i-j], tmp)
    dp[i] = tmp

print(dp[-1])
