while True:
    try:
        year = int(input("Please enter the year between 1900 and 100000: "))
        if year < 1900 or year > 10 ** 5:
            raise ValueError
        break
    except ValueError:
        print("This input doesn't look like valid year, try again.")

def is_leap(year):
    leap = False
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        leap = True
    return leap
print(is_leap(year))
