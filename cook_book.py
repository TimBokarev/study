

def read_file(file_name):

    file_lines = []
    with open(file_name) as fi:
        for line in fi:
            file_lines.append(line.rstrip())
    return file_lines


k = read_file("recipes.txt")


def cook_book_creation(recipes_list):

    dish = []
    cook_work = {}

    for items in recipes_list:

        if items != '':
            dish.append(items)
        else:
            cutted_dish = dish.copy()
            cutted_dish.pop(0)
            cutted_dish.pop(0)

            list_of_ingradients = []
            dict = {}
            for string in cutted_dish:
                string = string.split(" | ")
                dict["ingredient_name"] = string[0]
                dict["quantity"] = string[1]
                dict["measure"] = string[2]
                list_of_ingradients.append(dict)

            print(list_of_ingradients)

            cook_work[dish[0]] = list_of_ingradients
            dish = []

    print(cook_work)

cook_book_creation(k)




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