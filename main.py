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

print(cook_book)