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
        return f'{self.name} отдыхает…'


ichigo = Hero('Ichigo', 90, 900, 80)
print(ichigo.greet())
print(ichigo.attack())
print(ichigo.health)   
print(ichigo.rest())
print(ichigo.health)  


DustinPorier = Hero('Dustin Porier', 80, 800, 70)
print(DustinPorier.greet())
print(DustinPorier.attack())
print(DustinPorier.strength)
print(DustinPorier.rest())
print(DustinPorier.health)
