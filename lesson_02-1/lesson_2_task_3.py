import math


def square(s):
    return math.ceil(s**2)


num_side = float(input("Введите сторону квадрата: "))
print(f'Площадь квадрата равна:{square(num_side)}')
