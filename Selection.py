# Week 3 practice from Online Weekly Work

year = int(input("Please enter the current year: "))
if year % 4 == 0 and year % 100 != 0:
    print(year, " is a leap year.")
elif year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
    print(year, " is a leap year.")
else:
    print(year, " is not a leap year.")
