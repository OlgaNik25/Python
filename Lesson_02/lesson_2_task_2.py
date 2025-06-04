def is_year_leap(year):
    if year % 4 == 0:
        return True
    else:
        return False


N_year = int(input("Введите год: "))
P_year = is_year_leap(N_year)
print("Год", N_year, ":", P_year)
