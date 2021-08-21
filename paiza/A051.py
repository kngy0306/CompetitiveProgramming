H, W = map(int, input().split())
s = [list(map(int, input().split())) for i in range(H)]

dp = [[0]*W for i in range(H)]
dp[0] = s[0]

for i in range(1, H):
  for j in range(W):
    if j == 0:
      dp[i][j] = s[i][j] + max(dp[i-1][j], dp[i-1][j+1])
    elif j == W-1:
      dp[i][j] = s[i][j] + max(dp[i-1][j], dp[i-1][j-1])
    else:
      dp[i][j] = s[i][j] + max(dp[i-1][j], dp[i-1][j-1], dp[i-1][j+1])

print(max(dp[-1]))