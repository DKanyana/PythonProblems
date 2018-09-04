def leap_year(year):
    if len(str(year)) == 4 and (year%400 ==0 or (year%4 ==0 and year%100 != 0)):
        return True
    else:
        return False

year = 201
print(leap_year(year))


# year%400 == 0
# year%4 ==0 and year%100 ! =0