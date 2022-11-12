import random
while(True):
    print("Press q to quit")
    def gamewin(comp,player):
        if player == 'q':
            exit()
        if comp == player:
            return None
        elif comp == 's':
            if player == 'w':
                return False
            elif player == 'g':
                return True
        elif comp == 'w':
            if player == 'g':
                return False
            elif player == 's':
                return True
        elif comp == 'g':
            if player == 's':
                return False
            elif player == 'w':
                return True


    print("Comp Turn:Snake(s) Water(w) Gun(g)?")
    randNo = random.randint(1,3)

    if randNo == 1:
        comp = 's'
    elif randNo == 2:
        comp = 'w'
    elif randNo == 3:
        comp = 'g'

    player = input("Your's Turn:Snake(s) Water(w) Gun(g)?")

    gamewin(comp,player)

    print(f"comp chose {comp}")
    print(f"player chose {player}")

    a = gamewin(comp,player)
    if a == None:
        print("The game is tie!")
    elif a:
        print("You win!")
    else:
        print("You Lose!")


# -------------------------------------------------------------or----------------------------------------------------------------

import random

while(True):
    def play():
        user = input("What's your choise 's' for snake, 'w' for water,'g' for gun\n")
        computer = random.choice(['s', 'w', 'g'])
        print(computer)

        if user == computer:
            return 'tie'

        if is_win(user, computer):
            return 'You Won!'

        return 'You Lost!'

    def is_win(player, opponent):
        # return true if player wins
        # r > s, s > p, p > r
        if (player=='s' and opponent == 'w') or (player == 's' and opponent == 'g')\
            or (player == 'w' and opponent == 'g'):
            return True

    print(play())
# ------------------------------------------------------------------------------------------------------------------------------------
