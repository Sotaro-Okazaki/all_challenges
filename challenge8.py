def f(x):
    return x // 2

def g(y):
    print(y * 4)

a = input("a=")
a = int(a)

g(f(a))
