import csv  # Для роботи з CSV-файлами
import random  # Для генерації випадкових значень
from faker import Faker  # Для генерації фейкових даних
from datetime import datetime, timedelta  # Для роботи з датами

# Ініціалізуємо об'єкт Faker для генерації фейкових даних англійською мовою
fake = Faker('en_US')

# Функція для генерації випадкової дати народження
def generate_birthdate():
    start_date = datetime(1938, 1, 1)
    end_date = datetime(2008, 12, 31)
    days_between = (end_date - start_date).days
    random_days = random.randint(0, days_between)
    birthdate = start_date + timedelta(days=random_days)
    return birthdate.strftime('%Y-%m-%d')

# Функція для генерації випадкового ім'я по батькові
def generate_middle_name(gender):
    if gender == 'Female':
        return fake.first_name_female()
    elif gender == 'Male':
        return fake.first_name_male()
    else:
        return fake.first_name()

# Створюємо CSV-файл з вказаною структурою
with open('employees2.csv', mode='w', newline='', encoding='utf-8') as file:
    fieldnames = ['Last Name', 'First Name', 'Middle Name', 'Gender', 'Date of Birth', 'Position', 'City of Residence',
                  'Address', 'Phone', 'Email']
    writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
    writer.writeheader()

    num_records = 2000  # Загальна кількість записів
    num_female = int(num_records * 0.4)  # Кількість жіночих записів (40% від загальної кількості)
    num_male = num_records - num_female  # Кількість чоловічих записів (решта)

    # Генеруємо і записуємо дані для жіночих працівників
    for _ in range(num_female):
        writer.writerow({
            'Last Name': fake.last_name_female(),
            'First Name': fake.first_name_female(),
            'Middle Name': generate_middle_name('Male'),  # Тут "Male" може бути помилково, має бути "Female"
            'Gender': 'Female',
            'Date of Birth': generate_birthdate(),
            'Position': fake.job(),
            'City of Residence': fake.city(),
            'Address': fake.address(),
            'Phone': fake.phone_number(),
            'Email': fake.email()
        })

    # Генеруємо і записуємо дані для чоловічих працівників
    for _ in range(num_male):
        writer.writerow({
            'Last Name': fake.last_name_male(),
            'First Name': fake.first_name_male(),
            'Middle Name': generate_middle_name('Male'),  # Тут "Male" може бути помилково, має бути "Male"
            'Gender': 'Male',
            'Date of Birth': generate_birthdate(),
            'Position': fake.job(),
            'City of Residence': fake.city(),
            'Address': fake.address(),
            'Phone': fake.phone_number(),
            'Email': fake.email()
        })




