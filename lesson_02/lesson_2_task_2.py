def is_year_leap(y):
    if y % 4 == 0:
        return True
    else:
        return False


year = int(input("Введите год: "))
result = is_year_leap(year)

print(f'год {year}: {result}')
