import csv


def sort_vstavk(data):
    """ Функция sort_vstavk сортирует полученный массив по возрастанию используя метод сортировки вставками
    data - массив который нужно отсортировать"""
    for i in range(len(data)):
        j = i - 1
        str1 = data[i]
        while j >= 0 and str1 < data[j]:
            data[j + 1] = data[j]
            data[j] = str1
            j -= 1
    return data


with open("products.csv", encoding="utf-8-sig") as file:
    reader = csv.reader(file, delimiter=";")
    header = next(reader)
    answer = list(reader)

    categories = []
    for line in answer:
        categories.append(line[0])
    categories = list(set(categories))
    categories = sort_vstavk(categories)

    ceni = []
    ceni_tovar = {}
    for line1 in answer:
        if line1[0] == categories[0]:
            ceni.append(line1[-2])
            ceni_tovar[line1[-2]] = line1[1]
    ceni = sort_vstavk(ceni)
    prod = ceni_tovar[ceni[-1]]
    print(f"В категории: {categories[0]} самый дорогой товар: {prod} его цена за единицу товара составляет {ceni[-1]}")