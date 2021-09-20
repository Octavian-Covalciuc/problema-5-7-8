def prob_5():
    print('PROBLEMA 5')
    x = [1,2,3,4,5]
    y = x.copy()
    sumx = 0
    prodx = 1
    for i in range(3):
        sumx += x[i]
    print(f'Suma primelor 3 elemente din x este {sumx}')
    print('Suma elementelor din y este', sum(y))
    for i in x:
        prodx *= i
    print(f'Produsul elementelor din x este {prodx}')
    print('Valoarea absoluta a elementului 3 din y este', abs(y[2]))
    print('Suma primelor cifre din fiecare vector este', x[0] + y[0])

def prob_7():
    print('PROBLEMA 7')
    v = {'Luni': 1, 'Marti': 2, 'Miercuri': 3, 'Joi': 4, 'Vineri': 5, 'Sambata': 6, 'Duminica': 7}
    lst = v.values()
    print('Venitul saptamanal al saptaminii este ', sum(lst))
    print('Venitul zilnic este ', sum(lst) / 7)
    for key, value in v.items():
        if value == max(lst):
            print(f'Venitul cel mai mare este {key}')
        elif value == min(lst):
            print(f'Venitul cel mai mic este {key}')

def prob_8():
    print('PROBLEMA 8')
    temp = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,\
            '9': 9, '10': 10, '11': 11, '12': 12, '13': 13, '14': 14, '15': 15, '16': 16, '17': 17,\
            '18': 18, '19': 19, '20': 20, '21': 21, '22': 22, '23': 23, '24': 24, '25': 25,}
    lst = temp.values()
    print('Temperatura medie este', sum(lst) / 24)
    for key, value in temp.items():
        if value == max(lst):
            print(f'Temperatura cea mai mare, {value}, este la ora {key}')
        elif value == min(lst):
            print(f'Temperatura cea mai mica, {value}, este la ora {key}')
prob_5()
prob_7()
prob_8()