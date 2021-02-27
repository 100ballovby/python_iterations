from itertools import *
from string import *
# все буквы и циферки
alphabet = digits + ascii_letters
# 0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ


def brute_force(a, ml, mxl):
    """алфавит, min_длина, max_длина"""
    joiner = ''.join

    for cur_len in range(ml, mxl + 1):
        yield from map(joiner, product(a, repeat=cur_len))


# Пароль может состоять из 3 чисел и 2 букв латинского алфавита.
# Минимальная длина 1, максимальная 3
alph = '123AB'
print(*brute_force(alph, 1, 5), sep=', ')