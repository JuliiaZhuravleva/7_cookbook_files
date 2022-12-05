def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        for dish_ingredient in cook_book[dish]:
            di_name = dish_ingredient['ingredient_name']
            di_quantity = dish_ingredient['quantity']
            if di_name in shop_list_by_dishes:
                shop_list_by_dishes[di_name]['quantity'] += di_quantity * person_count
            else:
                di_measure = dish_ingredient['measure']
                shop_list_by_dishes[di_name] = {"measure": di_measure, "quantity": di_quantity * person_count}
    return shop_list_by_dishes


cook_book = {}

with open('recipes.txt', 'rt', encoding='utf8') as file:
    for recipe in file:
        dish_name = recipe.strip()
        ingredients_count = file.readline()
        ingredients = []
        for i in range(int(ingredients_count)):
            ingredient = file.readline()
            ingredient_name, quantity, measure = ingredient.strip().split(' | ')
            ingredients.append({'ingredient_name': ingredient_name,
                                "quantity": int(quantity),
                                "measure": measure})
        blank_line = file.readline()
        cook_book[dish_name] = ingredients

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))