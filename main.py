import datetime
import calendar
import re

def replace_numbers_with_stars(date_str):
    result = re.sub(r'\d+', lambda match: '*' * len(match.group()), date_str)

    return result


# Функция для определения дня недели
def get_weekday(day, month, year):
    return calendar.day_name[datetime.date(year, month, day).weekday()]

# Функция для проверки, является ли год високосным
def is_leap_year(year):
    return calendar.isleap(year)

# Функция для вычисления возраста пользователя
def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age


# Основная часть программы
def main():
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))
    formatted_date = f"{day}.{month}.{year}"
    print(f"Дата рождения: {formatted_date}")
    birthdate = datetime.date(year, month, day)
    weekday = get_weekday(day, month, year)
    leap = "високосный" if is_leap_year(year) else "не високосный"
    age = calculate_age(birthdate)
    print(f"День недели вашего рождения: {weekday}")
    print(f"Год вашего рождения {leap}.")
    print(f"Вам сейчас {age} лет.")
    print(replace_numbers_with_stars(formatted_date))

if __name__ == "__main__":
    main()