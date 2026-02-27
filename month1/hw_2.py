# day = int(input("Введите день вашего рождения(с 1 до 31) p.s. если у вас др в феврале то вводите до 28-го:"))
# month = int(input("Введите месяц вашего рождения(с 1 до 12): "))
#
# if (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 20):
#     print("Ваш знак зодиака Овен")
#
# elif (month == 4 and 21 <= day <= 30) or (month == 5 and 1 <= day <= 21):
#     print("Ваш знак зодиака Телец")
#
# elif (month == 5 and 22 <= day <= 31) or (month == 6 and 1 <= day <= 21):
#     print("Ваш знак зодиака Близнецы")
#
# elif (month == 6 and 22 <= day <= 30) or (month == 7 and 1 <= day <= 22):
#     print("Ваш знак зодиака Рак")
#
# elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 21):
#     print("Ваш знак зодиака Лев")
#
# elif (month == 8 and 22 <= day <= 31) or (month == 9 and 1 <= day <= 23):
#     print("Ваш знак зодиака Дева")
#
# elif (month == 9 and 24 <= day <= 30) or (month == 10 and 1 <= day <= 23):
#     print("Ваш знак зодиака Весы")
#
# elif (month == 10 and 24 <= day <= 31) or (month == 11 and 1 <= day <= 22):
#     print("Ваш знак зодиака Скорпион")
#
# elif (month == 11 and 23 <= day <= 30) or (month == 12 and 1 <= day <= 22):
#     print("Ваш знак зодиака Стрелец")
#
# elif (month == 12 and 23 <= day <= 31) or (month == 1 and 1 <= day <= 20):
#     print("Ваш знак зодиака Козерог")
#
# elif (month == 1 and 21 <= day <= 31) or (month == 2 and 1 <= day <= 19):
#     print("Ваш знак зодиака Водолей")
#
# elif (month == 2 and 20 <= day <= 28) or (month == 3 and 1 <= day <= 20):
#     print("Ваш знак зодиака Рыбы")
#
# else:
#     print("Вводите только цифры (от 1 до 31 и месяцы от 1 до 12)")

day = int(input("Введите день вашего рождения (1–31): "))
month = int(input("Введите месяц вашего рождения (1–12): "))


if month < 1 or month > 12:
    print("Ошибка: месяца с таким номером не существует")


elif month == 2 and day > 28:
    print("Ошибка: в феврале максимум 28 дней")
elif month in [4, 6, 9, 11] and day > 30:
    print("Ошибка: в этом месяце только 30 дней")
elif day < 1 or day > 31:
    print("Ошибка: день должен быть с 1 до 31")

elif (month == 3 and 21 <= day <= 31) or (month == 4 and 1 <= day <= 20):
    print("Ваш знак зодиака Овен")

elif (month == 4 and 21 <= day <= 30) or (month == 5 and 1 <= day <= 21):
    print("Ваш знак зодиака Телец")

elif (month == 5 and 22 <= day <= 31) or (month == 6 and 1 <= day <= 21):
    print("Ваш знак зодиака Близнецы")

elif (month == 6 and 22 <= day <= 30) or (month == 7 and 1 <= day <= 22):
    print("Ваш знак зодиака Рак")

elif (month == 7 and 23 <= day <= 31) or (month == 8 and 1 <= day <= 21):
    print("Ваш знак зодиака Лев")

elif (month == 8 and 22 <= day <= 31) or (month == 9 and 1 <= day <= 23):
    print("Ваш знак зодиака Дева")

elif (month == 9 and 24 <= day <= 30) or (month == 10 and 1 <= day <= 23):
    print("Ваш знак зодиака Весы")

elif (month == 10 and 24 <= day <= 31) or (month == 11 and 1 <= day <= 22):
    print("Ваш знак зодиака Скорпион")

elif (month == 11 and 23 <= day <= 30) or (month == 12 and 1 <= day <= 22):
    print("Ваш знак зодиака Стрелец")

elif (month == 12 and 23 <= day <= 31) or (month == 1 and 1 <= day <= 20):
    print("Ваш знак зодиака Козерог")

elif (month == 1 and 21 <= day <= 31) or (month == 2 and 1 <= day <= 19):
    print("Ваш знак зодиака Водолей")

elif (month == 2 and 20 <= day <= 28) or (month == 3 and 1 <= day <= 20):
    print("Ваш знак зодиака Рыбы")

else:
    print("Ошибка введите только числа и попробуйте снова")