import math

# 累積和
print("累積和(1〜10)")
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = [0]*len(x)

for i in range(len(x)):
    if i == 0:
        s[i] = x[i]
    else:
        s[i] = s[i-1]+x[i]

print(s)

# 約数全列挙
print("\n約数列挙(10000)")
n = 10000

for i in range(1, int(math.sqrt(n))+1):
    if n % i == 0:
        print(i)

# 素因数分解
print("\n素因数分解(2020)")
ans = dict()
n = 2020

for i in range(2, int(math.sqrt(n))+1):
    if n % i != 0:
        continue

    cnt = 0
    while(n % i == 0):
        cnt += 1
        n /= i
    ans[i] = cnt

if n != 1:
    ans[int(n)] = 1

print(ans)
