x = input()

same = True
step = True
for i in range(len(x)-1):
    if x[i] != x[i+1]:
        same = False
    a = int(x[i])
    b = int(x[i+1])
    if (a+1) % 10 != b:
        step = False

if same or step:
    print("Weak")
else:
    print("Strong")
