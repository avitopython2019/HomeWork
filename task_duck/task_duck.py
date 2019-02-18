import random

def barmen_func(intox, money):
    print("Что будем пить?\
        \n\t 1 - Вискарик\
        \n\t 2 - Пиво\
        \n\t 3 - Воду")
    num_choice = int(input())
    if num_choice == 1:
        if can_buy (money, drinks_dict["виски"]["цена"]):
            print("Бармен наливает Вискарик. Утенок становится пьянее")
            intox += drinks_dict["виски"]["опьянение"]
            money -= drinks_dict["виски"]["цена"]
        else:
            print("Ууу, Это не покарману")
    elif num_choice == 2:
        if can_buy (money, drinks_dict["виски"]["цена"]):
            print("Бармен наливает Пиво. Утенок становится пьянее")
            intox += drinks_dict["пиво"]["опьянение"]
            money -= drinks_dict["пиво"]["цена"]
        else:
            print("Ууу, Это не покарману")
    elif num_choice == 3:
        if can_buy (money, drinks_dict["виски"]["цена"]):
            print("Бармен смотрит на вас подозрительно. Утенок уталяет жажду")
            intox += drinks_dict["вода"]["опьянение"]
            money -= drinks_dict["вода"]["цена"]
        else:
            print("Ууу, Это не покарману")
    print ("Текущие деньги: ", money)
    return intox, money

def sum_2_card(pack):
    card1 = pack.pop()
    card2 = pack.pop()
    if (card1 == card2) == 11:
        return 21
    return card1 + card2

def is_drunk(intox):
    if intox >= 100:
        print("Утёнок напился!")
        return True
    return False

def can_buy(money, cost):
    if money - cost > 0:
        return True
    print("Утёнок не может себе это позволить!")
    return False

def jackal_func(intox, money):
    game = False
    money_before = money
    print("За столом сидят Бурый и Рыжий шакал.\
        \nОни сразу предлогают сыграть в 21, ставка 30 у.е.\
        \nИграем с ними? Да/Нет")
    bet_score = 30
    if input() in ["Да", "да", "Yes", "yes", "Д", "д", "Y", "y"]:
        game = True
    while game:
        if not can_buy(money, bet_score):
            print("Ну что пустые карманы да? Беги отсюда")
            break
        money -= bet_score
        print("Может что-то выпить?")
        if input() in ["Да", "да", "Yes", "yes", "Д", "д", "Y", "y"]:
            intox, money = barmen_func(intox, money)
            if is_drunk(intox):
                return intox, money
        pack = [6,7,8,9,10,2,3,4,11] * 4
        print("Бурый мешает колоду и сдает карту")
        score_dict = {"Бурый": 0, "Рыжий": 0, "Утёнок": 0}
        random.shuffle(pack)
        score_dict["Утёнок"] = sum_2_card(pack)
        print("Cумма ", score_dict["Утёнок"], " Ещё карту?")
        yet_card = input() in ["Да", "да", "Yes", "yes", "Д", "д", "Y", "y"]
        while yet_card:
            current = pack.pop()
            print("Карта %d" %current)
            score_dict["Утёнок"] += current
            print("Очки: ", score_dict["Утёнок"])
            if score_dict["Утёнок"] > 21:
                break
            print("Ещё карту?")
            yet_card = input() in ["Да", "да", "Yes", "yes", "Д", "д", "Y", "y"]
        print("Бурый сдаёт карты Рыжему и себе")
        score_dict["Бурый"] = sum_2_card(pack)
        score_dict["Рыжий"] = sum_2_card(pack)
        while score_dict["Бурый"] < 19:
            score_dict["Бурый"] += pack.pop()
        while score_dict["Рыжий"] < 19:
            score_dict["Рыжий"] += pack.pop()
        print("Бурый ухмыльнулся и сказал:\"Вскрываемся:\"")
        max_score = 0
        for k in score_dict:
            print(k, score_dict[k])
            if (score_dict[k] <= 21) and (max_score < score_dict[k]):
                max_score = score_dict[k]

        final_dict =  {k : v for k, v in score_dict.items() if v == max_score}
        num_winers = len(final_dict)
        if num_winers != 0:
            for k  in final_dict:
                print("Победил", k,final_dict[k])
            if final_dict.get("Утёнок") != None:
                print("Утёнку сегодня везет + ", (bet_score*3)//num_winers, "у.е.")
                money += (bet_score*3)//num_winers
                print("Текущие финансы: ", money)
            else:
                print("Утёнок програл")
        print("Шакалы переглядываются и предлогают ещё партейку")
        if not input() in ["Да", "да", "Yes", "yes", "Д", "д", "Y", "y"]:
            game = False
    if money > money_before:
        print("Шакалы начинают скалиться, но разрешают Утёнку выйти из-за стола")
    else :
        print("Шакалы уговаривают Утёнка сыграть ещё, но он встаёт")
    return intox, money
drinks_dict = { "виски": {"цена": 20, "опьянение": 40}, "пиво": {"цена": 15, "опьянение": 25}, "вода": {"цена": 10, "опьянение": 0}}

intoxication = 0
money = 100
play = False
print("Приветсвуем, вы запустили игру про уточку!")
print("Играем? Введите Да/Нет\n")

if input() in ["Да", "да", "Yes", "yes", "Д", "д", "Y", "y"]:
    play = True
    print("\nВы Утёнок, который идёт в бар после тяжёлой рабочей недели.\
        \nУ вас с собой 100 у.е. \
        \nЗаходя внутрь вы оглядывается, чтобы найти место куда сесть:")
while play:
    print("\t1 - Свободное место у барной стойки\
        \n\t2 - Присоединиться за столик к Шакалам\
        \n\t3 - Домой\
        \n\nКуда сядете?")
    num_place = int(input())
    if num_place == 1:
        drink = True
        while drink:
            intoxication, money = barmen_func(intoxication, money)
            if intoxication > 100:
                break
            print("Ещё выпить?")
            if input() not in ["Да", "да", "Yes", "yes", "Д", "д", "Y", "y"]:
                drink = False
    elif num_place == 2:
        intoxication, money = jackal_func(intoxication, money)
        if intoxication > 100:
            break
    else:
        print("Ну домой так домой")
        play = False
print("Конец игры. До встречи!")

