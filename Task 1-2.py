from pprint import pprint

with open('recipes.txt', 'r', encoding='utf-8') as file:  # открываем файл
    cook_book = {}
    cook_book_dishes = []
    line = file.readline()
    while line:
        while line and line.strip() == '':
            line = file.readline()
        if line.strip() != '':
            name_of_dish = line.strip()
            ingredients_quantity = int(file.readline().strip())
            ingredients = []
            for ingredient_string in range(ingredients_quantity):
                ingredient = file.readline().strip()
                ingredient_dict = {}
                ingr = ingredient.split('|')
                ingredient_dict['ingredient_name'] = ingr[0].strip()
                ingredient_dict['quantity'] = int(ingr[1].strip())
                ingredient_dict['measure'] = ingr[2].strip()
                ingredients.append(ingredient_dict)
            cook_book[name_of_dish] = ingredients
            cook_book_dishes.append(name_of_dish)
            line = file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            if ingredient['ingredient_name'] not in shop_list.keys():
                measure_and_quantity = {}
                measure_and_quantity['measure'] = ingredient['measure']
                measure_and_quantity['quantity'] = ingredient['quantity'] * person_count
                shop_list[ingredient['ingredient_name']] = measure_and_quantity
            else:
                shop_list[ingredient['ingredient_name']]['quantity'] += ingredient['quantity'] * person_count
    pprint(shop_list)


get_shop_list_by_dishes(['Омлет', 'Утка по-пекински'], 6)
