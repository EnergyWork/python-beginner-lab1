def task1(method):
    """
        #1 Пять способов поменять значения переменных местами
    """
    x = int(input('Введите первое число: '))
    y = int(input('Введите второе число: '))

    if method == 1: # способ 1
        tmp = x
        x = y
        y = tmp
    elif method == 2: # способ 2
        x, y = y, x
    elif method == 3: # способ 3
        x = x + y
        y = x - y
        y = x - y
    elif method == 4: # способ 4
        x = x ^ y
        y = x ^ y
        x = x ^ y
    elif method == 5: # способ 5
        tmp = [x, y]
        x = tmp[1]
        y = tmp[0]
    else:
        x = 'не указан'
        y = 'способ'
    
    print('Результат: ', x, y)

    if __name__ == "__main__":
        task1(method=5) # (1-5) Пять способов поменять значения переменных местами