import csv

all_lists =[
    ["top Gun", "Risky Business", "Minority Report"],

    ["Titanic", "The Revenant", "Inception"],

    ["Traning Day", "Man on Fire", "Flight"]

]

with open("films.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    w.writerow(all_lists[0])
    w.writerow(all_lists[1])
    w.writerow(all_lists[2])

