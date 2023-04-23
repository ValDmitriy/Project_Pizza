from datetime import datetime

import Pizza, Terminal, Zakaz, Seller
import time

# функция для прокрутки консоли
def scroll():
    print("\n" * 15)

# функция для ввода пароля кассы
def enter_password():
    password = ""
    while password != "1234":
        password = input("введите пароль: ")
        if password == "1234":
            print("вы успешно ввели пароль!")
            term.flag = True
            time.sleep(1)
        else:
            password = input("введите пароль: ")


if __name__ == "__main__":

    # создаём объекты для пицц
    bar = Pizza.Barbecue()
    pep = Pizza.Pepperoni()
    sea = Pizza.Seafood()

    # открываем терминал
    term = Terminal.Terminal(bar, pep, sea)

    # регистрируется кассир
    seller = Seller.Seller(input("Введите имя кассира: "))
    n = int(input("введите длительность рабочей смены кассира в минутах: "))
    enter_password()

    # фиксируем время открытия кассы
    time_of_work = n * 60    # рабочая смена кассира в сек

    print("общая длительность смены: ", time_of_work)

    # стартовое время смены кассира
    start = seller.timeOpen()

    ##########################################
    # АЛГОРИТМ ПЕРЕВОДА ФОРМАТА ВРЕМЕНИ В ДЕСЯТИЧНОЕ ПРЕДСТАВЛЕНИЕ

    # t1 = datetime.now()
    # t11 = t1.timetuple()
    # time.sleep(1)
    # t2 = datetime.now()
    # t22 = t2.timetuple()
    #
    # print(time.mktime(t22) - time.mktime(t11))
    ############################################

    listOfZakaz = []            # список заказов
    i = 0                       # счётчик заказов

    # списки готовых  и не готовых заказов
    listReady = []
    listNotReady = []
    # здесь цикл продолжается пока не закончилась смена кассира
    while (time.mktime(datetime.now().timetuple()) - time.mktime(start.timetuple())) <= time_of_work:
        #очищаем списки готовых не готовых заказов
        listReady.clear()
        listNotReady.clear()

        # печатаем приветствие и меню
        scroll()
        print(f"{term.__str__():^50}")
        print("\n" * 5)
        time.sleep(5)
        scroll()
        term.print_menu()

        try:
            time_block = 4  # время, по истечению которого касса блокируется
            time_start_block = datetime.now()

            n = int(input("Хотите сделать заказ: "
                          "\n\t1 - да"
                          "\n\t0 - нет\n"))

            # проверяем прошло ли время для блокировки кассы
            if (time.mktime(datetime.now().timetuple()) - time.mktime(time_start_block.timetuple())) >= time_block:
                term.flag = False

            if term.flag == True:   # проверяем заблокирована ли касса
                scroll()
                # открываем терминал для заказа пицц и фиксируем время открытия
                if n == 1:
                    # создаём время открытия чека
                    term.open()
                    print(term.openTerminal, "статус открытия кассы: ", term.flag)
                    zak = Zakaz.Zakaz()
                    listOfZakaz.append(zak)      # создаём новый заказ

                    # добавляем в заказ пиццу
                    listOfZakaz[i].add_pizza(bar, pep, sea)


                    scroll()
                    # оплата заказа
                    term.give_money(listOfZakaz[i])

                    # Создаём время закрытия чека
                    term.close()

                    # печатаем чек для гостя
                    term.print_check(listOfZakaz[i], seller)

                    scroll()
                    # выводим все заказы и время, которое осталось до приготовления заказа
                    for j in range(len(listOfZakaz) - 1):
                        if (listOfZakaz[j].order_cooking_time - (time.mktime(datetime.now().timetuple()) - time.mktime(
                                listOfZakaz[j].order.timetuple()))) > 0:
                            str = f"{listOfZakaz[j].number_zakaz} - {listOfZakaz[j].order_cooking_time - (time.mktime(datetime.now().timetuple()) - time.mktime(listOfZakaz[j].order.timetuple()))}\t"
                            listNotReady.append(str)
                        elif listOfZakaz[j].order_status == 0:
                            str = f"{listOfZakaz[j].number_zakaz} - ГОТОВ!"
                            listReady.append(str)
                            listOfZakaz[j].order_status = 1

                    # делаем равными количества элементов в списках listReady и listNotReady
                    if len(listReady) > len(listNotReady):
                        a = len(listReady) - len(listNotReady)
                        for k in range(a):
                            listNotReady.append("\t" * 3)
                    else:
                        a = len(listNotReady) - len(listReady)
                        for k in range(a):
                            listReady.append(" ")

                    # выводим готовые и не готовые заказы на экран
                    print("ГОТОВЯТСЯ: \t\t", "ГОТОВЫ: ")
                    for k in range(len(listReady)):
                        print(listNotReady[k] + "\t" + listReady[k])
                    time.sleep(5)

                    # отправляем заказ на кухню(в этом методе фиксируем время отправки)
                    listOfZakaz[i].perform()
                    i += 1      # переходим к следующему заказу
                else:
                    print("Всего Доброго! Ждем Вас в следующий раз!")
                    time.sleep(1)
                    scroll()

            else:
                enter_password()

        except ValueError:
            print('Ввод некорректен. Попытайтесь ввести снова')
            input("Нажмите Enter..")

    else:
        print("К сожалению наша пиццерия закрывается.. Ждём вас завтра!")

    scroll()
    # устанавливаем время закрытия
    seller.timeClose()
    # печать чека закрытия
    seller.print_check(bar, pep, sea, term)
input()