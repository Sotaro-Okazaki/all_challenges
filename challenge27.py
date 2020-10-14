numbers = [2, 6, 7, 11, 17, 19]

while True:
    x = input("Type a number or \"q\".(If you type \"q\",you can quit this game.):")
    if x == "q":
        break
    else:
        try:
            x = int(x)
            if x in numbers:
                print("You're right!")
            else:
                print("Sorry, you're wrong.")
        except ValueError:
            print("Sorry, type a number or \"q\".")
