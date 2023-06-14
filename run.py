# Start of the game

print("Are you ready to play Back To Red Dwarf!")
print("Youve been woken up by alargot o bridgem bells and sirens going off.")
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
    print("We have two choices either fight or scarpa")
    print("What would you like to do?")

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
            print("Lister says he'll build it, as he took a class once at art school")
            print("Do you let lister build it or kryten?")

        else:
            print("Invalid choice. Please enter analyse or board.")

# User input for the shower choice
    
            showerChoice = input("> ")
    
            if (showerChoice == "kryten"):
                print("kryten unpacks the shower and starts building it")
                print("After about two hours hes finished and starts to test the device")
                print("A huge explosion happens killing everyone on board")
                print("It seems Lister had swapped out krytens head to spare head two")
                print("You're Dead!")

            elif (showerChoice == "Lister"):
                print("Lister starts building the shower")
                print("He builds it in under and hour, which is very suspicious")
                print("It seems hes used abit of the luck virus")
                print("When he tests it, the whole crew are teleported to what looks like earth")
                print("You soon realise you are on a backwards planet. You know this, as the cat has just been to the toilet, yikes")
                print("The remote for the teleporter is dead and needs batteries. Do you go forwards or backwards")

            else:
                print("Invalid choice. Please enter forwards or backwards.")

# User input for the lemons choice

                lemonsChoice = input("> ")

                if (lemonsChoice == "forwards"):
                    print("Oh smeg, its a backwards planet.")
                    print("You walk backwards straight off a cliff")
                    print("You're Dead!")

                elif (lemonsChoice == "backwards"):
                    print("Your walk forwards straight to the nearest village")
                    print("Its a Gelf village. They unfortunately dont have a nine volt battery for the remote")
                    print("But look they have lemons and copper. We could make a battery says kryten")
                    print("The Gelfs are happy to trade, but want rimmer in exchange")
                    print("Do you exchange rimmer for the lemons and copper?")

                else:
                    print("Invalid choice. Please enter yes or no.")

else:
    print("Invalid choice. Please enter bridge or sit back.")

