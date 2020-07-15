import time
import random


def print_pause(msg):
    print(msg)
    time.sleep(2)


def user_input(response, option1, option2):
    while 10 == 10:
        choice = input(response)
        if choice == option1:
            break
        elif choice == option2:
            break
    return choice


def welcome():
    print_pause("you find yourself in an opened field, " +
                "filled with grass and yellow sunflowers")
    print_pause("Rumor has it that sth is somewhere around here" +
                " and has been terrifying the nearby village.")
    print_pause("In front of you there is a house")
    print_pause("on your right there is cave")
    print_pause("You hold your trusty but not very effective dagger")


def gameplay(items):
    choice = user_input("enter 1 to knock on" +
                        "the door or 2 to explore the cave", "1", "2")
    if choice == "1":
        house(items)
    elif choice == "2":
        cave(items)


def cave(items):
    global combat_tools
    combat_tools = random.choice(["Thor's Axe", "Katana", "Odin's Hammer"])
    print_pause("you peer into the cave")
    if items != []:
        print_pause("You have already been here")
        print_pause("there is nothing else cool here!")
    else:
        print_pause(f"your eyes spots a glint of metal behind a rock.")
        print_pause(f"You have found {combat_tools}")
        print_pause(f"You discard your silly old dagger" +
                    f" and take {combat_tools} with you.")
    print_pause("You walk back to the field")
    items.append(combat_tools)
    gameplay(items)


def house(items):
    monster = random.choice(["a troll","a Dragon", "KingKong"])
    print_pause("you approach the door")
    print_pause(f"You are about to knock when the door " +
                f"opens and out steps {monster}")
    print_pause(f"It attacks you ")
    if items == []:
        print_pause("You feel you are week with this tiny dagger")
    choice = user_input("do you want to (1) fight or (2) run away", '1', '2')
    if choice == "1":
        if items != []:
            print_pause(f"Enemy attacks you")
            print_pause(f"You decide to use your new {combat_tools}")
            print_pause("You fight bravely and finally the VICTORY is yours")
        else:
            print_pause("You try to survive but the enemy is too strong")
            print_pause("You have been defeated")
    elif choice == "2":
        print_pause("Yoy run back and seem not to be have followed.")
        print_pause("Don't be ashamed,you saved your life now to fight later!")
        gameplay(items)


def start_game():
    items = []
    welcome()
    gameplay(items)

start_game()


another_choice = input('Do you want to play again? Type yes or no').lower()
if "yes" in another_choice:
    print_pause("ok lets play again")
    start_game()
elif "no" in another_choice:
    print("ok gg")
