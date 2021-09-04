n = int(input())
 
ans = ""
while n > 0:
    if n % 2 == 0:
        ans += "B"
    else:
        ans += "AB"
    n //= 2
 
print(ans[::-1])