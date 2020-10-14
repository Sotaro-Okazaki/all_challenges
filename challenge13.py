Sotaro = {"height": "180cm",
          "weight": "85kg",
          "favorite_color": "yellow"}

infomation = input("""Which information do you wanna learn about me?
Choose from height, weight, and favorite_color:""")

if infomation in Sotaro:
    print(Sotaro[infomation])
else:
    print("Sorry, I can't tell you that infomation.")

