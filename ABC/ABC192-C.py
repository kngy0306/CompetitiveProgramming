'''
入力例 1 
314 2
出力例 1 
693

 a0=314
 a1=f(314)=431−134=297
 a2=f(297)=972−279=693
です。
'''

import itertools
import sys
sys.setrecursionlimit(100000)


def fnc(num, cnt, end):
    if cnt == end:
        print(num)
        exit()

    num = str(num)
    l = [int(i) for i in num]

    mi_int = sorted(l)
    mi_str = [str(i) for i in mi_int]
    ma_int = sorted(l, reverse=True)
    ma_str = [str(i) for i in ma_int]

    a, b = "", ""
    for i in range(len(num)):
        a += ma_str[i]
        b += mi_str[i]

    cnt += 1
    a = int(a)
    b = int(b)
    fnc(a-b, cnt, end)


num, end = map(int, input().split())
cnt = 0
fnc(num, cnt, end)
