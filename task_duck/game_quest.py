##############################################################################
##                          DUCKLING IN PRISON                              ## 
##                          Eliseev Anton 2019                              ##                    
##############################################################################
         
# Cцена №1 Клетка
def prison_cage():
    prison_message = '\n'.join(['\nУтенок просыпается в сырой темнице. Всюду',
    'снуют крысы в поисках еды. Потолок протекает, а холодные капли падают',
    'прямо на клюв. Напротив камеры сидит огромная жаба с грустными глазами',
    '(видимо надсмотрщик) и пристально следит за вами, а также что-то',
    'охраняет в своей тумбочке.\n'])
    print(prison_message)

    
    choosing = True
    while choosing:
        print("\nХотите оглядеться? (да/нет) \n")
        option = input()
        if option.lower().strip() == 'да':
            choosing = False
        else:
            print("\nЗдесь все равно нечем больше заняться.\n")

    prison_dict = {
        '1' : 'wall',
        '2' : 'toad',
        '3' : 'bucket',
        '4' : 'spider',
        }

    prison_message = '\n'.join(['\nОглядевшись утенок заострил внимание на',
    'четырех объектах для взаимодействия: cтена камеры, на которой красуется',
    'огромная трещина; жаба-надсмотрщик, сходящая с ума от скуки;' ,
    'железное ведро, в котором когда-то была вода и пугающих размеров', 
    '(по меркам уток) паук, свивший паутинку в дальнем углу камеры.'
    '\nC чем утенок пойдет взаимодейстовать? \n'])
    print(prison_message)

    exit = False
    bucket_picked = False
    spider_catched = False
    
    prison_messages = ['1. СТЕНА','2. ЖАБА','3. ВЕДРО','4. ПАУК']

    while not exit:
        print("\nДля выбора объекта введите цифру:\n ")
        for prison_message in prison_messages:
            print(prison_message)
        choosing = input("\nВарианты от 1 до 4:\n ")            
        if prison_dict.setdefault(choosing) == 'wall':
            choosing = True
            if bucket_picked == True and spider_catched != True:
                while choosing:
                    print("\nВыглядит хрупко, хотите сломать стену?(да/нет)\n")
                    option = input()
                    if option.lower().strip() == 'да':
                        choosing = False
                        exit = True
                        ending = 'wall_broken'
                        print("\nВы вышли наружу из клетки\n")
                        return ending
                    else:
                        print("\nОтходите, чтобы снова осмотреться\n")
                        choosing = False
            elif spider_catched == True:
                print("\nНекогда думать о стене - жаба идет к утенку\n")
            else:
                print('\nВыглядит хрупко, но ломать надо чем-то\n')

        elif prison_dict[choosing] == 'toad':
            if spider_catched == True:
                print( "\nЖаба просит показать что у вас в ведре\n"
                "\nНедолго думая, утенок поднимает ведро\n"
                "\nДовольная жаба находит свой обед и расплывается\n"
                "в улыбке. Кажется она считает вас другом.\n")
                
                exit = True
                ending = 'toad_fed'
                return ending
            else:
                print("\nЛениво смотрит на тумбу и облизывает свой глаз\n"
                "\nМожет можно ее как-то привлечь?\n")    

        elif prison_dict[choosing] == 'bucket' and bucket_picked == False:           
            bucket_picked = True
            print("\nВедро выглядит большим и вместительным: пригодится\n"
            "\n*Подобрал ведро*\n")
            prison_messages.remove('3. ВЕДРО')             

        elif prison_dict[choosing] == 'spider' and spider_catched == False:
            if bucket_picked == True:
                spider_catched = True
                print("\nКажется ведро достаточно большое, чтобы поймать его"
                "\n*Вы поймали стремного паука в ведро*\n"
                "\nИз-за шума в камере на ваc обратила внимание жаба\n")
                prison_messages.remove('4. ПАУК')                            
            else:
                print("\nПаук выглядит стремно, приближаться не хочется\n")
        else:
            exit = False
    prison_messages.clear()
    prison_dict.clear()
       
#Cцена №2 Тюрьма 
def prison_escape(prison_cage):

    prison_dict = {
        '1' : 'stone',
        '2' : 'exit',
        }

    prison_messages = ['1. ВЗЯТЬ КАМЕНЬ','2. БЕЖАТЬ']

    if prison_cage == 'toad_fed':
        prison_message = '\n'.join(['\nЖаба открывает клетку, после чего',
        'дает ключ от нее утенку. Они долгое время беседуют и играют в шашки.',
        'Скоро они подружились и пошли заниматься тимбилдингом в бар!\n'])        
        print(prison_message)
        ending = 'good'
        return ending        
    elif prison_cage == 'wall_broken':
        prison_message = '\n'.join(['\nЖаба смотрит на вас с агрессией и ',
        'собирается напасть. Утенок видит под собой камень, а так же замечает',
        'что выход не так уж и далеко и он может попробовать сбежать!\n'])        
        print(prison_message)

        print("\nДля выбора действия введите цифру:\n ")
        for prison_message in prison_messages:
            print(prison_message)
        choosing = input("\nВарианты от 1 до 2:\n ")

        if prison_dict.setdefault(choosing) == 'stone':
            prison_message = '\n'.join(['\nПодобрав камень,утенок швыряет его',
            'прямо в голову жабе и вырубает ее. Обыскав ее он находит ключ от',
            'тумбочки. Отперев тумбочку он забирает ключ от своей камеры на',
            'память. И сбегает из тюрьмы\n'])        
            print(prison_message)

        elif prison_dict[choosing] == 'exit':
            prison_message = '\n'.join(['\nПеребирая своими утиными лапками',
            'герой почти добежал до выхода, но жаба зацепила его языком.',
            'Утенку приходит в голову гениальная идея привязать жабу языком к',
            'решетке. С большим трудом он справляется и бежит из тюрьмы без',
            'оглядки.\n'])        
            print(prison_message)
        ending = 'bad'
        return ending

    prison_messages.clear()
    prison_dict.clear() 
#Опредление концовки        
def end_of_game(prison_escape):
    if prison_escape == 'good':
        print("Конец игры!\nХорошая концовка")
    elif prison_escape == 'bad':
        print("Конец игры!\nПлохая концовка")

#Приветственный экран
hello = '\n'.join(['\nВы утенок, которого злая жаба посадила в тюрьму с целью', 
'плотно пообедать и сэкономить на KFC. Ваша задача освободиться и отомстить',
'обидчику!\n'])
print(hello)
# основная часть программы
choosing = True
while choosing:
    print("\nХотите начать игру? (да/нет) \n")
    option = input()
    if option.lower().strip() == 'да':
        choosing = False
        end_of_game(prison_escape(prison_cage()))
    else:
        break
print("Cпасибо за игру!")