import datetime
import time
import main

class Terminal:

    def __init__(self, bar, pep, sea):
        self.menu = [bar, pep, sea]
        self.order = []
        self.flag = False   # флаг, который позволяет узнать открыта
                            # или закрыта касса
        self.cash = 0
        self.card_payment = 0
        self.openTerminal = None
        self.closeTerminal = None

    def print_menu(self):
        pr = "руб."
        print("*" * (25 * 3 + 5))
        print(f"{self.menu[0].title:*^25}  {self.menu[1].title:*^25}  {self.menu[2].title:*^25}*")
        print("*" * (25 * 3 + 5))
        for i in range(len(self.menu[0].filling) - 1):
            print(f"{self.menu[0].filling[i]: <25}  {self.menu[1].filling[i]: <25}  {self.menu[2].filling[i]: <25}*")
        print(f"{str(self.menu[0].price) + pr:^25}  {str(self.menu[1].price) + pr:^25}  {str(self.menu[2].price) + pr:^25}*")
        print("*" * (25 * 3 + 5))

    def __str__(self):
        txt = f"ДОБРО ПОЖАЛОВАТЬ В НАШУ ПИЦЦЕРИЮ!"
        txt1 = f"предлагаем на выбор наши пиццы:"
        return f"{txt: ^100}\n{txt1: ^100}"

    # функция открывает терминал
    def open(self):
        self.openTerminal = datetime.datetime.now()
        return self.flag

    # функция закрывает теминал
    def close(self):
        self.closeTerminal = datetime.datetime.now()
        return self.flag

    # принять оплату
    def give_money(self, zak):

        print("сумма вашего заказа: ", zak.summa(self.menu[0], self.menu[1], self.menu[2]))
        choice = input("оплата: \n1 - наличными\n"
                  "2 - картой\n")
        if choice == "1":

            nal = 0
            while nal < zak.summa(self.menu[0], self.menu[1], self.menu[2]):
                n = int(input("введите сумму, которою вносите: "))
                nal += n
                if nal >= zak.summa(self.menu[0], self.menu[1], self.menu[2]):
                    print("Ваша сдача: ", nal - zak.summa(self.menu[0], self.menu[1], self.menu[2]))
                else:
                    print("внесите ещё ", zak.summa(self.menu[0], self.menu[1], self.menu[2]) - nal)

            self.cash += zak.summa(self.menu[0], self.menu[1], self.menu[2])

        if choice == "2":
            main.scroll()
            print("приложите карту к терминалу")
            time.sleep(1)
            input("чтобы приложить карту, нажмите Enter..")
            main.scroll()
            print("идёт запрос в банк...")
            time.sleep(1.5)
            main.scroll()
            print("успешно!")
            time.sleep(1.5)
            main.scroll()
            self.card_payment += zak.summa(self.menu[0], self.menu[1], self.menu[2])

    # печать чека
    def print_check(self, zak, seller):
        print("Печатается чек..")
        time.sleep(2)
        main.scroll()

        print("*" * 40)
        print("Кассир: ", seller.FIO)
        print("Чек открыт: ", self.openTerminal)
        print("Ваш заказ:")
        for i in range(len(zak.list_pizza)):
            if zak.list_pizza[i].title == "БАРБЕКЮ":
                print(zak.list_pizza[i].title, "\t\t * ", zak.bar_count, " = ",
                      zak.list_pizza[i].price * zak.bar_count)

            elif zak.list_pizza[i].title == "ПЕППЕРОНИ":
                print(zak.list_pizza[i].title, "\t\t * ", zak.pep_count, " = ",
                      zak.list_pizza[i].price * zak.pep_count)

            elif zak.list_pizza[i].title == "ДАРЫ МОРЯ":
                print(zak.list_pizza[i].title, "\t\t * ", zak.sea_count, " = ",
                      zak.list_pizza[i].price * zak.sea_count)


        print("\tИтого: ", zak.summa(self.menu[0], self.menu[1], self.menu[2]))
        print("Чек закрыт: ", self.closeTerminal)
        print("*" * 40)
        input("\n\n\nНажмите Enter, чтобы взять чек и отправить заказ на кухню..")
        main.scroll()

