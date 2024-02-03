import csv

with open("products.csv", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    header = next(reader)
    header.append("total")
    answer = list(reader)
    for line in answer:
        total = float(line[-2]) * float(line[-1])
        line.append(str(total))
    zakusk_tot = 0
    for line1 in answer:
        if line1[0] == "Закуски":
            zakusk_tot += float(line1[-1])
    print(zakusk_tot)

with open("products_new.csv", "w", encoding="utf-8-sig", newline="") as file1:
    w = csv.writer(file1, delimiter=";")
    w.writerow(header)
    w.writerows(answer)
