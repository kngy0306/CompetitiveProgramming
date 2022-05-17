N = int(input())

def f(x):
    if x == 1:
        return 1
    else:
        return (str(f(x-1)) + " " + str(x) +  " " + str(f(x-1)))

print(f(N))