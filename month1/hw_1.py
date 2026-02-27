mon = int(input("Расходы за понедельник: "))
tue = int(input("Расходы за вторник: "))
wed = int(input("Расходы за среду: "))
thu = int(input("Расходы за четверг: "))
fri = int(input("Расходы за пятницу: "))
sat = int(input("Расходы за субботу: "))
sun = int(input("Расходы за воскресенье: "))

week = mon + tue + wed + thu + fri + sat + sun
average = week // 7

print("Общая сумма расходов:", week)
print("Средний расход в день:", average)


#поискал в инете как улучшить код и вот что получилось
#expenses = []
#days = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
#
#for day in days:
#    expense = float(input(f"Введите расходы за {day}: "))
#    expenses.append(expense)
#
#total_expense = sum(expenses)
#average_expense = int(total_expense / 7)
#
#print(f"Общие расходы за неделю: {total_expense:.2f}")
#print(f"Средний расход в день: {average_expense}")
