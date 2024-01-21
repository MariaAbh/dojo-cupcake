class Cupcake:
    # def __init__(self):
    #     pass
    def name(self):
        return 'cupcake'

    def price(self):
        return 1

class Cookie:
    def name(self):
        return 'cookie'

    def price(self):
        return 2

class Pain_au_chocolat:
    def name(self):
        return 'pain au chocolat'

class Topping:
    def __init__(self,pastry):
        self.pastry = pastry

    def name(self):
        base = self.pastry.name()
        if 'with' in base:
            return base + ' and ' + self.topping
        else:
            return base + ' with ' + self.topping

    def price(self):
        return self.pastry.price() + self.pricing

class Chocolate(Topping):
    def __init__(self,pastry):
        super().__init__(pastry)
        self.pricing = 0.1
        self.topping = 'chocolate'

class Nuts(Topping):
    def __init__(self,pastry):
        super().__init__(pastry)
        self.pricing = 0.2
        self.topping = 'nuts'

class Sugar(Topping):
    def __init__(self,pastry):
        super().__init__(pastry)
        self.pricing = 0.3
        self.topping = 'sugar'
