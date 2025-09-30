from random import *

print('Welcome to Guessing Game!', "It's a good day to play", sep='\n')

n = randint(1, 100)

def is_valid(num):
    return True if num.strip().isdigit() else False


while True:
    num = input('Введите число: ')
    point = 0 #Number of attempts
    while True:
        if is_valid(num):
            num = int(num)
        else:
            print('', 'Упс, кажется это не число :)', sep='\n')
            num = input('Введите число: ')
            continue

        if num < n:
            print('Ваше число меньше  загаданного, попробуйте еще разок', end=' ')
            num = input()
        elif num > n:
            print('Ваше число больше загаданного, попробуйте еще разок', end=' ')
            num = input()
        else:
            print('Вы угадали, поздравляем!')
            print(f'Количество попыток: {point}')
            break
    print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
    print('Не желаете сыграть еще?')
    otv = input()
    if otv.lower() == 'да':
        print('Хотите изменить максимально возможное значение?')
        otv2 = input()
        if otv2.lower() == 'да':
            print('Введите максимально возможное значение', end=' ')
            maxn = int(input())
        continue
    else:
        break
