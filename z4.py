print('Программа для вывода всех чётных положительных чисел')
n = int(input('Введите любое положительное число: '))
evens = []
for num in range(n):
    if num%2 == 0:
        evens.append(num)

print(evens)

