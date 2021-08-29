'''
文字列 S の各文字を並べ替えて作ることが可能な文字列を辞書順にすべて列挙したとき、前から K 番目にくる文字列を求めてください。
aab 2
出力例 1 
aba
文字列 aab の各文字を並べ替えて作ることが可能な文字列は { aab, aba, baa } の 3 つですが、このうち辞書順で前から 2 番目にくるものは aba です。
'''

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