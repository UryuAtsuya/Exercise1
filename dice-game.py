import random

def roll_dice():
    return random.randint(1,6)

def dice_game():
    name = input("What is your name?\n>")
    print("Hello, " + name + "!")
    print("Rolling dice...")
    die1 = roll_dice()
    die2 = roll_dice()
    print("Die 1: ",die1)
    print("Die 2: ",die2)
    total_value = die1 + die2
    print("Toral value: ",total_value)

    if total_value > 7:
        print(name + " won!")
    else:
        print(name +" lost!")

dice_game()