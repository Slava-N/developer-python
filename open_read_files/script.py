with open('recipe.txt', encoding='utf-8') as document:
    menu={}
    for line in document:
        dish = line.strip()
        number_of_products = int(document.readline().strip())
        product_items = []
        for product in range(number_of_products):
            raw_line = document.readline().strip().split(' | ')
            product_info = {'product' : raw_line[0], 'quantity' : int(raw_line[1]), 'unit' : raw_line[2]}
            product_items.append(product_info)
        empty_line = document.readline().strip()
        menu[dish] = product_items
    print('В нашем меню представлены следующие блюда: \n {}'.format(list(menu.keys())))

def get_shop_list_by_dishes(dishes, people_count):
    shop_list = {}
    for dish in dishes:
        for ingridient in dishes[dish]:
            new_shop_item = dict(ingridient)
            # пересчитали ингрединты по количеству людей
            new_shop_item['quantity'] = new_shop_item['quantity'] * people_count[dish]
            if new_shop_item['product'] not in shop_list:
                shop_list[new_shop_item['product']] = new_shop_item
            else:
                shop_list[new_shop_item['product']]['quantity'] += new_shop_item['quantity']
    return shop_list

def print_shop_list(shop_list):
    for key, shop_list_item in shop_list.items():
        print("{product} {quantity} {unit}".format(**shop_list_item))

def create_shop_list(people_count, *order):
    # получить блюда из кулинарной книги
    dishes = {}
    people_count_dishes = {}
    for dish in order:
        if dish in dishes: people_count_dishes[dish] = people_count_dishes[dish] + people_count
        else:
            if dish in menu:
                dishes[dish] = menu[dish]
                people_count_dishes[dish] = people_count
            else:
                print('Блюдо "{}" закончилось'.format(dish))
    print('Мы приготовим Вам: {0}'.format(people_count_dishes), sep='\n')
    #заполнили список покупок
    shop_list = get_shop_list_by_dishes(dishes, people_count_dishes)
    # Вывести список покупок
    print('Список покупок: ')
    print_shop_list(shop_list)


print('Выберите первое блюдо: ')
first_dish = input()
print('Выберите второе блюдо: ')
second_dish = input()
print('Выберите третье блюдо: ')
third_dish = input()
print('На сколько человек?')
people_count = int(input())
create_shop_list(people_count, first_dish, second_dish, third_dish)
