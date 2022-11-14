import random

def RockPaperScissor():
    user = input("Choose 'r' for rock, 's' for scissor, 'p' for paper: \n")
    computer = random.choice(['r', 'p', 's'])

    print(f"Computer: {computer}")

    if user == computer:
        print("It's a tie.")

    if winning(user, computer):
        print("You Won!")

    else:
        print("You Lost!")

def winning(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
        or (player == 'p' and opponent == 'r'):
        return True

RockPaperScissor()
