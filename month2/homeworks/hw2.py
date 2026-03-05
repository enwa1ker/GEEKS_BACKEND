import random


class Hero:

    def __init__(self, name, level, health, strength):
        self.name = name
        self.level = level
        self.health = health
        self.strength = strength

    def greet(self):
        return f'Привет, я {self.name}, мой уровень {self.level}'

    def attack(self):
        self.strength -= 1
        return f'{self.name} наносит удар!'

    def rest(self):
        self.health += 1
        return f'{self.name} отдыхает и восстанавливает здоровье…'


class Warrior(Hero):

    def __init__(self, name, level, health, strength, stamina):
        super().__init__(name, level, health, strength)
        self.stamina = stamina

    def attack(self):
        self.stamina -= 1
        return f'Воин атакует мечом!'


class Mage(Hero):

    def __init__(self, name, level, health, strength, mana):
        super().__init__(name, level, health, strength)
        self.mana = mana

    def attack(self):
        self.mana -= 1
        return f'Маг кастует заклинание!'


class Assassin(Hero):

    def __init__(self, name, level, health, strength, stealth):
        super().__init__(name, level, health, strength)
        self.stealth = stealth

    def attack(self):
        self.stealth -= 1
        return f'Ассасин атакует из-под тишка!'


gandalf = Mage('Gandalf', 100, 1000, 100, 100)
print(gandalf.greet())
print(gandalf.attack())
print(f'Мана: {gandalf.mana}')
print(gandalf.rest())
print(f'Здоровье: {gandalf.health}')

print()

aragorn = Warrior('Aragorn', 90, 900, 90, 80)
print(aragorn.greet())
print(aragorn.attack())
print(f'Выносливость: {aragorn.stamina}')
print(aragorn.rest())
print(f'Здоровье: {aragorn.health}')

print()

altair = Assassin('Altair', 80, 800, 80, 90)
print(altair.greet())
print(altair.attack())
print(f'Скрытность: {altair.stealth}')
print(altair.rest())
print(f'Здоровье: {altair.health}')

print()

# Мини-игра "Камень, Ножницы, Бумага"

print('🎮 Мини-игра "Камень, Ножницы, Бумага" ')
print("Выберите героя: Warrior | Mage | Assassin")
choice = input("Введите название героя: ").strip().lower()

if choice == "Warrior":
    player = Warrior('Игрок', 1, 100, 10, 5)
elif choice == "Mage":
    player = Mage('Игрок', 1, 100, 10, 5)
elif choice == "Assassin":
    player = Assassin('Игрок', 1, 100, 10, 5)
else:
    print("Неверный выбор героя. Игра завершена.")
    exit()

opponents = [aragorn, gandalf, altair]
computer = random.choice(opponents)
computer_type = type(computer).__name__

print(f"\nВы выбрали: {choice}")
print(f"Противник: {computer_type} ({computer.name})")
print()

if choice == computer_type:
    print("Ничья!")
elif (choice == "Warrior" and computer_type == "Assassin") or \
     (choice == "Assassin" and computer_type == "Mage") or \
     (choice == "Mage" and computer_type == "Warrior"):
    print(f"{choice} победил!")
else:
    print(f"{computer_type} победил!")