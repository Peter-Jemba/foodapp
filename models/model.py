#Creating models for the foodapp database

class Order:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price != price:
            ValueError("Price must be equal to price on the order")
        self._price = price


orders_db = []
order1 = Order("Rice", 12.00)
orders_db.append(order1)
order2 = Order("Steak", 15.00)
orders_db.append(order2)
order3 = Order("Hot dog", 5.00)
orders_db.append(order3)
order4 = Order("Shawarma", 10.00)
orders_db.append(order4)
order5 = Order("Flies", 9.00)
orders_db.append(order5)
