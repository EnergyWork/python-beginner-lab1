def task8():
    """
        #8 Все трехзначные числа Армстронга
    """
    for num in range(100, 1000, 1):
        if num == sum([int(x)**3 for x in str(num)]):
            print(num)

if __name__ == "__main__":
    task8() # Все трехзначные числа Армстронга