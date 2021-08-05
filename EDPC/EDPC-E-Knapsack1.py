N, W = map(int, input().split())
li = [list(map(int, input().split())) for i in range(N)]

w = [0]
v = [0]

dp = [[0]*(W+1) for i in range(N+1)]

for key, value in li:
    w.append(key)
    v.append(value)

for i in range(1, N+1):
    for j in range(1, W+1):
        if w[i] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w[i]] + v[i])
        else:
            dp[i][j] = dp[i-1][j]

print(dp[-1][-1])
