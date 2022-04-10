import sys
from bisect import bisect_left
input = sys.stdin.readline

N, Q = map(int, input().split())
A = list(map(int, input().split()))
x = [int(input()) for _ in range(Q)]
A.sort()


for i in x:
    print(N - bisect_left(A, i))