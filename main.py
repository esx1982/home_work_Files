# Задача №1
cook_book = {}
def create_dict():
    with open('recipes.txt', encoding='utf-8') as f:
        last_key = ''
        for line in f:
            line = line.strip()
            if line.isdigit():
                continue
            elif line and '|' not in line:
                cook_book[line] = []
                last_key = line
            elif line and '|' in line:
                name, qt, msure = line.split(" | ")
                cook_book.get(last_key).append(dict(ingredient_name=name, quantity=int(qt), measure=msure))
    return cook_book
create_dict()
# Задача №2
dishes = []
for key in cook_book:
    dishes.append(key)
def get_shop_list_by_dishes(dishes, person_count):
    ingridients_quantity = {}
    for dish in dishes:
        # print(dish)
        if dish not in cook_book.keys():
            print('Такого блюда нет в списке рецептов!')
            break
        else:
            for el in cook_book[dish]:
                ingr_name = el['ingredient_name']
                measure = el['measure']
                quantity = el['quantity'] * person_count
                ingridients_quantity[ingr_name] = {'measure': measure, 'quantity': quantity}
    return ingridients_quantity
print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 5))

# Задача №3
def write_new_file():
    num = []
    d1 = 0
    d2 = 0
    d3 = 0
    with open('1.txt', encoding='utf-8') as f1:
        for idx1, l in enumerate(f1):
            d1 += 1
        num.append(d1)

    with open('2.txt', encoding='utf-8') as f2:
        for idx2, l in enumerate(f2):
            d2 += 1
        num.append(d2)

    with open('3.txt', encoding='utf-8') as f3:
        for idx3, l in enumerate(f3):
            d3 += 1
        num.append(d3)
    sorted_num = sorted(num)
    final_file = open("final_file.txt", "w")
    for i in sorted_num:
        if i == d1:
            with open('1.txt', encoding='utf-8') as f1:
                final_file.write(f"{f1.name}\n{d1}\n")
                for idx1, l in enumerate(f1):
                    final_file.write(f"строка № {idx1 + 1} {l.strip()} файла № {f1.name}\n")
        elif i == d2:
            with open('2.txt', encoding='utf-8') as f2:
                final_file.write(f"{f2.name}\n{d2}\n")
                for idx2, l in enumerate(f2):
                    final_file.write(f"строка № {idx2 + 1} {l.strip()} файла № {f2.name}\n")
        elif i == d3:
            with open('3.txt', encoding='utf-8') as f3:
                final_file.write(f"{f3.name}\n{d3}\n")
                for idx3, l in enumerate(f3):
                    final_file.write(f"строка № {idx3 + 1} {l.strip()} файла № {f3.name}\n")
    final_file.close()

write_new_file()