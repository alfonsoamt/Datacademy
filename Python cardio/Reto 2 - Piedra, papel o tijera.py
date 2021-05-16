import random

def PPT():
    options = ["piedra", "papel", "tijera"]
    rounds = 1

    while rounds < 4:
        print('_'*30)

        print("Round {}.".format(rounds))
        player1 = random.choice(options)
        player2 = random.choice(options)
        print("Player 1: {}.".format(player1))
        print("Player 2: {}.".format(player2))
        win1 = 0
        win2 = 0
        
        if player1 == "piedra" and player2 =="papel":
            print("player 2 wins.")
            win2 += 1
        elif player1 == "papel" and player2 =="piedra":
            print("player 1 wins.")
            win1 += 1
        elif player1 == "tijera" and player2 =="piedra":
            print("player 2 wins.")
            win2 += 1
        elif player1 == "piedra" and player2 =="tijera":
            print("player 1 wins.")
            win1 += 1
        elif player1 == "tijeras" and player2 =="papel":
            print("player 1 wins.")
            win1 += 1
        elif player1 == "papel" and player2 =="tijera":
            print("player 2 wins.")
            win2 += 1
        else:
            print("No one wins. Repeat round.")
            continue
        rounds += 1

 
    
    print('*'*30)
    if win1 > win2:
        print("Player 1 wins the game!")
    else:
        print("Player 2 wins the game!")

if __name__ == "__main__":
    PPT()            


