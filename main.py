import datetime
import calendar

DIGIT_ART = {
    '0': [
        '***',
        '* *',
        '* *',
        '* *',
        '***'
    ],
    '1': [
        '** ',
        ' * ',
        ' * ',
        ' * ',
        '***'
    ],
    '2': [
        '***',
        '  *',
        '***',
        '*  ',
        '***'
    ],
    '3': [
        '***',
        '  *',
        '***',
        '  *',
        '***'
    ],
    '4': [
        '* *',
        '* *',
        '***',
        '  *',
        '  *'
    ],
    '5': [
        '***',
        '*  ',
        '***',
        '  *',
        '***'
    ],
    '6': [
        '***',
        '*  ',
        '***',
        '* *',
        '***'
    ],
    '7': [
        '***',
        '  *',
        '  *',
        '  *',
        '  *'
    ],
    '8': [
        '***',
        '* *',
        '***',
        '* *',
        '***'
    ],
    '9': [
        '***',
        '* *',
        '***',
        '  *',
        '***'
    ],
    '.': [
        '   ',
        '   ',
        ' * ',
        '   ',
        '   '
    ]
}

def print_art_date(date_str):
    digits = list(date_str)
    for line in range(5):
        art_line = ' '.join([DIGIT_ART[d][line] for d in digits])
        print(art_line)

def get_weekday(day, month, year):
    return calendar.day_name[datetime.date(year, month, day).weekday()]


def is_leap_year(year):
    return calendar.isleap(year)

def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year
    if (today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

def main():
    day = int(input("Введите день рождения: "))
    month = int(input("Введите месяц рождения: "))
    year = int(input("Введите год рождения: "))
    formatted_date = f"{day}{month}{year}"
    
    print(f"\nДата рождения: {day}.{month}.{year}")
    print("\nДата рождения в виде звёздочек:")
    print_art_date(f"{day}.{month}.{year}")
    
    birthdate = datetime.date(year, month, day)
    weekday = get_weekday(day, month, year)
    leap = "високосный" if is_leap_year(year) else "не високосный"
    age = calculate_age(birthdate)
    
    print(f"\nДень недели вашего рождения: {weekday}")
    print(f"Год вашего рождения {leap}.")
    print(f"Вам сейчас {age} лет.")

if __name__ == "__main__":
    main()
