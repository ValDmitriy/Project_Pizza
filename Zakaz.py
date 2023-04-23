import datetime
import time


class Zakaz:

    number_zakaz = 1        # номер заказа

    def __init__(self):
        self.list_pizza = []
        self.bar_count = 0
        self.pep_count = 0
        self.sea_count = 0
        self.number_zakaz = Zakaz.number_zakaz  # присваиваем объекту порядковый номер
        self.order = datetime.datetime.now()
        self.order_cooking_time = 0  # общее время на приготовление заказа
        self.order_status = 0  # статус готовности заказа (0 - не готов, 1 - готов)

    def add_pizza(self, bar, pep, sea):

        try:
            Zakaz.number_zakaz += 1 # увеличиваем номер заказа для следующего заказа
            n = int(input("выберите пиццу: \n\t1. пицца Барбекю "
                          "2. пицца Пепперони "
                          "3. пицца Дары Моря "
                          "\n\t0. закончить заказ\n"))
            while n != 0:
                # добавляем в заказ пиццу
                if n == 1:
                    if bar not in self.list_pizza:
                        self.list_pizza.append(bar)
                    self.bar_count += 1
                    self.order_cooking_time += bar.time()
                    bar.count += 1

                elif n == 2:
                    if pep not in self.list_pizza:
                        self.list_pizza.append(pep)
                    self.pep_count += 1
                    self.order_cooking_time += pep.time()
                    pep.count += 1

                elif n == 3:
                    if sea not in self.list_pizza:
                        self.list_pizza.append(sea)
                    self.sea_count += 1
                    self.order_cooking_time += sea.time()
                    sea.count += 1

                else:
                    print("Такой позиции в меню нет! ")

                n = int(input("выберите пиццу: \n\t1. пицца Барбекю "
                              "2. пицца Пепперони "
                              "3. пицца Дары Моря "
                              "\n\t0. закончить заказ\n\t"))

        except ValueError:
            print('Номер пиццы введен некорректно. Заказ завершен.')

    # сумма заказа
    def summa(self, bar, pep, sea):
        sum = 0
        for i in self.list_pizza:
            if i == bar:
                sum += self.bar_count * bar.price
            elif i == pep:
                sum += self.pep_count * pep.price
            elif i == sea:
                sum += self.sea_count * sea.price
        return sum

    def perform(self):
        time.sleep(2)
        print("Ваш заказ отправляется на кухню...")
        go_to_kitchen = datetime.datetime.now()
        print(go_to_kitchen)

        local_time = 3
        while local_time:
            m, s = divmod(local_time, 60)
            min_sec_format = '{:02d}:{:02d}'.format(m, s)
            print(min_sec_format, end='\n')
            time.sleep(1)
            local_time -= 1
        print("Заказ отправлен. Ожидайте...")
        print("Время приготовления заказа: ", self.order_cooking_time, "секунд")
        time.sleep(3.5)
