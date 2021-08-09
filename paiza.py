N = int(input())

h = [[0]*(N+2) for i in range(N+2)]

for i in range(1, N+1):
    li = list(map(int, input().split()))
    for j in range(1, N+1):
        h[i][j] = li[j-1]

ans = []
for i in range(1, N+1):
    for j in range(1, N+1):
        height = h[i][j]
        if height > h[i-1][j] and height > h[i+1][j] and height > h[i][j-1] and height > h[i][j+1]:
            ans.append(height)

print(ans)
