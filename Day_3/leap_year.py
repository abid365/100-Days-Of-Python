# make a program to check if a year is leap year or not
# divisible by 4 -> leapyear
# divisible by 100, if yes -> not leap year, if no -> move to next condition
# if divisible by 400 leap year, if not -> not leap year

year = int(input("Check leap year or not: "))
if year % 4 == 0:
    if year % 100 != 0:
        print(f"{year} is a leap year")
    elif year % 400 == 0:
        print(f"{year} is leap year")
    elif year % 400 != 0:
        print(f"{year} is not a leap year")
else:
    print(f"The {year} is not leap year")