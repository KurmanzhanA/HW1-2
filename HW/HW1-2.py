class Superhero:
    people = 'people'

    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.heath_points = health_points
        self.catchphrase = catchphrase

    def names(self):
        return f'Name {self.name}'

    def hp2(self):
        return self.heath_points * 2

    def __str__(self):
        return f'Nickname {self.nickname}\n' \
               f'Superpower {self.superpower}\n' \
               f'Health {self.heath_points}'

    def __len__(self):
        return len(self.catchphrase)

mage = Superhero('Ororo', 'Storm', 'Ruler of Weather', 100, 'This battle is over.')
print(mage.names())
print(mage.hp2())
print(mage.__str__())
print(mage.__len__())

class Lightninghero(Superhero):
    lightning = 'lightning'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp2(self):
        self.fly = True
        return self.heath_points * self.heath_points

    def flight(self):
        return f' fly in the {self.fly}_phrase'



class Firehero(Superhero):
    fire = 'fire'
    def __init__(self, name, nickname, superpower, health_points, catchphrase, damage, fly = False):
        super().__init__(name, nickname, superpower, health_points, catchphrase)
        self.damage = damage
        self.fly = fly

    def hp2(self):
        self.fly = True
        return self.heath_points * self.heath_points

    def flight(self):
        return f' fly in the {self.fly}_phrase'
lightning_girl = Lightninghero('Kira', 'Kitsune', 'Sword', 90, 'I am the Messanger of Death', 40)
fire_woman = Firehero('Jean Grey', 'Phoenix Force', 'Fire', 300, 'Now and forever — I am Phoenix!', 100)
print(lightning_girl.hp2(),
      lightning_girl.flight())
print(fire_woman.hp2(),
      fire_woman.flight())

class Villain(Firehero):
    Superhero.people = 'Monster'

    def gen_x(self):...


    def crit(self, other):
        return other.damage * 2

evil = Villain('Jack Napier', 'Joker', 'Manipulation', 100, 'Why so serious?', 70)
print(Villain.crit(evil, lightning_girl))
print(Villain.crit(evil, fire_woman))