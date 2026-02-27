class Hero:

    # Конструктор класса
    def __init__(self, name, lvl=1, hp=100):
        self.name = name
        self.lvl = lvl
        self.hp = hp

    def action(self):
        print(f'{self.name} атакует!')
    
    def __str__(self):
        return f'Герой {self.name}, уровень {self.lvl}, здоровье {self.hp}'

#Экземпляр класса Hero
kirito = Hero('Kirito')
ichigo = Hero('Ichigo', 90, 900)
luffy = Hero('Luffy', 80, 800)

print(kirito.name, kirito.lvl, kirito.hp)
print(ichigo.name, ichigo.lvl, ichigo.hp)   
print(luffy.name, luffy.lvl, luffy.hp)
print(luffy.__dict__)

kirito.action()
ichigo.action()
luffy.action()

kirito.hp -= 100
print(kirito.hp)

print(kirito)


kirito.name = 'Kirito the Black Swordsman'
print(kirito)



my_int = 5
print(my_int.__str__())

my_str = "Hello"
print(my_str.__str__())
my_list = [1, 2, 3]
print(my_list.__str__())
print(my_list)


kirito = Hero('Kirito')
print(kirito)
