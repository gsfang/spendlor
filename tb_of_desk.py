from desk import Desk

peter_game =Desk()
peter_game.shuffle()
#peter_game.print_all()

peter_game.setup_player("Peter")
peter_game.setup_player("Sally")
peter_game.setup_table()
peter_game.print_table()
print "############################# GAME START ###################################"
#peter_game.Players[0].take_coin([0,0,0,0,0,1])
peter_game.take_coin(peter_game.Players[0],[0,2,0,0,0])
#peter_game.print_table()
peter_game.take_coin(peter_game.Players[0],[2,0,0,0,0])
#peter_game.print_table()
peter_game.take_coin(peter_game.Players[0],[0,0,2,0,0])
#peter_game.print_table()
peter_game.take_coin(peter_game.Players[0],[0,0,0,2,0])
#peter_game.print_table()
peter_game.take_coin(peter_game.Players[0],[0,0,0,0,2])
peter_game.take_coin(peter_game.Players[0],[0,0,1,1,1])
peter_game.take_coin(peter_game.Players[0],[0,1,1,1,0])
peter_game.take_coin(peter_game.Players[0],[1,1,1,0,0])
print "================= take  coins ==================="
peter_game.print_table()

print "================= take  cards ==================="
#peter_game.print_table()

peter_game.take_card (peter_game.Players[0], peter_game.Cards_on_table[0].pop(0))
print peter_game.Players[0]
peter_game.take_card (peter_game.Players[0], peter_game.Cards_on_table[0].pop(0))
print peter_game.Players[0]
peter_game.take_card (peter_game.Players[0], peter_game.Cards_on_table[0].pop(0))
print peter_game.Players[0]
peter_game.take_card (peter_game.Players[0], peter_game.Cards_on_table[0].pop(0))
print peter_game.Players[0]
peter_game.take_card (peter_game.Players[0], peter_game.Cards_on_table[0].pop(0))
print peter_game.Players[0]
peter_game.take_card (peter_game.Players[0], peter_game.Cards_on_table[0].pop(0))
print peter_game.Players[0]
peter_game.take_card (peter_game.Players[0], peter_game.Cards_on_table[0].pop(0))
print peter_game.Players[0]
peter_game.take_card (peter_game.Players[0], peter_game.Cards_on_table[0].pop(0))
print peter_game.Players[0]
peter_game.take_card (peter_game.Players[0], peter_game.Cards_on_table[1].pop(0))
print peter_game.Players[0]
print "====================="
peter_game.print_table()