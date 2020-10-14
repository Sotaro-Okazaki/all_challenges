sentence = "四月の晴れた寒い日で、時計がどれも十三時を打っていた。"

index_touten = sentence.index("、")

sentence = sentence[0: index_touten]

print(sentence)
