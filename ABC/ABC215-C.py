import itertools
 
s, k = input().split()
k = int(k)
 
l = [i for i in s]
 
ans = set()
 
for i in itertools.permutations(l, len(s)):
    tmp = ""
    for j in range(len(s)):
        tmp += i[j]
    ans.add(tmp)
 
print(sorted(ans)[k-1])