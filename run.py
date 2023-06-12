# Start of the game

print("Are you ready to play Back To Red Dwarf!")
print("Youve been woken up by alaram bells and sirens going off.")
print("You're in your quarters of a spaceship called Starbug.")
print("Do you want to go to the bridge to see what the smeg is going on?)
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

    if (userChoice == "scarpa"):
        print("You fire up the boosters and leg it")
        print("Unfortunately starbug is slower than an arthritic hamster")
        print("The simulants laugh and blast you to pieces")
        print("Youre Dead!")

    elif (userChoice == "fight")
    print("You turn starbug around and fire the guns")
    print("Direct hit, to there engines")
    print("The simulant ship is dead in the water, great shooting")
    print("There are no signs of life on the ship")
    print("Do you analyse what just happened? as rimmer has suggested.")
    print("Or")
    print("Go and board their ship and see if anything is worth swipping?")

    else:
        print("Invalid choice. Please enter scarpa or fight.")
