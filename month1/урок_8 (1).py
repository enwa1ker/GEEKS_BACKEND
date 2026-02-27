# Повторение

keywords_list = """False               class               from                or
None                continue            global              pass
True                def                 if                  raise
and                 del                 import              return
as                  elif                in                  try
assert              else                is                  while
async               except              lambda              with
await               finally             nonlocal            yield
break               for                 not""".split()

kw_dict = {}
passed = 0
failed = 0

print("***Оценка усвоения материала***")

for kw in keywords_list:
    while True:
        val = input(f'Проходили ли мы - "{kw}"? (0-10): ').strip()
        try:
            score = int(val)
            if 0 <= score <= 10:
                kw_dict[kw] = score
                break
            print("Нужно ввести число от 0 до 10!")
        except ValueError:
            print("Вводите только цифры!")

    if score > 0:
        passed += 1
    else:
        failed += 1

total = len(keywords_list)
percent = round((passed / total) * 100, 1)

sorted_stats = sorted(kw_dict.items(), key=lambda x: x[1], reverse=True)

print("\n" + "—" * 20)
print(f"Всего: {total}")
print(f"Пройдено: {passed}  | Не пройдено: {failed}")
print(f"Процентное соотношение: {percent}% из 100%")
print("—" * 20)

print("Личное освоение:")
for word, grade in sorted_stats:
    print(f"{word.ljust(10)}: {grade}")  

# """Домашнее задание №8
# 1) посчитать и вывести:
#  - общее количество слов
#  - пройденное количество
#  - не пройденное
#  - процентное соотношение прим. 75% из 100% 

# 2) Создать словарь и наполнять его в цикле по мере ответов.

# 3) Отсортировать словарь с ключевыми словами по величине оценки.

# 4) Вывести весь список ключевых слов в словаре (пары ключ: значение), 
# где ключом будут слова а значением 0 или от 1 до 10 по мере
# личного освоения.
