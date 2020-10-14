def f(x):
    """
    引数x:文字列
    戻り値:整数x
    """

    try:
        x = float(x)
        return x
    except ValueError:
        print("x must be a number")

a = input("type a number:")
print(f(a))

