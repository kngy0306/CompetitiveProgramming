# setで重複を除いた列挙を作成
# combinationsで組み合わせを作成
# combinations('ABCD', 2) --> AB AC AD BC BD CD
# combinations(range(4), 3) --> 012 013 023 123

from itertools import combinations

N, W = map(int, input().split())

li = list(map(int, input().split()))

ans = set()

for i in list(combinations(li, 1)):
    a = sum(i)
    if a <= W:
        ans.add(a)

for i in list(combinations(li, 2)):
    a = sum(i)
    if a <= W:
        ans.add(a)

for i in list(combinations(li, 3)):
    a = sum(i)
    if a <= W:
        ans.add(a)
    
print(len(ans))