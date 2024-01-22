class Pastry:
    def __init__(self, name, price):
        self.pastry_name = name
        self.pastry_price = price

    def name(self):
        return self.pastry_name

    def price(self):
        return self.pastry_price


class Cupcake(Pastry):
    def __init__(self):
        super().__init__('cupcake', 1)

class Cookie(Pastry):
    def __init__(self):
        super().__init__('cookie', 2)

class Pain_au_chocolat(Pastry):
    def __init__(self):
        super().__init__('pain au chocolat', 3)

class Topping(Pastry):
    def __init__(self,pastry,price,topping):
        self.pastry = pastry
        self.pastry_name = None
        self.pricing = price
        self.topping = topping

    def name(self):
        conjunction = 'and' if self.pastry.pastry_name is None else 'with'
        return f'{self.pastry.name()} {conjunction} {self.topping}'

    def price(self):
        return self.pastry.price() + self.pricing

class Chocolate(Topping):
    def __init__(self,pastry):
        super().__init__(pastry, 0.1,'chocolate')

class Nuts(Topping):
    def __init__(self,pastry):
        super().__init__(pastry, 0.2,'nuts')

class Sugar(Topping):
    def __init__(self,pastry):
        super().__init__(pastry, 0.3,'sugar')
