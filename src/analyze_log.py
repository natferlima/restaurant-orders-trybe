def most_request_dish(data_list, customer):
    dish_dic = dict()
    most_request_dish = ['', 0]
    for person, dish, day in data_list:
        if customer == person:
            if dish not in dish_dic:
                dish_dic[dish] = 1
            else:
                dish_dic[dish] += 1
            if dish_dic[dish] > most_request_dish[1]:
                most_request_dish = [dish, dish_dic[dish]]
    return most_request_dish[0]


def quantity_dish_customer(data_list, chosen_dish, customer):
    qt = 0
    for person, dish, day in data_list:
        if person == customer and dish == chosen_dish:
            qt += 1
    return qt


def dishes_not_ordered_by_customer(data_list, customer):
    customer_orders = set()
    all_dishes = set()
    for person, dish, day in data_list:
        if person == customer:
            customer_orders.add(dish)
        all_dishes.add(dish)
    return all_dishes.difference(customer_orders)


def days_customer_was_not(data_list, customer):
    days_customer_was = set()
    all_days = set()
    for person, dish, day in data_list:
        if person == customer:
            days_customer_was.add(day)
        all_days.add(day)
    return all_days.difference(days_customer_was)


def analyze_log(path_to_file):
    if not path_to_file.endswith('.csv'):
        raise FileNotFoundError(f"Extensão inválida: '{path_to_file}'")
    data = []
    try:
        with open(path_to_file, 'r') as file:
            for line in file:
                data.append(line.replace('\n', '').split(","))
        most_request_dish_maria = most_request_dish(data, 'maria')
        quantity_hamburguer_arnaldo = quantity_dish_customer(
            data, 'hamburguer', 'arnaldo')
        dishes_not_ordered_by_joao = dishes_not_ordered_by_customer(
            data, 'joao')
        days_joao_was_not = days_customer_was_not(data, 'joao')
        with open('data/mkt_campaign.txt', 'w') as file:
            file.write(
                f'{most_request_dish_maria}\n'
                f'{quantity_hamburguer_arnaldo}\n'
                f'{dishes_not_ordered_by_joao}\n'
                f'{days_joao_was_not}'
            )
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path_to_file}'")
