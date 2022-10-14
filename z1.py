print('Программа для вывода дня недели по его номеру')
def week_name(week_num):
    if 0 < week_num < 8:
        list_week_names = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
        return list_week_names[week_num]
    return 'Неверно указан день недели'

print(week_name(int(input('Введите номер дня недели: '))-1))
