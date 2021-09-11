# 最短経路を求めるので幅優先探索
'''
高橋君がスタートとゴールの位置を適切に定めたとき、青木君の移動回数は最大で何回になるでしょうか？

3 3
...
...
...

'''

from collections import deque
import sys
input = sys.stdin.readline

H,W = map(int, input().split())
s = [input() for _ in range(H)]
ans = 0

dx_dy = [[1,0], [0,1], [-1,0], [0,-1]]

for h in range(H):
    for w in range(W):
        
        if s[h][w] == ".":
            visited = [[0]*W for _ in range(H)]
            q = deque([[h,w]])
            visited[h][w] = 1
            
            while q:
                y,x = q.popleft()
                
                for i in range(4):
                    y2 = y + dx_dy[i][1]
                    x2 = x + dx_dy[i][0]
                    
                    if y2 < 0 or y2 >= H or x2 < 0 or x2 >= W:
                        continue
                    if s[y2][x2] != "#" and visited[y2][x2] == 0:
                        visited[y2][x2] = visited[y][x] + 1
                        q.append([y2,x2])
                        
            for i in range(H):
                for j in range(W):
                    ans = max(ans, visited[i][j])

print(ans-1)