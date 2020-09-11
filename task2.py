def task2():
    """
        #2 Определить четверть
    """
    x = int(input())
    y = int(input())

    if x == 0:
        if y == 0:
            print('начало')
        else:
            print('Ox')
    elif y == 0:
        print('Oy')
    elif x > 0:
        if y > 0:
            print(1)
        else:
            print(4)
    elif x < 0:
        if y > 0:
            print(2)
        else:
            print(3)

if __name__ == "__main__":
    task2() # Определить четверть