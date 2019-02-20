#
vibor_name = "Утенок по имени, имени.. как звали утенка?"
vstyplenie = ("Утенок по имени .. возвращался со смены и заметил по дороге небольшое казино 'Оленьи рога'"
    "\nЗаглянем?(да/нет)\n")
vybor_stola = ('выберите стол\n1\n2\n3\n')
obstanovka = ('Зайдя во внутрь,.. видит ')
message_stavka = "лягушка-крупье: '.., делай ставку'"
message_pole = 'Ведите номер поля на которое .. хочет поставить'
#stavka = "делает ставку, в кармане н руб"
vopros = "(да/нет)"
fishki = int(100)
kolvo_stolov = {1, 2, 3}
def ruletka(stavka, pole, fishki):
    nomer = random.randint(0, 100)
    if nomer == pole:
        fishki = fishki + 10*stavka
    else:
        fishki = fishki - stavka
    return fishki
    return nomer
def proverka_bad_enda(fishki):
    if fishki <= 0:
        print ("утенок опять все проиграл и грустный отправляется домой")
        input("конец, нажмите любую клавишу")

    else:
        return
def delaem_stavky ():
    print(message_stavka)
    stavka = int(input())
    while (stavka > fishki or stavka < 0):
        print('утенок еще раз порылся в карманах но ничего не нашел.\n',message_stavka)
        stavka = int(input())
    else:
        print(message_pole)
        pole = int(input())
        while (pole < 0 or pole > 100):
            print("крупье косо смотрит на утенка")
            pole = int(input())
        else:
            return [stavka, pole]
import random
print(vibor_name)
name = input()
vstyplenie = vstyplenie.replace("..", name)
message_pole = message_pole.replace("..", name)
message_stavka = message_stavka.replace("..", name)
print(vstyplenie)
soglasie = input()
while soglasie != "да":
    if soglasie != "нет":
        print("утенок не понял что ему делать..напишите да или нет")
        soglasie = input()
    else:
        print("утенок идет домой..")
        input("конец, нажмите любую клавишу")
        break
else:
    print('Зайдя внутрь утенок замечает первый стол c немного рассохшимся колесом\n'
          'и с уютным местом возле печки, второй стол ничем не примечатален,\n'
          'третий стол стоит возле стены с висящим на ней старым телефоном, на котором\n',
          ' грузно сидит огромный попугай Жако\n'
          ,vybor_stola)
    stol = int(input())
    while stol not in kolvo_stolov:
        print ('чешет репу..', vybor_stola)
        stol = input()
    else:
        if stol == 1:
            print('Едва сев за стол, утенок успел бросить взгляд на немного косое колесо с трещиной,\n',
                  'где только что выиграл номер 9, кажется сегодня утенку должно повезти')
            while fishki > 0:
                stavka, pole = delaem_stavky()
                if pole == 26:
                    print("Шарик останавливается на номере 26, утенок срывает джекпот\n,"
                          "ловя на себе недобрый взгляд местной жабы-вышибалы с занозой в глазу\n"
                          "понимая что сегодня больше лучше не рисковать, радостный утенок\n"
                          "собирается бежать домой с выигранными деньгами, едва сделав пару сделав пару шагов\n"
                          "он слышит резкий хлопок и в глазах у него сразу потемнело..")
                    input("продолжение следует..")
                    break
                fishki = ruletka(stavka, pole, fishki)
                print('колесо остановилось, теперь у утенка ', fishki, 'фишек')
                proverka_bad_enda(fishki)
        elif stol == 2:
            while fishki > 0:
                stavka, pole = delaem_stavky()
                fishki = ruletka(stavka, pole, fishki)
                print('колесо остановилось на ',nomer,', теперь у утенка ',fishki,'фишек')
                proverka_bad_enda(fishki)

        else:
            print('Подойдя к третьему столу, утенок слышит как попугай натужно пытается что-то выговорить\n',
                  ', но в звуках "MNO, MNO" не удается разобрать что-либо членораздельного..')
            while fishki > 0:
                stavka, pole = delaem_stavky()
                if pole == 66:
                    print("Шарик останавливается на номере 66, утенок срывает джекпот\n," 
                          "ловя на себе недобрый взгляд местной жабы-вышибалы с занозой в глазу\n"
                          "понимая что сегодня больше лучше не рисковать, радостный утенок\n"
                          "бежит домой с выигранными деньгами, едва сделав пару сделав пару шагов\n"
                          "он слышит резкий хлопок и в глазах у него сразу потемнело..")
                    input("продолжение следует..")
                    break
                else:
                    fishki = ruletka(stavka, pole, fishki)
                    print('колесо остановилось, теперь у утенка ', fishki, 'фишек')
                    proverka_bad_enda(fishki)




















