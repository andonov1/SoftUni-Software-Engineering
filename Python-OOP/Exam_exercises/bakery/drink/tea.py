from exams.bakery.drink.drink import Drink


class Tea(Drink):

    def __init__(self, name, portion, brand):
        super().__init__(name, portion, 2.50, brand)
