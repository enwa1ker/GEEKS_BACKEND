while True:
    word = input("Введите слово (или 'exit'): ")

    if word.lower() == 'exit':
        break

    word = word.replace(" ", "")
    total = len(word)

    if total == 0:
        print("Пусто!")
        continue

    vowels = "аеёиоуыэюяaeiouy"
    consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz"

    v_count = 0
    c_count = 0

    for s in word.lower():
        if s in vowels:
            v_count += 1
        elif s in consonants:
            c_count += 1

    v_perc = round((v_count / total) * 100, 2)
    c_perc = round((c_count / total) * 100, 2)

    print(f"Общее количество букв: {total}")
    print(f"Гласные: {v_count} ({v_perc}%)")
    print(f"Согласные: {c_count} ({c_perc}%)")
    print("-" * 10)


# тут пытался сделать так чтобы программа завершалась при нажатии клавиши escape, но как то не получилось(((

# import keyboard
#
# print("Программа запущена. Для выхода в любой момент нажмите 'Esc'")
#
# while True:
#     # Проверяем, нажата ли клавиша Esc
#     if keyboard.is_pressed('esc'):
#         print("Выход из программы...")
#         break
#
#     word = input("Введите слово: ")
#
#     # Если пользователь ввел слово и нажал Enter, считаем буквы
#     word = word.replace(" ", "")
#     total = len(word)
#
#     if total == 0:
#         continue
#
#     vowels = "аеёиоуыэюяaeiouy"
#     consonants = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz"
#
#     v_count = 0
#     c_count = 0
#
#     for s in word.lower():
#         if s in vowels:
#             v_count += 1
#         elif s in consonants:
#             c_count += 1
#
#     v_perc = round((v_count / total) * 100, 2)
#     c_perc = round((c_count / total) * 100, 2)
#
#     print(f"Всего: {total} | Гласные: {v_count} ({v_perc}%) | Согласные: {c_count} ({c_perc}%)")
#     print("Нажмите Esc для выхода или введите новое слово.")