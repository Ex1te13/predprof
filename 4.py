import csv


def promocod_generator(nazv, datap):
    """ Функция promocod_generator создает уникальные промокоды исходя из названия продукта и даты его поступления
    nazv - название продукта, datap - дата поступления продукта"""
    datap = datap.split(".")
    l = datap[1][::-1]
    promocod = nazv[:2].upper() + datap[0] + nazv[-1].upper() + nazv[-2].upper() + l
    return promocod


with open("products.csv", encoding="utf-8-sig") as file:
    reader = csv.DictReader(file, delimiter=";")
    reader = list(reader)
    for line in reader:
        line["promocode"] = promocod_generator(line["product"], line["Date"])

with open("product_promo.csv", "w", encoding="utf-8-sig", newline="") as file1:
    w = csv.DictWriter(file1, delimiter=";", fieldnames = ["Category", "product", "Date", "Price per unit", "Count", "promocode"])
    w1 = csv.writer(file1, delimiter=";")
    w1.writerow(["Category", "product", "Date", "Price per unit", "Count", "promocode"])
    w.writerows(reader)