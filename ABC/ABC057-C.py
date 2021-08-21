# 約数列挙 
'''
A>BA>B  であるような場合は、特に考えなくてもよいことに注意しましょう
(A = 3,B = 15 A = 3,B = 15 のケースと、A = 15,B = 3 A = 15,B = 3 のケースは答えが全く一緒です)。
'''

import math

N = int(input())


def F(a, b):
    return max(len(str(a)), len(str(b)))

ans = 10**10
for i in range(1, int(math.sqrt(N))+1):
  if (N % i == 0):
    ans = min(ans, F(i, N//i))

print(ans)