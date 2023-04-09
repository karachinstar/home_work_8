import json


class Orders:
    def __init__(self, orders_file):
        self.orders_file = orders_file
        self.order_list = []
        self.load_orders()

    def __str__(self):
        res = ''
        for order in self.order_list:
            res += f"Товар: {order['item']}\n" \
                   f"Количество: {order['quantity']}\n" \
                   f"Цена: {order['price']}\n" \
                   f"Покупатель: {order['buyer']}\n" \
                   f"Дата: {order['date']}\n\n"
        return res

    def add_order(self, order):
        self.order_list.append(order)

    def data_to_file(self):
        return {'orders': self.order_list}

    def load_orders(self):
        with open(self.orders_file) as orders_stream:
            data = json.load(orders_stream)
            for order in data['orders']:
                self.order_list.append(order)

    def write_order_to_json(self, order_data, res_file="hw_orders.json"):
        self.add_order(order_data)
        with open(res_file, "w") as orders_stream:
            json.dump(self.data_to_file(), orders_stream, indent=4)
            print("JSON записали.")


obj = Orders("orders.json")

obj.write_order_to_json({'item': 'слон',
                         'quantity': 1,
                         'price': 100,
                         'buyer': 'You',
                         'date': '01.01.2023'})