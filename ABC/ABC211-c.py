s = input()
t = "chokudai"
m = 1000000007

dp = [[0]*(len(s)+1) for i in range(len(t)+1)]
for i in range(len(s)+1):
    dp[0][i] = 1

for i in range(1,len(t)+1):
    t_index = i-1
    
    for j in range(1, len(s)+1):
        s_index = j-1
        if s[s_index] == t[t_index]:
            dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]) % m
        else:
            dp[i][j] = (dp[i][j-1]) % m
    print(dp[i])
print(dp[len(t)][len(s)])