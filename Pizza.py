class Pizza:
    def __init__(self):
        self.title = ''
        self.dough = ''
        self.sauce = ''
        self.filling = []
        self.price = int



    def time(self):
        cooking_time = 0
        return cooking_time


class Barbecue(Pizza):
    def __init__(self):
        super().__init__()
        self.title = 'БАРБЕКЮ'
        self.dough = 'Дрожжевое, толстое'
        self.sauce = 'Барбекю'
        self.filling = ['соус острый томатный', 'Колбаса Чоризо', 'колбаски охотничьи', 'бекон', 'курица копченая',
                        'зелень', 'сыр моцарелла', 'масло чесночное']

        self.price = 200
        self.count = 0

    def time(self, cooking_time=30):
        return cooking_time

    def __str__(self):
        return f"{self.title}\n{self.filling}\n" + "\t" * 5 + f"{self.price}руб."

class Pepperoni(Pizza):
    def __init__(self):
        super().__init__()
        self.title = 'ПЕППЕРОНИ'
        self.dough = 'Дрожжевое, тонкое'
        self.sauce = 'Острый томатный'
        self.filling = ['соус острый томатный', 'пепперони', 'сыр моцарелла', 'базилик', 'орегано', 'красный перец',
                        'помидоры']
        self.price = 170
        self.count = 0


    def time(self, cooking_time=20):
        return cooking_time

    def __str__(self):
        return f"{self.title}\n{self.filling}\n" + "\t" * 5 + f"{self.price}руб."


class Seafood(Pizza):
    def __init__(self):
        super().__init__()
        self.title = 'ДАРЫ МОРЯ'
        self.dough = 'Дрожжевое, тонкое'
        self.sauce = 'Чесночный соус'
        self.filling = ['чесночный соус', 'сыр моцарелла', 'семга', 'креветки', 'мидии', 'маслины', 'сыр фета',
                        'красный лук', ]
        self.price = 150
        self.count = 0


    def time(self, cooking_time=40):
        return cooking_time

    def __str__(self):
        return f"{self.title}\n{self.filling}\n" + "\t" * 5 + f"{self.price}руб."
