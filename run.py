# Start of the game

print("Are you ready to play Back To Red Dwarf!")
print("Youve been woken up by alaram bells and sirens going off.")
print("You're in your quarters of a spaceship called Starbug.")
print("Do you want to go to the bridge to see what the smeg is going on?")
print("or")
print("Sit back relax and watch some zero g football with a beer?")

# User input for the first choice

userChoice = input("> ")

if (userChoice == "sit back"):
    print("You sit back put your feet up and turn the game on")
    print("You grab the beer and just as you're about to open it,")
    print("It turns input a polymorph and sucks all your emotion out")
    print("The crys of dwayne dibbly!! are heard being shouted")
    print("Followed by the sound of a blaster")
    print("You're dead!")

elif (userChoice == "bridge"):
    print("You run to the bridge and ask what the smeg is going on?")
    print("Kryten replies, were being attacked by rouge simulants")
    print("We have two choices either fight or scrapa")
    print("What would you like to do?")

else:
    print("Invalid choice. Please enter bridge or sit back.")

# User input for the simulant choice

    simulantChoice = input("> ")

    if (simulantChoice == "scarpa"):
        print("You fire up the boosters and leg it")
        print("Unfortunately starbug is slower than an arthritic hamster")
        print("The simulants laugh and blast you to pieces")
        print("Youre Dead!")

    elif (simulantChoice == "fight"):
        print("You turn starbug around and fire the guns")
        print("Direct hit, to there engines")
        print("The simulant ship is dead in the water, great shooting")
        print("There are no signs of life on the ship")
        print("Do you analyse what just happened? as rimmer has suggested.")
        print("Or")
        print("Go and board their ship and see if anything is worth swipping?")

    else:
        print("Invalid choice. Please enter scarpa or fight.")

# User input for the analyse choice

    analyseChoice = input("> ")

    if (analyseChoice == "analyse"):
        print("You sit down with rimmer and analyse the situation")
        print("After days of analysing and organ music playing in the background")
        print("You decide its to much and throw yourself in space without a suit")
        print("You're Dead!")

    elif (analyseChoice == "board"):
        print("You board the simulant ship and start looking for goods to swipe")
        print("The cat finds a box with rejuvenating shower written on it")
        print("You all agree he can keep it, just to keep him quiet")
        print("Lister says he'll build it as he took a class once at art school")
        print("Do you let lister build it or kryten?")

    else:
       print("Invalid choice. Please enter analyse or board.")

# User input for the shower choice