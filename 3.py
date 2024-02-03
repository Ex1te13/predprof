import csv

with open("products.csv", encoding="utf-8-sig") as file:
    reader = list(csv.DictReader(file, delimiter=";"))

category1 = input()
while category1 != "молоко":
    col = []
    col_prod = {}
    for line in reader:
        if line["Category"] == category1:
            col.append(float(line["Count"]))
            col_prod[line["Count"]] = line["product"]
    if len(col) == 0:
        print("Такой категории не существует в нашей БД")
    else:
        min_col = min(col)
        prod = col_prod[str(min_col)]
        print(f"В категории: {category1} товар: {prod} был куплен {int(min_col)} раз")
    category1 = input()