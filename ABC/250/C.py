N, Q = map(int, input().split())

ball_num = {i:i for i in range(1, N+1)} # 数：位置
num_ball = {i:i for i in range(1, N+1)} # 位置：数

for i in range(Q):
    x = int(input()) # 指定されたボール
    
    left_p = ball_num[x] # 指定されたボールのいち
    if left_p < len(ball_num):
        right_p = left_p+1 # その右隣のいち
    else:
        right_p = left_p-1
    
    y = num_ball[right_p] # 右のボール
    
    ball_num[x] = right_p
    ball_num[y] = left_p
    num_ball[left_p] = y
    num_ball[right_p] = x

print(*list(num_ball.values()))