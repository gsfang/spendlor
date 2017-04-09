import csv
import random

class Hero():
    def __init__(self, resource):
        self.resource = resource
    def __str__(self):
        return str(self.resource)

class Card():
    def __init__ (self,no, level, element, point, resource):
        self.no = no
        self.resource = resource
        self.level = level
        self.element = element
        self.point = point
    def __str__(self):
            res = []#["No." + self.no ]
            #res.append("LVL: " + str(self.level))
            res.append("Ele: " + str(self.element))
            res.append("Pnt: " + str(self.point))
            res.append("Res: " + str(self.resource))
            return ' '.join(res)

class Player():
    def __init__(self, name):
        self.name =name
        self.Coins = []
        self.Hands = []
        self.Covers = []
        self.Heros = []
        self.Points = []
    def __str__ (self):
        res = []
        res.append("Name:" + self.name)
        res.append("Coins: " + str(self.Coins))
        res.append("Hands: " + str(self.Hands))
        res.append("Covers: " + str(self.Covers))
        res.append("Heros: " + str(self.Heros))
        res.append("Point: " + str(self.Points))
        return str(res)
    
    def take_coin (self,coin):
        self.Coins = self.Coins + coin
        if sum(self.Coins) > 10:
            print "The total Coins are more than 10 please return_coin(list) :"
            print ", ".join(self.Coins)
            
            
    def return_coin(self,coin):
        temp = self.Coins - coin
        Error_tag = 0
        for i in temp:
            if i < 0 :
                Error_tag = 1
                print " Coins < 0, please try again"
        if Error_tag == 0 :
            self.Coins = temp
        if sum() > 10 :
            print "The total Coins are more than 10 please return_coin(list) :"
            print ", ".join(self.Coins)

#def take_card (self, card):
    
    

    def cal_Ele(self):
        resource = [0, 0, 0, 0, 0]
        for card in self.Hands:
            if card.element == "White":
                resource[0] += 1
            elif card.element == "Blue":
                resource[1] += 1
            elif card.element == "Green":
                resource[2] += 1
            elif card.element == "Red":
                resource[3] += 1
            elif card.element == "Black":
                resource[4] += 1
            else :
                print "Error: Card's element not in list"
        return resource

class Desk():
    def __init__(self):
        self.Players = []
        self.Coins = [7,7,7,7,7,5]
        self.Cards= []
        self.Heros = []
        self.Cards_on_table = [[],[],[]]
        self.Heros_on_table = []
        self.Coins_on_table = []
        ## all Heros
        for i in range(0,5):
            w =     ((i%5==0) or (i%5==1))*4
            blu =   ((i%5==1) or (i%5==2))*4
            g =     ((i%5==2) or (i%5==3))*4
            r =     ((i%5==3) or (i%5==4))*4
            bla =   ((i%5==4) or (i%5==0))*4
            resource = [w,blu,g,r,bla]
            self.Heros.append(Hero(resource))
        for i in range(0,5):
            w =     ((i%5==0) or (i%5==1) or (i%5==2))*3
            blu =   ((i%5==1) or (i%5==2) or (i%5==3))*3
            g =     ((i%5==2) or (i%5==3) or (i%5==4))*3
            r =     ((i%5==3) or (i%5==4) or (i%5==0))*3
            bla =   ((i%5==4) or (i%5==0) or (i%5==1))*3
            resource = [w,blu,g,r,bla]
            self.Heros.append(Hero(resource))
        ## all cards
        with open('spendlor.csv', 'rb') as csvfile:
            card_data =[row for row in csv.reader(csvfile)]
            card_lv1 = []
            card_lv2 = []
            card_lv3 = []
            for card in card_data:
                if card[0] == 'No':
                    continue
                for i in range(0,9):
                    if i != 2 :
                        if card[i] :
                            card[i] = int(card[i])
                        else :
                            card[i] = 0
                if card[1] == 1:
                    card_lv1.append(Card(card[0],card[1],card[2],card[8],card[3:8]))
                elif card[1] == 2:
                    card_lv2.append(Card(card[0],card[1],card[2],card[8],card[3:8]))
                elif card[1] == 3:
                    card_lv3.append(Card(card[0],card[1],card[2],card[8],card[3:8]))
        self.Cards = [card_lv1, card_lv2, card_lv3]
    
    def shuffle(self):
        random.shuffle(self.Cards[0])
        random.shuffle(self.Cards[1])
        random.shuffle(self.Cards[2])
        random.shuffle(self.Heros)
    
    def print_table(self):
        print " lvl 1 Card on Table : "
        for card in self.Cards_on_table[0]:
            print card
        
        print " lvl 2 Card on Table : "
        for card in self.Cards_on_table[1]:
            print card

        print " lvl 3 Card on Table : "
        for card in self.Cards_on_table[2]:
            print card

        print "Hero on table :"
        for hero in self.Heros_on_table:
            print hero

        print "Coin on table :"
        print str(self.Coins_on_table)

        print " Players :"
        for player in self.Players:
            print player
    
    def setup_hero(self):
        for i in range(0, len(self.Players) + 1 ) :
            self.Heros_on_table.append(self.Heros.pop())
    
    def draw_card(self, lvl):
        if len(self.Cards[lvl]):
            self.Cards_on_table[lvl].append(self.Cards[lvl].pop())
        else :
            print "Cards Pool are empty"

    def setup_player(self,name):
        self.Players.append(Player(name))

    def setup_coin(self):
        if len(self.Players) == 2 :
            self.Coins_on_table = [4,4,4,4,4,5]
        elif len(self.Players) == 3:
            self.Coins_on_table = [5,5,5,5,5,5]
        else :
            self.Coins_on_table = [7,7,7,7,7,5]

    def setup_table(self):
        for i in range(0,4):
            peter_game.draw_card(0)
            peter_game.draw_card(1)
            peter_game.draw_card(2)
        peter_game.setup_coin()
        peter_game.setup_hero()




peter_game =Desk()
peter_game.shuffle()
#peter_game.print_all()

peter_game.setup_player("Peter")
peter_game.setup_player("Sally")
peter_game.setup_table()
peter_game.print_table()

peter_game.Players[0].take_coin([0,0,0,0,0,1])
peter_game.print_table()

