def leap_year(year):
    year = year % 400
    if (0 == year) or (year % 100 != 0):
        if year % 4 == 0:
            return True
    return False
print(leap_year(2000))