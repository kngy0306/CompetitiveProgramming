from collections import defaultdict

N = int(input())

di = defaultdict(int)

point = 0
k = ""
for i in range(N):
    S, T = input().split()
    
    if not S in di:
        di[S] = i+1
        if point < int(T):
            k = S
            point = int(T)


print(di[k])