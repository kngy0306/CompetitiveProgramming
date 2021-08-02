N = int(input())
h = list(map(int, input().split()))

dp = [0]*N  # len 4

for i in range(1, N):  # 1 ~ 3
    if i > 1:
        dp[i] = min(abs(h[i]-h[i-1])+dp[i-1], abs(h[i]-h[i-2])+dp[i-2])
    else:
        dp[i] = dp[i-1] + abs(h[i]-h[i-1])

print(dp[-1])
