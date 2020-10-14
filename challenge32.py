answer = input("What color do you like?:")

with open("favorite_color.txt", "w") as f:
    f.write(answer)
