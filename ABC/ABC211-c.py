# 動的計画法
s = input()

t = "chokudai"

dp = [[0]*(len(s)+1) for i in range(len(t)+1)]

m = 1000000007

for i in range(len(s)+1):
    dp[0][i] = 1

for i in range(1, len(t)+1):
    for j in range(1, len(s)+1):
        if t[i-1] == s[j-1]:
            dp[i][j] = (dp[i][j-1]+dp[i-1][j-1]) % m
        else:
            dp[i][j] = (dp[i][j-1]) % m

print(dp[-1][-1])
