import csv
import matplotlib.pyplot as plt
from datetime import datetime, date

# Функція для обчислення віку на основі дати народження
def calculate_age(birthdate):
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

# Функція для обчислення категорії віку
def calculate_age_category(age):
    if age < 18:
        return "молодше 18"
    elif 18 <= age <= 45:
        return "18-45"
    elif 45 < age <= 70:
        return "45-70"
    else:
        return "старше 70"

# Зчитування даних з CSV-файлу
data = []
try:
    with open('employees2.csv', mode='r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=';')
        for row in csv_reader:
            # Розбирання дати народження у форматі 'YYYY-MM-DD'
            birthdate = datetime.strptime(row['Date of Birth'], '%Y-%m-%d').date()
            age = calculate_age(birthdate)
            row['Age'] = age
            data.append(row)
except FileNotFoundError:
    print("CSV-файл не знайдено.")
    exit(1)
except Exception as e:
    print(f"Помилка при зчитуванні CSV-файлу: {e}")
    exit(1)

# Завдання 2: Підрахунок співробітників за статтю
male_count, female_count = 0, 0
for row in data:
    if row['Gender'] == 'Male':
        male_count += 1
    elif row['Gender'] == 'Female':
        female_count += 1

print(f"Кількість співробітників чоловіків: {male_count}")
print(f"Кількість співробітників жінок: {female_count}")

# Побудова графіку розподілу за статтю
plt.figure(figsize=(6, 4))
plt.bar(['Чоловіки', 'Жінки'], [male_count, female_count])
plt.title('Розподіл за статтю співробітників')
plt.xlabel('Стать')
plt.ylabel('Кількість')
plt.show()

# Завдання 3: Підрахунок співробітників за категорією віку
age_categories = {"молодше 18": 0, "18-45": 0, "45-70": 0, "старше 70": 0}
for row in data:
    age = row['Age']
    category = calculate_age_category(age)
    age_categories[category] += 1

print("Співробітники за категорією віку:")
for category, count in age_categories.items():
    print(f"{category}: {count}")

# Побудова графіку розподілу за категорією віку
plt.figure(figsize=(8, 4))
plt.bar(age_categories.keys(), age_categories.values())
plt.title('Розподіл співробітників за категорією віку')
plt.xlabel('Категорія віку')
plt.ylabel('Кількість')
plt.show()

# Завдання 4: Підрахунок співробітників за категорією віку та статтю
age_category_gender = {"молодше 18": {"Чоловіки": 0, "Жінки": 0},
                       "18-45": {"Чоловіки": 0, "Жінки": 0},
                       "45-70": {"Чоловіки": 0, "Жінки": 0},
                       "старше 70": {"Чоловіки": 0, "Жінки": 0}}

for row in data:
    age = row['Age']
    category = calculate_age_category(age)
    gender = row['Gender']

    # Перевірка наявності ключа перед збільшенням лічильника
    if gender in age_category_gender[category]:
        age_category_gender[category][gender] += 1

print("Співробітники за категорією віку та статтю:")
for category, gender_count in age_category_gender.items():
    print(f"Категорія: {category}")
    print(f"  Чоловіки: {gender_count['Чоловіки']}")
    print(f"  Жінки: {gender_count['Жінки']}")

# Побудова графіків розподілу за категорією віку та статтю
categories = age_category_gender.keys()
male_counts = [age_category_gender[category]['Чоловіки'] for category in categories]
female_counts = [age_category_gender[category]['Жінки'] for category in categories]

plt.figure(figsize=(10, 6))
plt.bar(categories, male_counts, label='Чоловіки', width=0.4)
plt.bar(categories, female_counts, label='Жінки', width=0.4, bottom=male_counts)
plt.title('Розподіл за категорією віку та статтю співробітників')
plt.xlabel('Категорія віку')
plt.ylabel('Кількість')
plt.legend()
plt.show()