import random

def martingale(bankroll):
    loss = False
    win = 0
    bet = 3
    pockets = ["Red"] * 18 + ["Black"] * 18 + ["Green"] * 2
    bankroll_history = []
    while bankroll-bet > 0:
        if loss == False:
            if bankroll >= 93 and bankroll < 108.5:
                bet = 3
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 124:
                bet = 3.5
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 139.5:
                bet = 4
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 155:
                bet = 4.5
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 170.5:
                bet = 5
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 186:
                bet = 5.5
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 189:
                bet = 6
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 220.5:
                bet = 3
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 252:
                bet = 3.5
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 283.5:
                bet = 4
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 315:
                bet = 4.5
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 346.5:
                bet = 5
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 378:
                bet = 5.5
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            elif bankroll < 381:
                bet = 6
                print("Bankroll: $", bankroll, " Bet: $", bet, " ")
            else:
                bet = 3

        roll = random.choice(pockets)
        if roll == "Black":
            print("WIN! $",bet, "\n")
            bankroll += bet
            loss = False
            win = win+1
        else:
            bankroll -= bet
            print("Loss! $",bet, "\n")
            bet *=2
            loss = True
        bankroll_history.append(bankroll)
    print("Won ", win, " times")
    return bankroll_history

#martingale(bankroll=150)
print(martingale(bankroll=150))

