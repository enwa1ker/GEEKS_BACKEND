import time

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Задание 1 — Проверка администратора
def is_admin(func):
    def wrapper(user):
        if user.role == "admin":
            return func(user)
        else:
            print("У вас нет доступа")
    return wrapper

@is_admin
def delete_video(user):
    print("Видео удалено")

# Задание 2 — Декоратор таймера
def timer(func):
   
    def wrapper():
        start = time.time()
        result = func()
        end = time.time()
        duration = end - start
        print(f"Время выполнения: {round(duration, 1)} секунд")
        return result
    return wrapper

@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")


admin = User("Ardager", "admin")
simple_user = User("Bek", "user")


delete_video(admin)  
delete_video(simple_user) 

download_video()