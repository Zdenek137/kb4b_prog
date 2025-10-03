import random
import os



def __clear_terminal__():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')



#globalni promenne
#https://chipy.com/academy/slots/slot-symbols#slot-symbol-meaning
symbols = ["💔", "🍉", "🍒", "🍋", "🍇", "🥝", "🔔", "💣", "💲", "💎", "🔥"]

money = 100



#generace zatoceni
while(True):
    __clear_terminal__()
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
    checking_symbol = ""

    for i in range(len(symbols)):
        checking_symbol = symbols[i]
        
        if(reel_symbols[0] == checking_symbol and reel_symbols[1] == checking_symbol and reel_symbols[2] == checking_symbol):
            print("WIN 10 ", checking_symbol, " ROW")
            money += 10
        if(reel_symbols[3] == checking_symbol and reel_symbols[4] == checking_symbol and reel_symbols[5] == checking_symbol):
            print("WIN 10 ", checking_symbol, " ROW")
            money += 10
        if(reel_symbols[6] == checking_symbol and reel_symbols[7] == checking_symbol and reel_symbols[8] == checking_symbol):
            print("WIN 10 ", checking_symbol, " ROW")
            money += 10

    print("MONEY: ", money)
    #hrat znova
    input()
