# https://atcoder.jp/contests/abc079/tasks/abc079_d

def warshall_floyd(dp):
    for k in range(10):  # 経由点
        for i in range(10):  # 始点
            for j in range(10):  # 終点
                dp[i][j] = min(dp[i][j], dp[i][k]+dp[k][j])
    return dp


h, w = map(int, input().split())
c = [list(map(int, input().split())) for _ in range(10)]

dp = warshall_floyd(c)

ans = 0
for i in range(h):
    a = list(map(int, input().split()))
    for b in a:
        if b != -1:
            ans += dp[b][1]
print(ans)
