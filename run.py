# Start of the game

print("Are you ready to play Back To Red Dwarf?")
print("")
print("You've been woken up by alarm bells and sirens going off.")
print("You're in your quarters of a spaceship called Starbug.")
print("")
print("Do you want to go to the bridge to see what the smeg is going on?")
print("Or sit back relax and watch some zero g football with a beer?")

# User input for the first choice

userChoice = input("> ")
user_input_lower = userChoice.lower()

if (userChoice == "sit back"):
    print("")
    print("You sit back put your feet up and turn the game on")
    print("You grab the beer and just as you're about to open it,")
    print("It turns input a polymorph and sucks all your emotion out")
    print("The cries of Dwayne Dibbly! are heard being shouted")
    print("Followed by the sound of a blaster")
    print("")
    print("You're dead!")
    quit()

elif (userChoice == "bridge"):
    print("")
    print("You run to the bridge and ask what the smeg is going on?")
    print("Kryten replies, were being attacked by rouge simulants")
    print("")
    print("We have two choices either fight or scarper")
    print("What would you like to do?")
    print("")

else:
    print("Invalid choice. Please enter bridge or sit back")

# User input for the simulant choice

simulantChoice = input("> ")
user_input_lower = simulantChoice.lower()

if (simulantChoice == "scarper"):
    print("")
    print("You fire up the boosters and leg it ")
    print("Unfortunately Starbug is slower than an arthritic hamster")
    print("The simulants laugh and blast you to pieces")
    print("")
    print("Youre Dead!")
    quit()

elif (simulantChoice == "fight"):
    print("")
    print("You turn Starbug around and fire the guns, Direct hit to")
    print("Their engines, the simulant ship is dead in the water")
    print("Great shooting, There are no signs of life on the ship")
    print("")
    print("Do you analyse what just happened? as rimmer has suggested.")
    print("Or go and board their ship and see if anything is worth swiping?")

else:
    print("Invalid choice. Please enter scarper or fight")

# User input for the analyse choice

analyseChoice = input("> ")
user_input_lower = analyseChoice.lower()

if (analyseChoice == "analyse"):
    print("")
    print("You sit down with rimmer and analyse the situation")
    print("After days of analysing and organ music playing in the background")
    print("You decide it's to much and throw yourself in space withour a suit")
    print("")
    print("You're Dead!")
    quit()

elif (analyseChoice == "board"):
    print("")
    print("You board the simulant ship and start looking for goods")
    print("The cat finds a box with rejuvenating shower written on it")
    print("You all agree he can keep it, just to keep him quiet")
    print("Lister says he'll build it, he took a class once at art college")
    print("")
    print("Do you let lister build it or kryten?")

else:
    print("Invalid choice. Please enter analyse or board")

# User input for the shower choice

showerChoice = input("> ")
user_input_lower = showerChoice.lower()

if (showerChoice == "kryten"):
    print("")
    print("Kryten unpacks the shower and starts building it")
    print("After two hours hes finished and tests the device")
    print("A huge explosion happens killing everyone on board")
    print("It seems Lister had swapped out krytens, Head to spare head two")
    print("The smeeeeg heeeeead")
    print("")
    print("You're Dead!")
    quit()

elif (showerChoice == "lister"):
    print("")
    print("Lister starts building the shower")
    print("He builds it in an hour, which is very suspicious, ")
    print("It seems hes used abit of the luck virus")
    print("")
    print("When he tests it, the whole crew are teleported to what looks like")
    print("Earth, You soon realise you are on a backwards planet, You know ")
    print("This as the cat has just been to the toilet, yikes!")
    print("")
    print("The remote is dead and needs batteries")
    print("Do you go forwards or backwards")

else:
    print("Invalid choice. Please enter kryten or lister")

# User input for the lemons choice

lemonsChoice = input("> ")
user_input_lower = lemonsChoice.lower()

if (lemonsChoice == "forwards"):
    print("")
    print("Oh smeg, it's a backwards planet.")
    print("You walk backwards straight off a cliff")
    print("")
    print("You're Dead!")
    quit()

elif (lemonsChoice == "backwards"):
    print("")
    print("You walk forwards straight to the nearest village")
    print("Its a Gelf village!. They unfortunately don't have a nine volt")
    print("Battery for the remote but, look, they do have lemons and ")
    print("Copper. Kryten said We could make a battery")
    print("")
    print("The Gelfs are happy to trade, but they want Rimmer in exchange")
    print("")
    print("Do you exchange Rimmer for the lemons and copper?")

else:
    print("Invalid choice. Please enter forwards or backwards")

# User input for the lemons choice

tradeChoice = input("> ")
user_input_lower = tradeChoice.lower()

if (tradeChoice == "yes"):
    print("")
    print("Double smeg, it's a backwards planet.")
    print("The Gelfs take offence because you won't trade")
    print("Plus Lister said they looked like his gran")
    print("")
    print("So they shoot you all, You're Dead!")
    quit()

elif (tradeChoice == "no"):
    print("")
    print("Excellent you've got the lemons & copper, plus")
    print("You've got rid of Rimmer, What a great day")
    print("")
    print("Kryten makes the battery and hits the return key, everyone is")
    print("Teleport but wait, this isn't Starbug, its Red Dwarf")
    print("")
    print("Congratulations!")
    print("You've made it Back to Red Dwarf")

else:
    print("Invalid choice. Please enter yes or no")
