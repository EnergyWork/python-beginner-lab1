def task7():
    """
        #7 Все перестановки трехзначного числа
    """
    from itertools import permutations
    n = input()
    perm = list(filter(lambda x: x > 99, list(set([int(''.join(x)) for x in permutations([x for x in n])])))) 
    print(perm)

if __name__ == "__main__":
    task7() # Все перестановки трехзначного числа