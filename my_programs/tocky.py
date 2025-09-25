import random

#globalni promenne
#https://chipy.com/academy/slots/slot-symbols#slot-symbol-meaning
symbols = ["💔", "🍉", "🍒", "🍋", "🍇", "🥝", "🔔", "💣", "💲", "💎", "🔥"]

money = 100



#generace zatoceni
while(True):
    money -= 5

    reel_symbols = []

    for i in range(9):
        reel_symbols.append(random.choice(symbols))

    print(" =======================")
    for i in range(9):
        print(" | " + reel_symbols[i] + " | ", end="")
        if(i == 2 or i == 5):
            print("")
    print("")
    print(" =======================")

    #vyhodnoceni radku
    


    #hrat znova
    input()
