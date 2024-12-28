cook_book = {}

with open('recipes.txt', 'rt', encoding='utf=8') as f:
    for i in f:
        nd = i.strip()
        c = int(f.readline().strip())
        dish_ing = []
        for j in range(c):
            ingr, quant, meas = f.readline().strip().split('|')
            dish_ing.append({'ingredient_name': ingr.strip(), 'quantity': int(quant.strip()), 'measure': meas.strip()})
        f.readline()
        cook_book[nd] = dish_ing


def get_shop_list_by_dishes(dishes, person_count):
    d_list = {}
    for dish in dishes:
        if dish in cook_book:
            for ingr in cook_book[dish]:
                q = ingr['quantity'] * person_count
                if ingr['ingredient_name'] not in d_list:
                    d_list[ingr['ingredient_name']] = {'measure': ingr['measure'], 'quantity': q}
                else:
                    for v in d_list.values():
                        v['quantity'] += q

    return d_list

print(get_shop_list_by_dishes(['Омлет', 'Фахитос'], 2))

