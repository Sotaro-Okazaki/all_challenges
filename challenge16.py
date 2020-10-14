what = input("What did you write yesterday?:")
who = input("Who did you send to what you wrote?:")

sentence = "私は昨日{}を書いて、{}に送った！"

result = sentence.format(what, who)
print(result)
