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
        self.Coins = [0,0,0,0,0,0]
        self.Hands = []
        self.Covers = []
        self.Heros = []
        self.Points = 0
    def __str__ (self):
        res = []
        res.append("Name:" + self.name)
        res.append("Coins: " + str(self.Coins))
        res.append("Hands: " + str(self.Hands))
        res.append("Covers: " + str(self.Covers))
        res.append("Heros: " + str(self.Heros))
        res.append("Point: " + str(self.Points))
        return str(res)
    
    def take_coin (self, coin):
        self.Coins = [x+y for x, y in zip(coin, self.Coins)]
        if sum(self.Coins) > 10:
            print "The total Coins are more than 10 please return_coin(list) :"
            print str(self.Coins)
            
            
    def return_coin (self, coin):
        if len(coin) == 6:
            Error_tag = 0
        else:
            Error_tag = 1
            print "The coin items should be 6"
        temp = [y-x for x, y in zip(coin, self.Coins)]
        if min(temp) < 0 :
            Error_tag = 1
            print " Coins < 0, please try again"
        if Error_tag == 0 :
            self.Coins = temp
        if sum(self.Coins) > 10 :
            print "The total Coins are more than 10 please return_coin(list) :"
            print str(self.Coins)
        return Error_tag    

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
            self.draw_card(0)
            self.draw_card(1)
            self.draw_card(2)
        self.setup_coin()
        self.setup_hero()

    def take_coin (self, player, take_coins):
        Error_tag = 0
        take_coins.append(0)
        ## the take coins need be 5
        if len (take_coins) != 6:
            Error_tag =1
            print "Error: Take_coin len(coin) != 6"
        elif sum(take_coins) > 3:
            Error_tag =1
            print "Error: You take more than 3 coins"
        
        ## table have no enough coins
        temp = [y-x for x, y in zip(take_coins, self.Coins_on_table)]
        if min (temp) < 0:
            Error_tag =1
            print "Error: Coin on table is less than you wanna take"
        ## check if 1 item more than 2
        elif max(take_coins) > 1:
            if sum(take_coins) >2 :
                Error_tag =1
                print "Error: You cant take 3 coins and 2 from the same element"
            elif self.Coins_on_table[take_coins.index(2)] < 4:
                print "Error: The element you want take 2 is less than 4 coins on table"
                Error_tag =1
        
        if Error_tag == 0:
            self.Coins_on_table = [y-x for x, y in zip(take_coins, self.Coins_on_table)]
            player.take_coin(take_coins)
        return Error_tag

    def return_coin (self, player, return_coins):
        Error_tag =0
        if len (return_coins) != 6:
            Error_tag =1
            print "Error: Return_coin len(coin) != 6"
        
        if min(return_coins) < 0:
            print "Error: Cant return negative numbers coin"
            Error_tag =1
            return Error_tag
        else :
            self.Coins_on_table = [y+x for x, y in zip(return_coins, self.Coins_on_table)]
            return player.return_coin(return_coins)

    def take_card (self, player, take_cards):
        print 'player $s take %s ' % (str(player),str(take_cards))
        Error_tag =0
        #test if the resource is enough?
        player.cal_Ele()
        need_ele = [y-x for x, y in zip(player.cal_Ele() , take_cards.resource)]
        use_gold = 0
        for i in range(0,5):
            if need_ele[i] < 0:
                need_ele[i] = 0
            if player.Coins[i] >= need_ele[i]:
                continue
            else:
                use_gold +=  player.Coins[i] - need_ele[i]
        if use_gold > player.Coins[6] :
            Error_tag = 1
            print "There ara no enough coins, please retry"
            print 'your coins : %s elements: %s , card needs : %s' $ ( str(player.Coins[i]), str(player.cal_Ele()), str(take_cards.resource))
        else :
            self.return_coin (player, need_ele.append(use_gold))
            player.Cards
        return Error_tag

         

                              







