H, W, N = map(int, input().split())
X, Y = [], []
for i in range(N):
    x, y = map(int, input().split())
    X.append(x)
    Y.append(y)

x_dict = {x: i+1 for i, x in enumerate(sorted(X))}
y_dict = {y: i+1 for i, y in enumerate(sorted(Y))}

for i in range(N):
    print(x_dict[X[i]], y_dict[Y[i]])
