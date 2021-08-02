N = int(input())
a = [list(map(int, input().split())) for i in range(N)]

dp = [[0]*3 for i in range(N)]
dp[0] = a[0]

for i in range(1, N):
    for j in range(3):
        if j == 0:
            dp[i][j] = a[i][j] + max(dp[i-1][j+1], dp[i-1][j+2])
        elif j == 1:
            dp[i][j] = a[i][j] + max(dp[i-1][j-1], dp[i-1][j+1])
        else:
            dp[i][j] = a[i][j] + max(dp[i-1][j-2], dp[i-1][j-1])
print(max(dp[N-1]))
