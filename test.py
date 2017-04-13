
def test_take_coins(obj):

    print "[Test]: peter take 2 blue"
    obj.take_coin(obj.Players[0],[0,2,0,0,0])
    print "[Test]: Error peter take 2 blue"
    obj.take_coin(obj.Players[0],[0,2,0,0,0])
    print "[Test]: peter take 2 white"
    obj.take_coin(obj.Players[0],[2,0,0,0,0])
    print "[Test]: Error peter take 2 white and 1 blue"
    obj.take_coin(obj.Players[0],[2,1,0,0,0])
    print "[Test]: Error peter take 5 elements"
    obj.take_coin(obj.Players[0],[1,1,1,1,1])
    print "[Test]: Error peter take 4 elements"
    obj.take_coin(obj.Players[0],[0,1,1,1,1])
    print "[Test]: peter take 3 elements"
    obj.take_coin(obj.Players[0],[0,1,1,1,0])

def test_take_card(obj):
    print "[Test] : Error sally take card lvl 0"
    obj.take_card(obj.Players[1],obj.Cards_on_table[0][0])
    print "[Test] : peter take card lvl 0"
    obj.take_card(obj.Players[0],obj.Cards_on_table[0][0])
    print "[Test] : peter take card lvl 0"
    obj.take_card(obj.Players[0],obj.Cards_on_table[0][0])
    print "[Test] : peter take card lvl 0"
    obj.take_card(obj.Players[0],obj.Cards_on_table[0][0])
    
def test_take_all_coins(obj):
    print "[Test] take all coins"
    for i in range(0,6):
        obj.Players[0].Coins[i] += obj.Coins_on_table[i]
        obj.Coins_on_table[i] = 0 
