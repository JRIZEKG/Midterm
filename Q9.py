def days_since_birthday(birthday):
    """""
    :param BD: your birth date
    :return: number of days alive
    """""
    day, month, year = map(int, birthday.split('-'))
    import datetime
    current_date = datetime.datetime.now()
    years_passed = current_date.year - year - 1
    total_days_passed = 0
    for i in range(year + 1, current_date.year):
        if i % 4 == 0 and (i % 100 != 0 or i % 400 == 0):  # Checking for leap year
            total_days_passed += 366
        else:
            total_days_passed += 365
    total_days_passed += (current_date - datetime.datetime(current_date.year, month, day)).days
    return total_days_passed
birthday = "20-11-2003"
print("Days passed since birthday:", days_since_birthday(birthday) )