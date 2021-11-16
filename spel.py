import time,sys


def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(0.05)
#Introduction som skrivs ut innan spelet "börjar"
def intro():
    print()
    print_slow("Darkness")
    time.sleep(1)
    print()
    print_slow("Nothing but darkness")
    time.sleep(1)
    print()
    print_slow("You feel around you, struggling to understand what is going on")
    time.sleep(1)
    print()
    print_slow("The ground is cold to the touch")
    time.sleep(1)
    print()
    print_slow("You stand up and reach for your phone")
    time.sleep(1)
    print()
    print_slow("No cell connection")
    time.sleep(1)
    print()
    print_slow("You turn on the flashlight and look around")
    time.sleep(1)
    print()
    print_slow("I gotta get out of here")
    time.sleep(1)
    print()
    time.sleep(1)
    firstchoice()

#Det första valet spelaren får göra
def firstchoice():
    print()
    time.sleep(1)
    print_slow("You look ahead and see 3 paths leading in different directions. Which do you choose?")
    time.sleep(1)
    print()
    print_slow("To your right is a tunnel with what looks like a distant, very faint light")
    time.sleep(1)
    print()
    print_slow("Right ahead is a wall with very thick vines leading upwards. They look sturdy enough to climb up")
    time.sleep(1)
    print()
    print_slow("To your left is an opening leading to a large body of water")
    time.sleep(1)
    print()
    first_choice=input("Where will you go? Right, Left or Forward?: ").strip().lower()
    if first_choice == "left" or "l":
        print("You chose to go left and explore the waters")
    elif first_choice == "right" or "r":
        print("You chose to go right and wander into the tunnel opening")
    elif first_choice == "forward" or "f":
        print("You chose to go forward, making oyur way towards the large rock wall and the vines that are climbing up it")

#Jobbig grej
def clear():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()

def start():
    play = input("Would you like to start the game? (yes/no): ").lower().strip()
    if play == "yes":
     intro()
    elif play == "no":
        print("Maybe next time")
    elif play != "yes" or "no":
        again()


def again():
    time.sleep(1)
    print_slow("Please enter a valid answer")
    clear()
    start()





clear()
start()







