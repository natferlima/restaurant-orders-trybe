from src.analyze_log import (
    most_request_dish, dishes_not_ordered_by_customer, days_customer_was_not)


class TrackOrders:
    # aqui deve expor a quantidade de estoque
    def __init__(self):
        self.all_orders = list()
        self.days = dict()
        self.busiest_day = ['', 0]
        self.least_busiest_day = ['', 0]

    def __len__(self):
        return len(self.all_orders)

    def add_new_order(self, customer, order, day):
        self.all_orders.append([customer, order, day])

    def get_most_ordered_dish_per_customer(self, customer):
        return most_request_dish(self.all_orders, customer)

    def get_never_ordered_per_customer(self, customer):
        return dishes_not_ordered_by_customer(self.all_orders, customer)

    def get_days_never_visited_per_customer(self, customer):
        return days_customer_was_not(self.all_orders, customer)

    def get_busiest_day(self):
        for customer, order, day in self.all_orders:
            if day not in self.days:
                self.days[day] = 1
            else:
                self.days[day] += 1

            if self.days[day] > self.busiest_day[1]:
                self.busiest_day = [day, self.days[day]]
        return self.busiest_day[0]

    def get_least_busy_day(self):
        self.get_busiest_day()
        self.least_busiest_day = self.busiest_day

        for day in self.days:
            if self.days[day] < self.least_busiest_day[1]:
                self.least_busiest_day = [day, self.days[day]]

        return self.least_busiest_day[0]
