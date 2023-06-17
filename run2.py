

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
        print("Or go and board their ship and see if anything is worth swiping?")


def sit_or_bridge():
    user_input = get_user_input(['sit back', 'bridge'])
    if (user_input == "sit back"):
        print("")
        print("You sit back put your feet up and turn the game on")
        print("You grab the beer and just as you're about to open it,")
        print("It turns input a polymorph and sucks all your emotion out")
        print("")
        print("The cries of Dwayne Dibbly! are heard being shouted")
        print("Followed by the sound of a blaster")
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
        fight_or_scarper()


# Start of the game
def start_game_text():
    print("Are you ready to play Back To Red Dwarf?")
    print("")
    print("You've been woken up by alarm bells and sirens going off.")
    print("You're in your quarters of a spaceship called Starbug.")
    print("")
    print("Do you want to go to the bridge to see what the smeg is going on?")
    print("Or sit back relax and watch some zero g football with a beer?")
    sit_or_bridge()


if __name__=="__main__":
      start_game_text()