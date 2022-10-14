import math


print('Программа выводит возможный диапазон значений в 4х четвертях на графике.')
match int(input('Введите номер четверти графика: ')): 
    case 1:
        print('x > 0, y > 0')
    case 2:
        print('x < 0, y > 0')
    case 3:
        print('x < 0, y < 0')
    case 4:
        print('x > 0, y < 0')
    case _:
        print('Неверно указана четверть') 
