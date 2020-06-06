import random
class Hero:
    def __init__(self, name: str, hp: int, damage: int):
        self.name = name
        self.hp = hp
        self.damage = damage
        print('Hi Iam',self.name, self.hp, self.damage)

    def attack(self)-> int:
        return self.damage
    def attacked(self, damage: int)-> bool:
        if self.hp - damage <= 0:
            print(self.name,'died...')
            return True
        else:
            self.hp = self.hp - damage
            print(self.name,self.hp)
            return False

you = Hero('You',100,20)
monster = Hero('Monster',100,30)

while True:
    is_died = False
    lucky = random.randrange(1,3) # 1 2 3 4
    too = int(input('Тоо оруулна уу: '))
    if lucky == too:
        is_died = monster.attacked(you.attack())
    else:
        is_died = you.attacked(monster.attack())

    if is_died:
        break
else:
    print('Game Over...')
