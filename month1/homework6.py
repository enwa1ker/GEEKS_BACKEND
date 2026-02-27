def check_password(password):

    if len(password) < 6:
        return False

    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)

    special_chars = [char for char in password if not char.isalnum()]
    has_two_symbols = len(special_chars) >= 2
    
    return all([has_digit, has_upper, has_lower, has_two_symbols])


weak_passwords = ["12345", "password", "Qwerty123", "Admin!!", "???!!!", "short"]

print("Проверка стандартных слабых паролей:")
for pw in weak_passwords:
    result = "Надежный" if check_password(pw) else "Слабый"
    print(f"- {pw:12} : {result}")

print("\n" + "-"*30 + "\n")

user_pw = input("Введите ваш пароль для проверки: ")

if check_password(user_pw):
    print(" Этот пароль прошел проверку")
else:
    print(" Пароль слишком слабый. Убедитесь, что в нем есть цифры, разные регистры и хотя бы 2 спецсимвола.")


def find_closest(numbers, target=0):
    if not numbers:
        return None
    return min(numbers, key=lambda x: abs(x - target))

try:

    raw_input = input("Введите числа через пробел (например: 1 2.5 10 -3): ")
 
    user_list = [float(x) for x in raw_input.split()]

    target_str = input("Введите целевое число (или нажмите Enter для 0): ")
    
    user_target = float(target_str) if target_str.strip() else 0

    if user_list:
        result = find_closest(user_list, user_target)
        print(f"\nБлижайшее число к {user_target} из вашего списка: {result}")
    else:
        print("Список пуст, искать не в чем.")

except ValueError:
    print(" Ошибка: вводите только числа, разделенные пробелом!")