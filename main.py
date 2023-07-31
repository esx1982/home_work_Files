from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()
with open('recipes.txt', 'rb') as fh:
    for line in fh:
        detector.feed(line)
        if detector.done:
            break
    detector.close()
# print(detector.result)
cook_book = {}
# Задача №1
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

# print(cook_book)
# Задача №2
dishes = []
for key in cook_book:
    dishes.append(key)
    # print(dishes)

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
    print(ingridients_quantity)
get_shop_list_by_dishes(dishes, 5)