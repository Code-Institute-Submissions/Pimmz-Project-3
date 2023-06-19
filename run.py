# function to get user input but only if it matches the valid option

def get_user_input(valid_options):
    input_is_valid = False
    print(f"{valid_options} ? ")
    while input_is_valid is False:
        user_choice = input("> ")
        user_input_lower = user_choice.lower()
        if user_input_lower in valid_options:
            input_is_valid = True
        else:
            print('Invalid input, please enter again')
    return user_input_lower


# User input for the first choice

def sit_back_or_bridge():
    user_input = get_user_input(['sit back', 'bridge'])
    if (user_input == "sit back"):
        print("")
        print("You sit back put your feet up and turn the game on")
        print("You grab the beer and just as you're about to open it,")
        print("It turns into a Polymorph and sucks all your emotion out")
        print("")
        print("The cries of Dwayne Dibbly! are heard being shouted")
        print("Followed by the sound of a blaster")
        print("")
        print("You're dead!")
        quit()

    elif (user_input == "bridge"):
        print("")
        print("You run to the bridge and ask what the smeg is going on?")
        print("Kryten replies, were being attacked by rouge simulants")
        print("")
        print("We have two choices either fight or scarper")
        print("What would you like to do?")
        print("")


# User input for the simulant choice

def fight_or_scarper():
    user_input = get_user_input(['fight', 'scarper'])
    if (user_input == "scarper"):
        print("")
        print("You fire up the boosters and leg it ")
        print("Unfortunately Starbug is slower than an arthritic hamster")
        print("The simulants laugh and blast you to pieces")
        print("")
        print("Youre Dead!")
        quit()

    elif (user_input == "fight"):
        print("")
        print("You turn Starbug around and fire the guns, Direct hit to")
        print("Their engines, the simulant ship is dead in the water")
        print("Great shooting, There are no signs of life on the ship")
        print("")
        print("Do you analyse what just happened? as rimmer has suggested.")
        print("Or go and board their ship to see if anything is worth swiping")


# User input for the analyse choice

def analyse_or_board():
    user_input = get_user_input(['analyse', 'board'])
    if (user_input == "analyse"):
        print("")
        print("You sit down with rimmer and analyse the situation, after")
        print("Days of analysing and organ music playing in the background")
        print("You decide you cant take it any more and throw yourself")
        print("In space without a suit")
        print("")
        print("You're Dead!")
        quit()

    elif (user_input == "board"):
        print("")
        print("You board the simulant ship and start looking for goods")
        print("The cat finds a box with rejuvenating shower written on it")
        print("You all agree he can keep it, just to keep him quiet")
        print("Lister says hell build it, he took a class once at art college")
        print("")
        print("Do you let lister build it or kryten?")


# User input for the shower choice

def kryten_or_lister():
    user_input = get_user_input(['kryten', 'lister'])
    if (user_input == "kryten"):
        print("")
        print("Kryten unpacks the shower and starts building it")
        print("After two hours hes finished and tests the device")
        print("A huge explosion happens killing everyone on board")
        print("It seems Lister had swapped out krytens head to spare head two")
        print("The smeeeeg heeeeead")
        print("")
        print("You're Dead!")
        quit()

    elif (user_input == "lister"):
        print("")
        print("Lister starts building the shower")
        print("He builds it in an hour, which is very suspicious, ")
        print("It seems hes used abit of the luck virus")
        print("")
        print("When he tests it, the whole crew are teleported to what looks")
        print("Like Earth You soon realise you are on a backwards planet, You")
        print("Know this as the cat has just been to the toilet, yikes!")
        print("")
        print("The remote is dead and needs batteries")
        print("Do you go forwards or backwards")


# User input for the lemons choice

def forwards_or_backwards():
    user_input = get_user_input(['forwards', 'backwards'])
    if (user_input == "forwards"):
        print("")
        print("Oh smeg, it's a backwards planet.")
        print("You walk backwards straight off a cliff")
        print("")
        print("You're Dead!")
        quit()

    elif (user_input == "backwards"):
        print("")
        print("You walk forwards straight to the nearest village")
        print("Its a Gelf village!. They unfortunately don't have a nine volt")
        print("Battery for the remote but, look, they do have lemons and ")
        print("Copper. Kryten said We could make a battery")
        print("")
        print("The Gelfs are happy to trade, but they want Rimmer in exchange")
        print("")
        print("Do you exchange Rimmer for the lemons and copper?")


# User input for the lemons choice

def yes_or_no():
    user_input = get_user_input(['yes', 'no'])

    if (user_input == "yes"):
        print("")
        print("Double smeg, it's a backwards planet.")
        print("The Gelfs take offence because you won't trade")
        print("Plus Lister said they looked like his gran")
        print("")
        print("So they shoot you all, You're Dead!")
        quit()

    elif (user_input == "no"):
        print("")
        print("Excellent you've got the lemons & copper, plus")
        print("You've got rid of Rimmer, What a great day")
        print("")
        print("Kryten makes the battery and hits the return key, everyone is")
        print("Teleport but wait, this isn't Starbug, its Red Dwarf")
        print("")
        print("Congratulations!")
        print("You've made it Back to Red Dwarf")


# Start of the game

def start_game_text():
    print("Are you ready to play Back To Red Dwarf?")
    print("")
    print("You've been woken up by alarm bells and sirens going off.")
    print("You're in your quarters of a spaceship called Starbug.")
    print("")
    print("Do you want to go to the bridge to see what the smeg is going on?")
    print("Or sit back relax and watch some zero g football with a beer?")
    sit_back_or_bridge()


if __name__ == "__main__":
    start_game_text()
