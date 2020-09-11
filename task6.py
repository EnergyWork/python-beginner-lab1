def task6():
    """
        #6 Числа Фибоначчи
    """
    n = int(input())
    fib = [0, 1]
    for _ in range(n - 2):
        fib.append(fib[-1] + fib[-2])
    print(fib)

if __name__ == "__main__":
    task6() # Числа Фибоначчи