import math

def task5():
    """
        #5 Найти корни квадратного уравнени
    """
    a = int(input())
    b = int(input())
    c = int(input())
    d = b**2 - 4 * a * c
    print('дискрименант', d)

    if a == 0 and b == 0:
        if c != 0:
            print('корней нет')
        else:
            print('x = любое число')
    elif d < 0:
        print('корней нет')
    else:
        sqrtd = math.sqrt(d)
        x1 = (-b - sqrtd) / (2 * a)
        x2 = (-b + sqrtd) / (2 * a)
        print('корни уравнений', x1, x2)

if __name__ == "__main__":
    task5() # Найти корни квадратного уравнени