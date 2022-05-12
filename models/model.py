#Creating models for the foodapp database

class Menu:

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 0: # less than zero
            ValueError("Price must be equal to price on the order")
        self._price = price


menus_db = []
menu1 = Menu("Rice", 12.00)
menus_db.append(menu1)
menu2 = Menu("Steak", 15.00)
menus_db.append(menu2)
menu3 = Menu("Hot dog", 5.00)
menus_db.append(menu3)
menu4 = Menu("Shawarma", 10.00)
menus_db.append(menu4)
menu5 = Menu("Flies", 9.00)
menus_db.append(menu5)

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

user_db = []
user1 = User("jones", "asdf")
user_db.append(user1.__dict__)
user2 = User("mike", "asdf")
user_db.append(user2.__dict__)
user3 = User("tim", "asdf")
user_db.append(user3.__dict__)


