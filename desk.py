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
            buff_no = str(self.no)
            while len(buff_no)<4:
                buff_no += " " 
            res = ["No." + buff_no]    
            #res.append("LVL: " + str(self.level))
            buff = self.element
            while len(buff)<6:
                buff += " "
            res.append("Ele: " + buff + "  ")
            res.append("Pnt: " + str(self.point) + "   ")
            res.append("Res: " + str(self.resource))
            return ' '.join(res)

class Player():
    def __init__(self, name):
        self.name =name
        self.Coins = [0,0,0,0,0,0]
        self.Cards = []
        self.Covers = []
        self.Heros = []
        self.Points = 0
    def __str__ (self):
        res = []
        res.append("Name: " + self.name)
        res.append("Coins: " + str(self.Coins))
        res.append("Cards: " + str(self.cal_Ele()))
        #for card in self.Cards:
        #    res.append(str(card))
        res.append("Covers: ")
        for card in self.Covers:
            res.append(str(card))
        res.append("Heros: ")
        for hero in self.Heros:
            res.append(str(hero))
        res.append("Point: " + str(self.point()))
        return str(res)
    
    def cal_Ele(self):
        resource = [0, 0, 0, 0, 0]
        for card in self.Cards:
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

    def point(self):
        pnt = 0
        for card in self.Cards:
                pnt += card.point
        pnt += len(self.Heros)*3
        return pnt


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
        print "============================================================="
        print " "
        print "-------------------- lvl 1 Card on Table --------------------"
        for card in self.Cards_on_table[0]:
            print card
        
        print "-------------------- lvl 2 Card on Table --------------------"
        for card in self.Cards_on_table[1]:
            print card

        print "-------------------- lvl 3 Card on Table --------------------"
        for card in self.Cards_on_table[2]:
            print card

        print "--------------------    Hero on table    --------------------"
        for hero in self.Heros_on_table:
            print hero

        print "----------------------  Coin on table -----------------------"
        print str(self.Coins_on_table)

        print "--------------------------- Players -------------------------"
        for player in self.Players:
            print player
        print "============================================================="
    
    def setup_hero(self):
        for i in range(0, len(self.Players) + 1 ) :
            self.Heros_on_table.append(self.Heros.pop())
    
    def draw_card(self, lvl):
        if len(self.Cards[lvl]):
            self.Cards_on_table[lvl].append(self.Cards[lvl].pop())
        elif len(self.Cards_on_table[lvl]) == 0 :
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
###################    ACT   #######################
### ACT 1 Take Coin
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
            player.Coins = [x+y for x, y in zip(take_coins, player.Coins)]
        return Error_tag


### Return Coin
    def return_coin (self, player, coins):
        Error_tag =0
        if len(coins) != 6:
            Error_tag =1
            print "Error: Return_coin len(coin) != 6"
        
        if min(coins) < 0:
            print "Error: Cant return negative numbers coin"
            Error_tag =1
        else :
            self.Coins_on_table = [y+x for x, y in zip(coins, self.Coins_on_table)]
            temp = [y-x for x, y in zip(coins, player.Coins)]
            if min(temp) < 0 :
                Error_tag = 1
                print " Coins are not enough"
            if Error_tag == 0 :
                player.Coins = temp
        return Error_tag


### ACT 2 Take Card ###
    def take_card (self, player, card):
        print "*** ACT: %s take %s" % (player.name, card)
        Error_tag =0
        #test if the resource is enough?
        need_ele = [y-x for x, y in zip(player.cal_Ele() , card.resource)]
        use_gold = 0
        for i in range(0,5):
            if need_ele[i] < 0:
                need_ele[i] = 0
            if player.Coins[i] < need_ele[i]:
                insufficient = need_ele[i] - player.Coins[i]
                use_gold += insufficient
                need_ele[i] -= insufficient
        if use_gold > player.Coins[5] :
            Error_tag = 1
            print "There are no enough coins, please retry"
            print 'your coins : %s elements: %s , card needs : %s' % ( str(player.Coins), str(player.cal_Ele()), str(card.resource))
            self.Cards_on_table[card.level-1].append(card)
        else :
            need_ele.append(use_gold)
            self.return_coin (player, need_ele)
            player.Cards.append(card)
            self.draw_card(card.level-1)
        return Error_tag

### ACT 3 Cover card ###
    def cover_card (self, player, card):
        Error_tag = 0
        # test player's covers
        if len(player.Covers) >2 :
            Error_tag =1
            print "Error : you aready cover 3 cards"
            self.Cards_on_table[card.level-1].append(card)
        else :
            player.Covers.append(card)
            self.draw_card(card.level-1)
            if self.Coins_on_table[5] > 0:
                self.Coins_on_table[5] -= 1
                player.Coins[5] += 1
            else :
                print "No golden coins"
        return Error_tag
## V ACT 
    def take_hero (self, player, hero):
        Error_tag = 0
        resource = player.cal_Ele()
        for i in range(0,5):
            if resource[i] < hero.resource[i]:
                Error_tag = 1
                print "you can't take the hero"
                self.Heros_on_table.append(hero)
                break
        if Error_tag == 0 :
            player.Heros.append(hero)

#### checker
    def checker (self):
        staus = 1 
        # status = 1 system is OK 
        # status = 0 Fatal Error will closed the game !!!
        # status = 3 Someone over 15 point 
        # status = 4 Need Return coins
        ####### check coins on the desk  ##########
        coins =[0,0,0,0,0,0]
        golden_coins = [4,4,4,4,4,5]
        for i in range(0,6):
            for player in self.Players:
                coins[i] += player.Coins[i]
            coins[i] += self.Coin_on_table[i]
        for coin, golden_coin in zip(coins,golden_coins):
            if coin != golden_coin:
                status = 0
                print "[Fetal Error: Total Coins are not the same]"
                print coins
        
        ####### check Cards #######
        cards = 0
        cards += len(self.Cards_on_table[0]) + len(self.Cards[0])
        cards += len(self.Cards_on_table[1]) + len(self.Cards[1])
        cards += len(self.Cards_on_table[2]) + len(self.Cards[2])
        for player in self.Players:
            cards += len(player.Cards)
            cards += len(player.Covers)
        if cards != 90 :
            status = 0
            print "[Fetal Error: Total Cards are not the same]"

            #--- check Cards on table ---
        for cards_t, cards in zip (self.Cards_on_table, self.Cards):
            if len(cards_t) != 4:
                if len(cards) != 0:
                    status = 0
                    print "[Fetal Error: there are not 4 cards on table]"  

        ##### check 15pt #####

        ##### check over coins ######
        ##### check take Heros ######
####
            
            
def setup_game(obj):
    obj.shuffle()
    obj.setup_player("Peter")
    obj.setup_player("Sally")
    obj.setup_table()
    obj.print_table()

A=Desk()
setup_game(A)
Peter = A.Players[0]
Sally = A.Players[1]
LVL1 = A.Cards_on_table[0]
LVL2 = A.Cards_on_table[1]
LVL3 = A.Cards_on_table[2]
