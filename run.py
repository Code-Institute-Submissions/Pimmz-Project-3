# Start of the game

print("Are you ready to play Back To Red Dwarf!")
print("You've been woken up by alarm bells and sirens going off.")
print("You're in your quarters of a spaceship called Starbug.")
print("")
print("Do you want to go to the bridge to see what the smeg is going on?")
print("Or")
print("Sit back relax and watch some zero g football with a beer?")

# User input for the first choice

userChoice = input("> ")
user_input_lower = userChoice.lower

if (userChoice == "sit back"):
    print("You sit back put your feet up and turn the game on")
    print("You grab the beer and just as you're about to open it,")
    print("It turns input a polymorph and sucks all your emotion out")
    print("The cries of Dwayne Dibbly! are heard being shouted")
    print("Followed by the sound of a blaster")
    print("")
    print("You're dead!")

elif (userChoice == "bridge"):
    print("You run to the bridge and ask what the smeg is going on?")
    print("Kryten replies, were being attacked by rouge simulants")
    print("We have two choices either fight or scarper")
    print("")
    print("What would you like to do?")

# User input for the simulant choice

    simulantChoice = input("> ")
    user_input_lower = simulantChoice.lower

    if (simulantChoice == "scarper"):
        print("You fire up the boosters and leg it")
        print("Unfortunately Starbug is slower than an arthritic hamster")
        print("The simulants laugh and blast you to pieces")
        print("")
        print("Youre Dead!")

    elif (simulantChoice == "fight"):
        print("You turn Starbug around and fire the guns")
        print("Direct hit, to their engines")
        print("The simulant ship is dead in the water, great shooting")
        print("There are no signs of life on the ship")
        print("")
        print("Do you analyse what just happened? as rimmer has suggested.")
        print("Or")
        print("Go and board their ship and see if anything is worth swipping?")

# User input for the analyse choice

        analyseChoice = input("> ")
        user_input_lower = analyseChoice.lower

        if (analyseChoice == "analyse"):
            print("You sit down with rimmer and analyse the situation")
            print("After days of analysing and organ music playing")
            print("You decide it's to much and throw yourself in space.")
            print("")
            print("You're Dead!")

        elif (analyseChoice == "board"):
            print("You board the simulant ship and start looking for goods")
            print("The cat finds a box with rejuvenating shower written on it")
            print("You all agree he can keep it, just to keep him quiet")
            print("Lister says he'll build it, he took a class once at school")
            print("")
            print("Do you let lister build it or kryten?")

# User input for the shower choice

            showerChoice = input("> ")
            user_input_lower = showerChoice.lower

            if (showerChoice == "kryten"):
                print("Kryten unpacks the shower and starts building it")
                print("After two hours hes finished and tests the device")
                print("A huge explosion happens killing everyone on board")
                print("It seems Lister had swapped out krytens ")
                print("Head to spare head two, the smeeeeg heeeeead")
                print("")
                print("You're Dead!")

            elif (showerChoice == "lister"):
                print("Lister starts building the shower")
                print("He builds it in an hour, which is very suspicious")
                print("It seems hes used abit of the luck virus")
                print("When he tests it, the whole crew are teleported to")
                print("What looks like earth, You soon realise you are on a")
                print("Backwards planet, You know this,")
                print("As the cat has just been to the toilet, yikes")
                print("The remote is dead and needs batteries")
                print("")
                print("Do you go forwards or backwards")

# User input for the lemons choice

                lemonsChoice = input("> ")
                user_input_lower = lemonsChoice.lower

                if (lemonsChoice == "forwards"):
                    print("Oh smeg, it's a backwards planet.")
                    print("You walk backwards straight off a cliff")
                    print("")
                    print("You're Dead!")

                elif (lemonsChoice == "backwards"):
                    print("Your walk forwards straight to the nearest village")
                    print("Its a Gelf village They unfortunately don't have a")
                    print("Nine volt battery for the remote but look they do")
                    print("Have lemons and copper. We could make a battery")
                    print("The Gelfs are happy to trade")
                    print("But they want Rimmer in exchange")
                    print("")
                    print("Do you exchange Rimmer for the lemons and copper?")

# User input for the lemons choice

                    tradeChoice = input("> ")
                    user_input_lower = tradeChoice.lower

                    if (tradeChoice == "yes"):
                        print("Double smeg, it's a backwards planet.")
                        print("The Gelfs take offence because you won't trade")
                        print("Plus Lister said they looked like his gran")
                        print("")
                        print("So they shoot you all, You're Dead!")

                    elif (tradeChoice == "no"):
                        print("Excellent you've got the lemons & copper, plus")
                        print("You've got rid of Rimmer, What a great day")
                        print("Kryten makes the battery and hits button")
                        print("They all teleport back to the ship")
                        print("But wait this isn't Starbug its Red Dwarf")
                        print("")
                        print("Congratulations!")
                        print("You've made it Back to Red Dwarf")

                    else:
                        print("Invalid choice. Please enter yes or no")

                else:
                    print("Invalid choice. Please enter forwards or backwards")

            else:
                print("Invalid choice. Please enter kryten or lister")

        else:
            print("Invalid choice. Please enter analyse or board")

    else:
        print("Invalid choice. Please enter scarper or fight")

else:
    print("Invalid choice. Please enter bridge or sit back")
