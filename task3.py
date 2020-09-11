import math

def task3():
    """
        #3 Найти значение функции
    """
    x = int(input())
    if x > 0:
        print(math.sqrt(4 * x))
    elif x < 0:
        print(abs(x))
    else:
        print(math.exp(1))

if __name__ == "__main__":
    task3() # Найти значение функции