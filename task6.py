def task6():
    """
        #6 Числа Фибоначчи
    """
    n = int(input())
    #i = 0
    fib = [1, 1]
    for _ in range(n):
        fib.append(fib[-1] + fib[-2])
    #while i < n - 2:
    #    fib.append(fib[-1] + fib[-2])
    #    i += 1
    print(fib)

if __name__ == "__main__":
    task6() # Числа Фибоначчи