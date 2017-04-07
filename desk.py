import csv
class Hero():
    def __init__(self, resource):
        self.resource = resource
    def __str__(self):
        return self.resource 

class Card():
    def __init__ (self, level, element, point, resource):
        self.resource = resource
        self.level = level
        self.element = element
        self.point = point
    def __str__(self):
            res = []
            res.append(str(self.level))
            res.append(str(self.element))
            res.append(str(self.point))
            return ' '.join(res)

class Desk():
    def __init__(self):
        self.player = []
        self.coin = [7,7,7,7,7,5]
        self.Card_I= []
        self.Heros = []
        for i in range(0,5):
            w =     ((i%5==0) or (i%5==1))*4
            blu =   ((i%5==1) or (i%5==2))*4
            g =     ((i%5==2) or (i%5==3))*4
            r =     ((i%5==3) or (i%5==4))*4
            bla =   ((i%5==4) or (i%5==0))*4
            self.Heros.append(,)
            
    def print_all(self):
        for card in self.Cards_I:
            print card

class Player():
    def __init__(self, name):
            self.name =name

peter_game =Desk()
peter_game.print_all()

