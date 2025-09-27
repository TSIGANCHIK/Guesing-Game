from random import *
#test
while True:
  maxn = 100
  n = randint(1, maxn)
  print('Добро пожаловать в числовую угадайку')
  def is_valid(num):
    if num.isalpha():
        return False
    if 100 >= int(num) >= 1 and str(num).isdigit():
        return True
    else: 
        return False
  print('Введите число:', end= ' ')
  num = input()
  point = 0
  while True:
    point += 1
    if is_valid(num):
      num = int(num)
    else:
      print('А может быть все-таки введем целое число от 1 до 100?', end= ' ')
      num = input()
      continue
    if num < n:
      print('Ваше число меньше  загаданного, попробуйте еще разок', end= ' ')
      num = input()
    elif num > n:
      print('Ваше число больше загаданного, попробуйте еще разок', end= ' ')
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
      print('Введите максимально возможное значение', end= ' ')
      maxn = int(input())
    continue
  else:
    break
