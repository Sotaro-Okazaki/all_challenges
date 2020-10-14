import cubed

a = input("Type a number:")

try:
    a = int(a)
    cubed.f(a)

except ValueError:
    print("Invalid input")
