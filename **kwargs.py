user = ('kona', 22)
print(user)
print(*user)


def show(**kwargs):
    for name, age in kwargs.items():
        print(name, age)


d = {'mayu': 20, 'seira': 20, 'ayame': 17}
show(**d)
