import random

player = int(input("Please tell me your choice(rock-1 scissors-2 paper-3): "))
computer = random.randint(1, 3)
print("player gives %d - computer gives %d" % (player, computer))

if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("Score! The computer sucks")
elif player == computer:
    print("Wow we really have a tacit understanding")
else:
    print("Fine, you win...")
