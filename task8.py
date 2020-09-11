def task8():
    """
        #8 Все трехзначные числа Армстронга
    """
    #способ 1
    for num in range(100, 1000, 1):
        if num == sum([int(x)**3 for x in str(num)]):
            print(num)

    #способ 2
    mas = list(filter(lambda x: x != 0, [num if num == sum([int(x)**3 for x in str(num)]) else 0 for num in range(100, 1000, 1)]))
    print(mas)

if __name__ == "__main__":
    task8() # Все трехзначные числа Армстронга