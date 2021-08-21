N, M, L = map(int, input().split())

d = [list(map(int, input().split())) for i in range(N)]
a = [0]*M
ans = [0]*(L-1)

for i in range(L):
    if i == 0:
        before = list(map(int, input().split()))
        continue

    tmp = list(map(int, input().split()))
    for j in range(M):
        a[j] = tmp[j] - before[j]

    ans[i-1] = d.index(a)+1
    before = tmp

for i in range(len(ans)):
    print(ans[i])
