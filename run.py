import random
import time
import sys
import os


class Player:
    def __init__(self, name):
        self.name = name


player_attributes = Player('')


def introduction():
    """
    Opens the game with the title screen and introduction
    to the story of the game.
    """
    print()
    print("""
 _____                                          __  ___  ___                    
|_   _|                                        / _| |  \/  |                    
  | |_ __ ___  __ _ ___ _   _ _ __ ___    ___ | |_  | .  . | __ _ ______ _ _ __ 
  | | '__/ _ \/ _` / __| | | | '__/ _ \  / _ \|  _| | |\/| |/ _` |_  / _` | '__|
  | | | |  __/ (_| \__ \ |_| | | |  __/ | (_) | |   | |  | | (_| |/ / (_| | |   
  \_/_|  \___|\__,_|___/\__,_|_|  \___|  \___/|_|   \_|  |_/\__,_/___\__,_|_|   
    """)
    print()
    print("""
     
     ]╢▒▒▒▒▒▒╣▒▒▒▒▒▒▒▒▒╣▒▒▒▒▒╣▒▒▒╢╫╣╬▓▓▀▀╣
     ╘▒▒▒▒▒▒▒▒▒░░░░░░░ ░░░░▒▒▒▒▒▒▒▒▒▒░▒▒▒╢
      ▒▒░▒▒▒▒▒▒▒▒▒▒▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒░▒▒░▒
      ╙▒░░▒▒▒▒▒▒▒╣▒▒▒▒░░▒▒▒▒▒▒▒▒▒▒▒░░░░░░
       ╚▒▒▒▒▒▒╣╣╣╣╣╣▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░╫╣▒▒`
        "╬▒░░▒╢╣╣╣╣╣▒▒▒▒▒▒▒▒▒▒▒▒▒▒╢╫╣▒▒
           ▀╩▓╣╢▓▓▓▓▓▓▓▓▓▓╣╣╢╣╣╣╣▒▓▀╙
                 `"╙▓▓▓╣╣▓▓▓"``
                    ╟▓▓▓▓▓▓⌐
                     ╟╢▓▓▓M
                     ▐▓▓▌▓
                   ,╔╣▓╬▀▀▀╖,
                 ╫▓▒╢╣╬@▒░╬╬╣▓Γ
    """)
    print()
    print("Long ago, a powerful king named Mazar reigned undisputed.\n")
    print("Until one day, he was betrayed by his son and his reign ended.\n")
    print("Before his death, Mazar built a great tomb and stashed his most prized treasure.\n")
    print("It's wherabouts laid secret for untold years...\n")
    print("Until suddenly, rumours began to spread of its supposed location.\n")
    print("Many went in search for the great treasures within.\n")
    print("But not a single soul has returned to tell the tale.\n")
    print("Will you enter the tomb and succeed where others have failed...?\n")
    print("Do you have what it takes to claim the fabled Treasure of Mazar?\n")
    start_game()


def start_game():
    """
    Lets the user choose to start the game and enter
    their name before beginning.
    """
    start_choice = input("Are you ready to start your adventure? (Yes/No)\n")
    if start_choice.lower().strip() == "yes":
        player_attributes.name = input("What is your name?\n")
        print(f"Welcome {player_attributes.name}. Your adventure awaits!\n")
        begin_adventure()
    elif start_choice.lower().strip() == "no":
        print("Very well... Please take your time.")
        time.sleep(5)
        os.system('cls||clear')
        introduction()
    else:
        print("Please type Yes or No!")
        start_game()


def begin_adventure():
    """
    Sets the beginning of the story and provides the choice
    between entering the tomb or not.
    """
    print()
    print("Hearing the rumours of the tomb of Mazar, you set off in search of fortune.\n")
    print("You arrive at a misty ruin in a forest where the air is still.\n")
    print("Shivers run down your spine as you see a great doorway to a tomb.\n")
    print(f"{player_attributes.name}: 'This must be it... The tomb of Mazar!'\n")
    print(f"{player_attributes.name}: 'Somewhere inside is the fabled Treasure of Mazar...'\n")
    print(f"{player_attributes.name}: 'If I find that, I could live like a king!'\n")
    print(f"{player_attributes.name}: 'But then again, nobody has ever come out alive...'\n")
    print(f"{player_attributes.name}: 'Should I really risk my life for this?'\n")
    enter_choice = input("Do you want to enter the tomb? (Yes/No)\n")
    if enter_choice.lower().strip() == "yes":
        print(f"{player_attributes.name}: 'There's no turning back now! Here I go!'\n")
        print("You push open the great tomb doors and make your way into the depths below.\n")
    elif enter_choice.lower().strip() == "no":
        print(f"{player_attributes.name}: 'No... I can't do this. My life is more valuable than any treasure.'\n")
    else:
        print("Please type Yes or No!")
        time.sleep(2)
        begin_adventure()


#def enter_tomb():


#def path_1():


#def path_2():


#def path_3():


#def path_4():


#def path_5():


#def path_6():


#def try_again(): 


#def death():


#def end_1():


#def end_2():


#def end_3():


#def end_4():


introduction()