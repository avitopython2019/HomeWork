
def step1():
    print(
        'Утка - маляр решила выпить зайти в бар. '
        'Взять ей зонтик?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


def step2_umbrella():
    print(
        'Утка вышла из дома, но дождя нету. '
        'Выкинуть ей зонт или нет?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_without_umbrella()
    return step3_with_umbrella()


def step2_no_umbrella():
    print(
        'Утка вышла из дома и захотела полететь в космос. '
        'Полететь ей в космос или нет?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step3_to_space()
    return step3_no_space()


def step3_with_umbrella():
    print(
        'Утка не стала выбрасывать зонтик и дошла до бара. '
        'Взять ей B-52 или нет?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step4_b52()
    return step4_without_b52()


def step3_without_umbrella():
    print(
        'Утка выбросила зонт. За это её арестовала полиция. '
        'Вы в тюрьме, поздравляю!'
    )


def step3_to_space():
    print(
        'Утка полетела в космос, но забыла надеть скафандр при выходе в открытый космос. '
        'Вы умерли, поздравляю!'
    )


def step3_no_space():
    print(
        'Утка не захотела лететь в космос, но пока о нем думала упала в канаву и разбилась. '
        'Вы умерли, поздравляю!'
    )


def step4_b52():
    print(
        'Утка взяла B-52, но в неё случайно попал мышьяк. '
        'Вы умерли, поздравляю!'
    )


def step4_without_b52():
    print(
        'Утка решила не пить и просто послушать хорошую музыку. '
        'Идти ей домой?'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        print('Выберите: {}/{}'.format(*options))
        option = input()

    if options[option]:
        return step5_home()
    return step5_bar()


def step5_bar():
    print(
        'Утка решила остаться в баре. Пока она слушала музыку на бар упала ракета, на которой она не захотела лететь. '
        'Вы умерли, поздравляю!'
    )


def step5_home():
    print(
        'Утка решила решила пойти домой. По дороге пошел дождь и она использовала зонтик. Придя домой она заснула '
        'очень крепким сном...'
    )


if __name__ == '__main__':
    step1()
