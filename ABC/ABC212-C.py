n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
ans = 10**10
ai = 0
bi = 0

while ai < n and bi < m:
    ans = min(abs(a[ai]-b[bi]), ans)

    if a[ai] < b[bi]:
        ai += 1
    else:
        bi += 1

print(ans)
