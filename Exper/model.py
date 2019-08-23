#from handler import *
#from main import *
class Player (object):
    def __init__(self, _name, _level, _hp, _damage):
        self.name = _name
        self.level = _level
        self.hp = _hp
        self.damage = _damage
        self.isDead = False

    def reportHealth (self):
        print("%s has %d hp " % (self.name, self.hp))


    def attack(self, targetCharacter):
        targetCharacter.hp = targetCharacter.hp - self.damage
        print("%s did %d damage to %s" % (self.name, self.damage, targetCharacter.name))
        self.reportHealth()
        targetCharacter.reportHealth()
        if targetCharacter.hp <= 0:
            targetCharacter.isDead = True
            print("%s has died" % (targetCharacter.name))


class User (object):
    def __init__(self, _username, _password):
        self.username = _username
        self.password = _password

class Monster (object):
    def __init__(self, _name, _damage, _level, _hp):
        self.name = _name
        self.damage = _damage
        self.level = _level
        self.hp = _hp
        self.isDead = False

    def attack(self, targetCharacter):
        targetCharacter.hp = targetCharacter.hp - self.damage
        if targetCharacter.hp <= 0:
            targetCharacter.isDead = True
#def get_damage (self, amouDam)
    def reportHealth (self):
        print("%s has %d hp " % (self.name, self.hp))


class Room(object):
    def __init__(self, _description , _connectedRooms, _enemy,_img):
        self.connectedRooms = _connectedRooms
        self.description = _description
        self.enemy = _enemy
        self.img = _img
class Goblin(Monster):
    def __init__ (self):
        self.name = "Goblin"
        self.hp = 100
        self.level = 1
        self.damage = 20

    def attack(self, targetCharacter):
        targetCharacter.hp = targetCharacter.hp - self.damage
        print("%s did %d damage to %s" % (self.name, self.damage, targetCharacter.name))
        self.reportHealth()
        targetCharacter.reportHealth()
        if targetCharacter.hp <= 0:
            targetCharacter.isDead = True
            print("%s has died" % (targetCharacter.name))

class Hobgoblin(Monster):
    def __init__ (self):
        self.name = "HobGoblin"
        self.hp = 150
        self.level = 2
        self.damage = 30

    def attack(self, targetCharacter):
        targetCharacter.hp = targetCharacter.hp - self.damage
        print("%s did %d damage to %s" % (self.name, self.damage, targetCharacter.name))
        self.reportHealth()
        targetCharacter.reportHealth()
        if targetCharacter.hp <= 0:
            targetCharacter.isDead = True
            print("%s has died" % (targetCharacter.name))
class GoblinKing(Monster):
    def __init__ (self):
        self.name = "Goblin King"
        self.hp = 200
        self.level = 3
        self.damage = 50

    def attack(self, targetCharacter):
        targetCharacter.hp = targetCharacter.hp - self.damage
        print("%s did %d damage to %s" % (self.name, self.damage, targetCharacter.name))
        self.reportHealth()
        targetCharacter.reportHealth()
        if targetCharacter.hp <= 0:
            targetCharacter.isDead = True
            print("%s has died" % (targetCharacter.name))
class NoMonster(Monster):
    def __init__ (self):
        self.name = "None"
        self.hp = 0
        self.level = 0
        self.damage = 0

goblin1 = GoblinKing ()
player1 = Player ("ken", 1, 100, 100)


player1.attack(goblin1)
goblin1.attack(player1)
player1.attack(goblin1)
