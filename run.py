import gspread
from google.oauth2.service_account import Credentials
import json

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEETS = GSPREAD_CLIENT.open('Back_to_Red_Dwarf')

pack = SHEETS.worksheet('pack')

"""
function to get user input but only if it matches the valid
option else it displays a invalid input
"""


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


# User input to find out what is going on

def sit_back_or_bridge():
    user_input = get_user_input(['sit back', 'bridge'])
    if (user_input == "sit back"):
        print("")
        print("You sit back put your feet up and turn the game on\n")
        print("You grab the beer and just as you're about to open it,")
        print("It turns into a Polymorph and sucks all your emotion out")
        print("")
        print("The cries of Dwayne Dibbly! are heard being shouted")
        print("Followed by the sound of a blaster\n")
        print("You're dead!")
        quit()

    elif (user_input == "bridge"):
        print("")
        print("You run to the bridge and ask what the smeg is going on?")
        print("Kryten replies, were being attacked by rouge simulants\n")
        print("Would you like to fight or scarper\n")
        fight_or_scarper()


"""
User input for the simulant choice to decide if you want to fight
the simulants.
"""


def fight_or_scarper():
    user_input = get_user_input(['fight', 'scarper'])
    if (user_input == "scarper"):
        print("")
        print("You fire up the boosters and leg it\n")
        print("Unfortunately Starbug is slower than an arthritic hamster")
        print("The simulants laugh and blast you to pieces\n")
        print("Youre Dead!")
        quit()

    elif (user_input == "fight"):
        print("")
        print("You turn Starbug around and fire the guns. Direct hit to")
        print("Their engines. The simulant ship is dead in the water.")
        print("Great shooting! There are no signs of life on the ship\n")
        guitar_or_not()


# Guitar reward for completing the game linked to google docs

def guitar_or_not():
    reward = input("Do you want listers Guitar as a reward? (yes/no):")
    if reward == "yes":
        print("Adding to your backpack...\n")
        pack_worksheet = SHEETS.worksheet("pack")
        data = ["Guitar"]
        pack_worksheet.append_row(data)
        print("Added to your backpack successfully\n")
        print("Do you want to analyse what happened, as Rimmer has suggested")
        print("Or board the ship to look for anything worth swiping?\n")
        analyse_or_board()

    elif reward == "no":
        print("")
        print("You have left the Guitar behind\n")
        print("Do you want to analyse what happened, as Rimmer has suggested")
        print("Or board the ship to look for anything worth swiping?\n")
        analyse_or_board()


# User input for the analyse choice after the simulant fight

def analyse_or_board():
    user_input = get_user_input(['analyse', 'board'])
    if (user_input == "analyse"):
        print("")
        print("You sit down with Rimmer and analyse the situation, after")
        print("Days of analysing and organ music playing in the background")
        print("You decide you can't take it any more and throw yourself")
        print("In space without a spacesuit\n")
        print("You're Dead!")
        quit()

    elif (user_input == "board"):
        print("")
        print("You board the simulant ship and start looking for goods\n")
        print("The cat finds a box with rejuvenating shower written on it")
        print("You all agree he can keep it, just to keep him quiet.\n")
        hair_or_not()


# Hairbrush reward for completing the game linked to google docs

def hair_or_not():
    reward = input("He also found a hairbrush do you pick it up? (yes/no):")
    if reward == "yes":
        print("Adding to your backpack...\n")
        pack_worksheet = SHEETS.worksheet("pack")
        data = ["Hairbrush"]
        pack_worksheet.append_row(data)
        print("Added to your backpack successfully\n")
        print("Lister wants to build the shower as he took a class once at")
        print("Art College do you let lister build it or Kryten?\n")
        kryten_or_lister()

    elif reward == "no":
        print("")
        print("You have left the hairbrush behind\n")
        print("Lister wants to build the shower as he took a class once at")
        print("Art College, do you let lister build it or Kryten?\n")
        kryten_or_lister()


# User input for the shower choice to see who builds it

def kryten_or_lister():
    user_input = get_user_input(['kryten', 'lister'])
    if (user_input == "kryten"):
        print("")
        print("Kryten unpacks the shower and starts building it")
        print("After two hours he's finished and tests the device\n")
        print("A huge explosion happens killing everyone on board")
        print("It seems Lister had swapped out Krytens head to spare head two")
        print("The smeeeeg heeeeead\n")
        print("You're Dead!")
        quit()

    elif (user_input == "lister"):
        print("")
        print("Lister starts building the shower, he builds it in an hour")
        print("Which is very strange,It seems he used a bit of the luck virus")
        print("")
        print("When he tests it, the whole crew are teleported to what looks")
        print("Like Earth you soon realise you are on a backwards planet, you")
        print("Know this as the cat has just been to the toilet, yikes!\n")
        print("The remote is dead and needs batteries\n")
        print("Do you go forwards or backwards?\n")
        forwards_or_backwards()


# User input for the forwards or backwards input to decide on the gelf trade

def forwards_or_backwards():
    user_input = get_user_input(['forwards', 'backwards'])
    if (user_input == "forwards"):
        print("")
        print("Oh smeg, it's a backwards planet.\n")
        print("You walk backwards straight off a cliff\n")
        print("You're Dead!")
        quit()

    elif (user_input == "backwards"):
        print("")
        print("You walk forwards straight to the nearest village\n")
        print("Its a Gelf village!. They unfortunately don't have a nine volt")
        print("Battery for the remote but look, they do have lemons and ")
        print("Copper. Kryten said we could make a battery.\n")
        print("The Gelfs are happy to trade, but they want Rimmer in exchange")
        print("")
        print("Do you exchange Rimmer for the lemons and copper?\n")
        yes_or_no()


# User input for the lemons choice to decide which way to go

def yes_or_no():
    user_input = get_user_input(['yes', 'no'])

    if (user_input == "yes"):
        print("")
        print("Double smeg, it's a backwards planet.\n")
        print("The Gelfs take offence because you won't trade")
        print("Plus Lister said they looked like his gran\n")
        print("So they shoot you all, You're Dead!")
        quit()

    elif (user_input == "no"):
        print("")
        print("Excellent you've got the lemons & copper, plus")
        print("You've got rid of Rimmer, What a great day!\n")
        print("Kryten makes the battery and hits the return key, everyone is")
        print("Teleported, but wait, this isn't Starbug, its Red Dwarf\n")
        print("Congratulations!\n")
        print("You've made it Back to Red Dwarf\n")
        curry_or_not()


# Curry reward for completing the game linked to google docs

def curry_or_not():
    reward = input("Do you fancy a celebratery curry? (yes/no):")
    if reward == "yes":
        print("Adding to your backpack...\n")
        pack_worksheet = SHEETS.worksheet("pack")
        data = ["Curry"]
        pack_worksheet.append_row(data)
        print("Added to your backpack successfully\n")
        print("Game Over")

    elif reward == "no":
        print("No curry for you tonight then!\n")
        print("Game Over")


# Start of the game

def start_game_text():
    print("Are you ready to play Back To Red Dwarf?\n")
    print("You've been woken up by alarm bells and sirens going off.")
    print("You're in your quarters of a spaceship called Starbug.\n")
    print("Do you want to go to the bridge to see what the smeg is going on?")
    print("Or sit back relax and watch some zero g football with a beer?\n")
    sit_back_or_bridge()


if __name__ == "__main__":
    start_game_text()
