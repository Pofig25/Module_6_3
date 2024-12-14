import random
                                        # Необходимо написать 5 классов:
class Animal:                           # Animal - класс описывающий животных.
    live = True                         # live = True
    sound = None                        # sound = None - звук (изначально отсутствует)
    _DEGREE_OF_DANGER = 0               # _DEGREE_OF_DANGER = 0 - степень опасности существа
    def __init__(self, speed):          # Объект этого класса обладает следующими атрибутами:
        self._cords = [0, 0, 0]         # _cords = [0, 0, 0] - координаты в пространстве.
        self.speed = speed              # speed =...- скорость передвижения существа (определяется при создании объекта)

    def move(self, dx, dy, dz):                     # move(self, dx, dy, dz), который должен менять соответствующие
        self._cords[0] += dx * self.speed           # кооординаты в _cords на dx, dy и dz в том же порядке,
        self._cords[1] += dy * self.speed           # где множетелем будет являтся speed.
        self._cords[2] += dz * self.speed
        if self._cords[2] <= 0:                             #  Если при изменении координаты z в _cords значение меньше 0,
            print("It's too deep, i can't dive :(")         # то выводить сообщение "It's too deep, i can't dive :(",
            self._cords[2] = 0                              # при этом изменения не вносяться.

    def get_cords(self):                         # get_cords(self), выводит координаты в формате: "X: <координаты по x>,
        print(f'X:{self._cords[0]}, Y:{self._cords[1]}, Z:{self._cords[2]}') # Y: <координаты по y>, Z: <координаты по z>"

    def attack(self):                                           # attack(self), который выводит "Sorry, i'm peaceful :)",
        if self._DEGREE_OF_DANGER < 5:                          # если степень опасности меньше 5
            print("Sorry, i'm peaceful :)")
        else:                                                   # и "Be careful, i'm attacking you 0_0" , если равно или больше.
            print("Be careful, i'm attacking you 0_0")

class Bird(Animal):                                              # Bird - класс описывающий птиц. Наследуется от Animal.
    beak = True                                                  # beak = True - наличие клюва

    def lay_eggs(self):                                          # lay_eggs(self), который выводит строку "Here are(is)
        print(f"Here are(is)', {random.randint(1, 4)} eggs for you")    # <случайное число от 1 до 4> eggs for you"

class AquaticAnimal(Animal):                                    # AquaticAnimal - класс плавающего животного. От Animal.
    _DEGREE_OF_DANGER = 3                                       # В этом классе атрибут _DEGREE_OF_DANGER = 3.
    def dive_in(self, dz):                                      # dive_in(self, dz)
        self._cords[2] -= int((abs(dz) * self.speed)/2)         # Скорость при нырянии уменьшается в 2 раза.

class PoisonousAnimal(Animal):                      # PoisonousAnimal - класс ядовитых животных. Наследуется от Animal.
    _DEGREE_OF_DANGER = 8                                       # В этом классе атрибут _DEGREE_OF_DANGER = 8.

class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):   # Duckbill - класс утконоса. Наследуется от классов Bird,
    def __init__(self, speed):                          # AquaticAnimal, PoisonousAnimal. Порядок наследования
        super().__init__(speed)                         # определите сами, опираясь на ниже приведённые примеры
        self.sound = "Click-click-click"                # выполнения кода.
                                                    # Объект этого класса должен обладать одним дополнительным атрибутом:
    def speak(self):                                # sound = "Click-click-click" - звук, который издаёт утконос
        print(self.sound)

db = Duckbill(10)

print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()
