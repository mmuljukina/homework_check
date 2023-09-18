# Задание 1
# Необходимо вывести имена всех учеников из списка с новой строки

names = ['Оля', 'Петя', 'Вася', 'Маша']

# Цикл по списку
for i in names:
    print(i)   



# Задание 2
# Необходимо вывести имена всех учеников из списка, рядом с именем показать количество букв в нём
# Пример вывода:
# Оля: 3
# Петя: 4

names = ['Оля', 'Петя', 'Вася', 'Маша']

#Цикл по списку
for i in names:
    print(i + ':', len(i))



# Задание 3
# Необходимо вывести имена всех учеников из списка, рядом с именем вывести пол ученика

is_male = {
    'Оля': False,  # если False, то пол женский
    'Петя': True,  # если True, то пол мужской
    'Вася': True,
    'Маша': False,
}

names = ['Оля', 'Петя', 'Вася', 'Маша']

#Циклы по списку и словарю
for iext in names:
    for iin in is_male:
        if iext == iin:
            print(iin, is_male[iin])



# Задание 4
# Даны группу учеников. Нужно вывести количество групп и для каждой группы – количество учеников в ней
# Пример вывода:
# Всего 2 группы.
# Группа 1: 2 ученика.
# Группа 2: 4 ученика.

groups = [
    ['Вася', 'Маша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
    ['Оля', 'Петя', 'Гриша'],
]

#Цикл по словарю
for i in groups:
    str_grp = 'Группа '
    char = ':'
    grp_num = groups.index(i) + 1
    cnt_student = len(i)
    if len(i) >= 5:
        str_student = ' учеников.'
    else:
        str_student = ' ученика.'    
    print(f'{str_grp} {grp_num}{char} {cnt_student} {str_student}')



# Задание 5
# Для каждой пары учеников нужно с новой строки перечислить учеников, которые в неё входят
# Пример вывода:
# Группа 1: Вася, Маша
# Группа 2: Оля, Петя, Гриша

groups = [
    ['Вася', 'Маша'],
    ['Оля', 'Петя', 'Гриша'],
    ['Вася', 'Маша', 'Саша', 'Женя'],
]

# Вопросы, так для каждой пары или группы, судя по примеру я бы сказала, что группы, но если нужно все же пары
for i in groups:
    str_grp = 'Группа '
    char = ':'
    grp_num = groups.index(i) + 1    
    cnt_list = ", ".join(i)
    print(f'{str_grp} {grp_num}{char} {cnt_list}')