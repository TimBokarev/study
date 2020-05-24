

def read_file(file_name):

    file_lines = []
    with open(file_name) as fi:
        for line in fi:
            file_lines.append(line.rstrip())
    return file_lines


def cook_book_creation(recipes_list):

    dish = []
    cook_book = {}
    recipes_list.append('')

    for items in recipes_list:

        if items != '':
            dish.append(items)
        else:
            cutted_dish = dish.copy()
            cutted_dish.pop(0)
            cutted_dish.pop(0)

            list_of_ingradients = []
            for string in cutted_dish:
                dict = {}
                string = string.split(" | ")
                dict["ingredient_name"] = string[0]
                dict["quantity"] = string[1]
                dict["measure"] = string[2]
                list_of_ingradients.append(dict)

            cook_book[dish[0]] = list_of_ingradients
            dish = []

    return cook_book


book = cook_book_creation(read_file("recipes.txt"))


for key in book:
    print(key, end=" - ")
print()
dishes_request = input("введите через запятую блюда из предлагаемого списка: ")
choice = dishes_request.split(',')
guests_number = int(input("введите кол-во гостей: "))
print(choice)

# choice = ["Омлет", "Фахитос", "Утка по-пекински"]
# guests_number = 2

def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    shop_list_addition = {}
    for dish in book:

        if dish in dishes:

            for k in book.get(dish):

                shop_items = {}
                shop_items["measure"] = k.get("measure")
                shop_items["quantity"] = guests_number * int(k.get("quantity"))
                ingradient = k.get("ingredient_name")
                shop_list_addition[ingradient] = shop_items

            for item in shop_list_addition:

                if item in shop_list:
                    dict1 = shop_list_addition.get(item)
                    dict2 = shop_list.get(item)
                    qua1 = dict1.get("quantity")
                    qua2 = dict2.get("quantity")
                    mes = dict2.get("measure")
                    quames = {}
                    quames["measure"] = mes
                    quames["quantity"] = int(qua1) + int(qua2)
                    shop_list[item] = quames

                else:
                    shop_list[item] = shop_list_addition.get(item)

    return shop_list


print(get_shop_list_by_dishes(choice, guests_number))


# {
#   'Картофель': {'measure': 'кг', 'quantity': 2},
#   'Молоко': {'measure': 'мл', 'quantity': 200},
#   'Помидор': {'measure': 'шт', 'quantity': 4},
#   'Сыр гауда': {'measure': 'г', 'quantity': 200},
#   'Яйцо': {'measure': 'шт', 'quantity': 4},
#   'Чеснок': {'measure': 'зубч', 'quantity': 6}
# }


# cook_book = {
#   'Омлет': [
#     {'ingredient_name': 'Яйцо', 'quantity': 2, 'measure': 'шт.'},
#     {'ingredient_name': 'Молоко', 'quantity': 100, 'measure': 'мл'},
#     {'ingredient_name': 'Помидор', 'quantity': 2, 'measure': 'шт'}
#     ],
#   'Утка по-пекински': [
#     {'ingredient_name': 'Утка', 'quantity': 1, 'measure': 'шт'},
#     {'ingredient_name': 'Вода', 'quantity': 2, 'measure': 'л'},
#     {'ingredient_name': 'Мед', 'quantity': 3, 'measure': 'ст.л'},
#     {'ingredient_name': 'Соевый соус', 'quantity': 60, 'measure': 'мл'}
#     ],
#   'Запеченный картофель': [
#     {'ingredient_name': 'Картофель', 'quantity': 1, 'measure': 'кг'},
#     {'ingredient_name': 'Чеснок', 'quantity': 3, 'measure': 'зубч'},
#     {'ingredient_name': 'Сыр гауда', 'quantity': 100, 'measure': 'г'},
#     ]
#   }