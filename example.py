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

# from chardet.universaldetector import UniversalDetector
#
# detector = UniversalDetector()
# with open('recipes.txt', 'rb') as fh:
#     for line in fh:
#         detector.feed(line)
#         if detector.done:
#             break
#     detector.close()
# print(detector.result)
# Задача №3

with open('1.txt', encoding='utf-8') as f:
    for idx1, l in enumerate(f):
        print(idx1, l.strip())

with open('2.txt', encoding='utf-8') as f:
    for idx2, l in enumerate(f):
        print(idx2, l.strip())

with open('3.txt', encoding='utf-8') as f:
    for idx3, l in enumerate(f):
        print(idx3, l.strip())