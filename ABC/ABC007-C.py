# 幅優先探索

from collections import deque

# → ↑ ← ↓
dx_dy = [[1, 0], [0, 1], [-1, 0], [0, -1]]

R, C = map(int, input().split())  # 7, 8
sy, sx = map(int, input().split())  # 2, 2
gy, gx = map(int, input().split())  # 4, 5

sx -= 1
sy -= 1
gx -= 1
gy -= 1

c = [input() for i in range(R)]

cost = [[100000]*C for i in range(R)]
cost[sy][sx] = 0
q = deque([[sx, sy]])

while q:
    x, y = q.popleft()
    c2 = cost[y][x] + 1
    for i in range(4):
        x2 = x + dx_dy[i][0]
        y2 = y + dx_dy[i][1]
        if x2 < 0 or x2 >= C or y2 < 0 or y2 >= R or c[y2][x2] == "#":
            continue
        if cost[y2][x2] > c2:
            cost[y2][x2] = c2
            q.append([x2, y2])

ans = cost[gy][gx]
print(ans)
