# 累積和
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
s = [0]*len(x)

for i in range(len(x)):
  if i == 0:
    s[i] = x[i]
  else:
    s[i] = s[i-1]+x[i]

print(s)

# 約数全列挙
