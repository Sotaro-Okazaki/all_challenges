import csv

all_lists =[

    ["トップガン", "リスキービジネス", "マイノリティリポート"],

    ["タイタニック", "ザ・レヴナント", "インセプション"],

    ["トレーニングデイ", "マンオンファイアー", "フライト"]

]

with open("films_japanese.csv", "w", newline="", encoding="cp932") as f:
    w = csv.writer(f, delimiter=",")
    for i in range(0, 3):
        w.writerow(all_lists[i])
