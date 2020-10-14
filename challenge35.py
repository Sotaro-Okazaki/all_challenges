import random

def hungman(word):
    wrong = 0
    stages = ["",
              "_______       ",
              "|             ",
              "|      |      ",
              "|      0      ",
              "|    ／|＼    ",
              "|    ／ ＼    ",
              "|             "
              ]
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ!")
    while wrong < len(stages) - 1:
        print("\n")
        msg = "1文字予想してね:"
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = "$"
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち!")
            print("_".join(board))
            win = True
            break
    if not win:
        print("\n".join(stages[0:wrong + 1]))
        print("あなたの負け!正解は {}.".format(word))

word_list = ["mouse", "cow", "tiger", "rabbit", "doragon", "snake", "horse", "sheep", "monkey", "bird", "dog", "boar"]

a = random.randint(0, len(word_list) - 1)
picked_word = word_list[a]
hungman(picked_word)
