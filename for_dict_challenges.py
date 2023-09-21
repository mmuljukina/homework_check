# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]

dict_stud={} # для заполнения посчитанными студентами 

for il in range(len(students)):                              # внешний цикл по списку
    cnt_s = 1
    for key_ext, val_ext in students[il].items():            # анализируем словарь
        iwh = il + 1
    while iwh <= len(students)-1:                            # цикл по списку дальше для поиска дубликатов значений из словаря
        for key_in, val_in in students[iwh].items():
            if val_ext == val_in:
                cnt_s = cnt_s + 1
        iwh = iwh + 1 

    # Производим анализ есть ли, уже ключ-Имя в посчитанном словаре, если нет, то заполняем словарь
    if dict_stud.get(val_ext) == None: dict_stud[val_ext] = cnt_s

    # Выводим полученный словарь на печать
for key, val in dict_stud.items(): 
    print(key,':' , val)   



# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]

cnt_max = 0      # для получения максимального повторения имен 
name_s_max = ''  # для получения частого имени

for il in range(len(students)):                              # внешний цикл по списку
    cnt_s = 1
    for key_ext, val_ext in students[il].items():            # анализируем словарь
        iwh = il + 1
    while iwh <= len(students)-1:                            # цикл по списку дальше для поиска дубликатов значений из словаря
        for key_in, val_in in students[iwh].items():
            if val_ext == val_in:
                cnt_s = cnt_s + 1
        iwh = iwh + 1 

    # Анализирум максимально встречаемые имена
    if cnt_max <= cnt_s: 
        cnt_max = cnt_s
        name_s_max = val_ext

    # Выводим результат
print(name_s_max)


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]

dict_stud = {}  # для сбора данных по каждому классу

for il in school_students:                              # внешний цикл по списку
    dict_stud = {}                                      
    for il_in in il:                                    # внутренний цикл по списку
        if dict_stud.get(il_in['first_name']) == None:  # сразу решила обратиться к ключу, получить значение и проверить новый словарь
            dict_stud[il_in['first_name']] = 1
        else:
            dict_stud[il_in['first_name']] = dict_stud[il_in['first_name']] + 1
    
    name_s_max = ''                                      # анализируем частое имя
    cnt_max = 0
    for key, val in dict_stud.items(): 
        if cnt_max <= val: 
           cnt_max = val
           name_s_max = key
                                                          # Выводим результат   
    print(f'Самое частое имя в классе {school_students.index(il) + 1}: {name_s_max}')
       



# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2в', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

# Циклы циклы циклы:)
for ish in school:
    wrdcls = ''
    cnt_mle = 0
    cnt_fmle = 0
    for key_sh, val_sh in ish.items():
        if key_sh == 'class':
            wrdcls = val_sh
        if  key_sh == 'students':
            for spk in val_sh:
                for key_st, val_st in spk.items():
                    for key_sml, val_sml in is_male.items():
                        if key_sml == val_st and val_sml == True:
                            cnt_mle = cnt_mle + 1
                        if key_sml == val_st and val_sml == False:
                            cnt_fmle = cnt_fmle + 1
    print(f'Класс {wrdcls}: девочки {cnt_fmle}, мальчики {cnt_mle}')                        


            


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '3c', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
]
is_male = {
    'Маша': False,
    'Оля': False,
    'Олег': True,
    'Миша': True,
}

dict_sch = {}

# Подправим код от предыдущего:)
for ish in school:
    wrdcls = ''
    cnt_mle = 0
    cnt_fmle = 0
    for key_sh, val_sh in ish.items():
        if key_sh == 'class':
            wrdcls = val_sh
        if  key_sh == 'students':
            for spk in val_sh:
                for key_st, val_st in spk.items():
                    for key_sml, val_sml in is_male.items():
                        if key_sml == val_st and val_sml == True:
                            cnt_mle = cnt_mle + 1
                        if key_sml == val_st and val_sml == False:
                            cnt_fmle = cnt_fmle + 1
    if cnt_mle < cnt_fmle: 
        dict_sch[f'Больше всего девочек в классе {wrdcls}'] = cnt_fmle
    else:
        dict_sch[f'Больше всего мальчиков в классе {wrdcls}'] = cnt_mle
                         
for key_p, val_p in dict_sch.items(): print(key_p, val_p)        

