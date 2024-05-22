def zadanie1():
    import json
    file = '10.1.JSON'
#'r': файл должен быть открыт в режиме чтения ('r').
#encoding='utf-8':указывает кодировку файла.указана кодировка UTF-8, поддерживает
# широкий спектр символов и является стандартом для текстовых файлов.
    with open(file, 'r', encoding='utf-8') as file1:
        zagryzka = json.load(file1)
        # Перебираем каждый продукт в списке
        for product in zagryzka['products']:
            print(f"Название: {product['name']} Цена: {product['price']}")
            print(f"Вес: {product['weight']}")
            if product['available']:
                print("В наличии")
            else:
                print("Нет в наличии!")
            print()

def zadanie2():
    import json
    def add_product_and_display():
        file = '10.1.JSON'
        # Спрашиваем у пользователя данные о продукте
        name = input("Введите название продукта: ")
        price = float(input("Введите цену продукта: "))
        weight = float(input("Введите вес продукта: "))
        available = input("Продукт доступен? (да/нет): ").lower() == 'да'

        # Загружаем данные
        with open(file, 'r', encoding='utf-8') as file1:
            zagryzka = json.load(file1)

        # Добавляем новый продукт
        new_product = {
            'name': name,
            'price': price,
            'weight': weight,
            'available': available
        }
        zagryzka['products'].append(new_product)

        # Записываем обновленные данные в файл
        with open(file, 'w', encoding='utf-8') as file1:
            json.dump(zagryzka, file1, ensure_ascii=False, indent=4)

        # Выводим содержимое итогового файла на экран
        print("\nОбновленное содержимое файла:")
        with open(file, 'r', encoding='utf-8') as file1:
            print(file1.read())

    # добавления продукта и вывод содержимого файла
    add_product_and_display()

def zadanie3():
    file = open('en-ru.txt', 'r')
    rows = file.readlines()
    ru_en = {}
    for row in rows:
        words = row.strip().split(' - ')
        if len(words) == 2:
            en = words[0]
            ru_words = words[1].split(', ')
            for word in ru_words:
                ru_en[word] = en
    file = open('ru-en.txt', 'w')
    sort = dict(sorted(ru_en.items()))
    for ru, en in sort.items():
        file.write(f"{ru} - {en}\n")

while True:
    print('1. Список')
    print('2. Список доп ')
    print('3. Перевод')
    print('4. Выход')
    a = int(input('Выберите действие: '))
    if a == 1:
        zadanie1()
    elif a == 2:
        zadanie2()
    elif a == 3:
        print(zadanie3())
    elif a == 4:
        break
    else:
        print('Неверное действие')