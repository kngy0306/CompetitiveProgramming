import bisect, array, sys
input = sys.stdin.readline
 
l, q = map(int, input().split())
cut = array.array('i', [0,l])
 
for i in range(q):
    a,b = map(int, input().split())
    if a == 2:
        index = bisect.bisect_left(cut, b)
        print(cut[index]-cut[index-1])
    else:
        index = bisect.bisect_left(cut, b)
        cut.insert(index, b)









