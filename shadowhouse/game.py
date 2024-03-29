"""Game logic module for Shadow House.

Supports all functions to play Shadow House, from the logic
necessary to support different narrative scenarios to mundane tasks such
as updating player's score and quitting.

Suggested improvements for next version:
* Make all commands case insensitive.
* Create a Player class that would hold player's name and running score,
  possibly even state data rather having that in the Room classes.
* Redesign game top-to-bottom to support a Map-Scene engine
* use 'from rooms.Rooms import Basement, DiningRoom, ...' to make code
  less wordy.
"""

import sys
import os
import random
from textwrap import dedent
from time import sleep
from datetime import datetime

# Module containing descriptions of each room player enters
import rooms

# --------------------------------GLOBAL----------------------------------

'''Accumulated points'''
POINTS = 0

'''Best possible score'''
TOTAL = 119

'''Dictionary to keep track of which points players has garnered'''
DICT_SCORE = {
        'base_read': False,
        'base_upstairs':False,
        'din_look': False,
        'din_talk1': False,
        'din_talk2': False,
        'din_talk3': False,
        'din_left': False,
        'din_touch': False,
        'din_down': False,
        'kit_look': False,
        'kit_pot1': False,
        'kit_pot2': False,
        'kit_pot3': False,
        'kit_code': False,
        'kit_open': False,
        'gard_look': False,
        'gard_well': False,
        'gard_down': False,
        'gard_south': False,
        'well_fall': False,
        'well_down': False
        }

'''Player's name. Anonymous if none specified.'''
WINNER_NAME = 'Anonymous'

'''End credits'''
CREDITS = '''
***CREDITS***
Story, writing and coding by Alex Dunne.
Apologies to DFW and DL for using their big ideas for my very small ones.
Thanks to Zed Shaw for providing the impetus and the basics that made
this game possible.
Special thanks to LK for additional dialogue concepts ;-).

Copyright © Alex Dunne, 2018-2020. All rights reserved.
'''

# ----------------------------HELPER FUNCTIONS-----------------------------

def show_hints(hints):
    """Prints allowable commands for a given room.

    Args:
        hints: String list of possible commands.
    """

    print("\nPossible commands")
    print("------------------")

    for item in hints:
        print(item)


def add_points(num, point_id=None):
    """Adds points to score while ensuring players aren't 'double-dipping'
    (i.e. repeating the same action to increase score)

    Args:
        num: Integer number of points to be added.
        point_id: String the identifies part of game where player earned points
                  and any additional context.
    """

    global POINTS
    global DICT_SCORE

    # If no id specified, just add the points.
    # Otherwise, change id from False to True for first-time scoring.
    # If already True, then player has already earned points. Do nothing.
    if point_id is None:
        POINTS += num
    elif DICT_SCORE[point_id] == False:
        DICT_SCORE[point_id] = True
        POINTS += num
    else:
        pass


def show_score():
    """Prints points accumulated thus far."""

    print(f"\nScore: {POINTS} out of {TOTAL} points")


def bad_input(player_input):
    """Prints feedback when player enters illegal commands or nothing.

    Args:
        player_input: String representing player's command.

    """
    if len(player_input.strip()) == 0:
        print("\nC'mon. Don't be a dweeb. Write something.")
    else:
        s_words = '''
        I do not understand many words and can only handle one space between
        the words that I do. Type \'Hint\' if you\'re getting nowhere.'''
        print(dedent(s_words))


def dead(why):
    """Prints why user died and exits game.

    Args:
        why: String describing cause of death.
    """

    print(why)
    print("\nThanks for playing! Better luck next time :-p.\n")

    quit_game()


def quit_game():
    """Exits game."""

    print("") # For aesthetic purposes

    sys.exit()


def ascii_animation():
    """Prints animation of player 'falling'"""

    # Number of tabs generally required to center animation
    c = 4

    # Animation loop parameters (fps: frames per second)
    fps = 18
    sec = 5
    frames = int(sec * fps)

    # Player falling down!
    for x in range(frames):

        if x % 2 == 0:
            print('\t' * c +"?" + "\n" * 3)

        print('\t' * c + '  /00\\')
        print('\t' * c + '   ||')
        if x % 3 == 0:
            print('\t' * c + ' >====v')
        if x % 3 == 1:
            print('\t' * c + ' v====<')
        if x % 3 == 2:
            print('\t' * c + ' >====<')
        print('\t' * c + '   ||')
        print('\t' * c + '   /\\')

        if x % 2 != 0:
            print("\n" * 3 + '\t' * c + "\t?")

        print('\n' * 5)

        # Period of a single frame
        sleep(1 / fps)

    # Dot at bottom of screen when player stops falling
    print('\n' * 15)
    print('\t' * (c) + '   ∙')

    # Pause for three seconds before carrying on with the game (suspense!)
    sleep(3)


def _get_dir():
    """Gets absolute path of the directory where module exists.

    Returns:
        dir: String of the unique ('canonical') absolute path of the directory
             containing the module (i.e. no symbolic links in path).
    """

    # Get the current working directory in Terminal
    # when you try to launch the module as a script
    cwd = os.getcwd()

    # Get the name of the directory where the module exists
    module_dir = os.path.dirname(__file__)

    # Intelligently cocantenate the two
    joinedpath = os.path.join(cwd, module_dir)

    # Get rid of any possible symbolic links found along and return the
    # absolute path
    return os.path.realpath(joinedpath)


def write_winner_to_file():
    """Writes date, player's name and score to file."""

    global WINNER_NAME

    # Truncate any name to a max of 15 characters.
    if len(WINNER_NAME) > 15:
        WINNER_NAME = WINNER_NAME[:15]

    # Add spaces to name to make it 15 characters long if shorter.
    elif len(WINNER_NAME) <= 15:
        WINNER_NAME = WINNER_NAME + ' ' * (15-len(WINNER_NAME))

    # Fetch current date and time; format as desired using format codes.
    right_now = datetime.now().strftime("%Y-%m-%d, %I:%M %p")

    # Format how to present the player's score
    s_score = f"{POINTS} out of {TOTAL} points"

    # Combine all parts together to form single string record
    rec = WINNER_NAME + '\t'*3 + right_now + '\t'*3 + s_score + "\n"

    try:
        # Get directory where this file exists
        absdir = _get_dir()

        # Intelligently concatenate the directory and the input file name
        # together
        full_filename = os.path.join(absdir, "scores.dat")

        with open(full_filename, 'a') as fin:
            fin.write(rec +"\n")

    except OSError as err:
        print("OSError: {0}".format(err), file=sys.stderr)
        print("Score.dat not loaded. Exiting program.", file=sys.stderr)
        sys.exit()


def show_credits():
    """Prints end credits."""
    print(dedent(CREDITS))


def common_input(choice, hints=None):
    """Groups common commands that are required when player enters a room.

    Args:
        choice: String representing command.
        hints: List of choices players can enter in a room.
    """

    if choice in ["Quit", "quit", "quit game", "Quit game"]:
        quit_game()
    elif choice in ["Score", "score"]:
        show_score()
    elif choice in ["Hint", "hint"]:
        show_hints(hints)
    else:
        bad_input(choice)


# ----------------------------STORY FUNCTIONS------------------------------

def enter_basement():
    """Handles event loop and game state for basement."""

    hints = rooms.Basement.get_choices()

    print(dedent(rooms.Basement.description))

    while True:
        choice = input("\n> ")
        choice = choice.strip()

        if choice == "Watch TV":
            dead(dedent(rooms.Basement.choices.get(choice)))

        elif choice == "Squash spider":
            dead(dedent(rooms.Basement.choices.get(choice)))

        elif choice == "Go upstairs":
            if not rooms.Basement.notebook_read:
                dead(dedent(rooms.Basement.descr_banana))
            else:
                print(dedent(rooms.Basement.choices.get(choice)))
                add_points(5, 'base_upstairs')
                enter_diningroom()

        elif choice == "Read notebook":
            print(dedent(rooms.Basement.choices.get(choice)))
            rooms.Basement.notebook_read = True
            add_points(10, 'base_read')

        elif choice == "Look around":
            print(dedent(rooms.Basement.choices.get(choice)))

        else:
            common_input(choice, hints)


def enter_diningroom():
    """Handles event loop and game state for dining room."""

    print(rooms.DiningRoom.description)

    hints = rooms.DiningRoom.get_choices()

    while True:
        choice = input("\n> ")

        choice = choice.strip()

        if choice == "Look around":
            print(dedent(rooms.DiningRoom.choices.get(choice)))
            rooms.DiningRoom.look_around = True
            add_points(10, 'din_look')

        elif choice == "Eat veggie straws":
            dead(dedent(rooms.DiningRoom.choices.get(choice)))

        elif choice == "Touch mannequin":
            print(rooms.DiningRoom.choices.get(choice))
            add_points(1, 'din_touch')

        elif choice == "Talk to mannequin":

            # Can't talk to mannequin unless player has seen it first
            if rooms.DiningRoom.look_around:

                if not rooms.DiningRoom.talk_once:
                    rooms.DiningRoom.talk_once = True
                    print(dedent(rooms.DiningRoom.choices.get(choice)))
                    add_points(5, 'din_talk1')

                elif not rooms.DiningRoom.talk_twice:
                    rooms.DiningRoom.talk_twice = True

                    rooms.DiningRoom.passcode = [
                        random.randint(0, 9),
                        random.randint(0, 9),
                        random.randint(0, 9),
                        random.randint(0, 9)
                        ]

                    descr_passcode = rooms.DiningRoom.descr_passcode
                    str_passcode = rooms.DiningRoom.stringify_passcode()

                    print(f'\n"{descr_passcode} {str_passcode}"')

                    add_points(10, 'din_talk2')

                else:
                    print(dedent(rooms.DiningRoom.descr_toomuch))
                    add_points(1, 'din_talk3')

            else:
                print(rooms.DiningRoom.descr_nomannequin)

        elif choice == "Go left":
            if rooms.DiningRoom.look_around:
                add_points(5, 'din_left')
                enter_kitchen()

            else:
                print(dedent(rooms.DiningRoom.descr_slowdown))

        elif choice == "Go downstairs":
            print(rooms.DiningRoom.choices.get(choice))
            add_points(1, 'din_down')

        else:
            common_input(choice, hints)


def enter_kitchen():
    """Handles event loop and game state for kitchen."""

    print(rooms.Kitchen.description)

    hints = rooms.Kitchen.get_choices()

    #choices
    while True:
        choice = input("\n> ")
        choice = choice.strip()

        if choice == "Look around":
            print(dedent(rooms.Kitchen.choices.get(choice)))
            add_points(10, 'kit_look')

        elif choice == "Open door":
            print(rooms.Kitchen.choices.get(choice))
            add_points(1, 'kit_open')

        elif choice == "Pick up potato":
            if rooms.Kitchen.potatoes < 3:
                rooms.Kitchen.potatoes += 1
                print("")
                print(rooms.Kitchen.potatoes, "potato.")
                add_points(1, 'kit_pot' + str(rooms.Kitchen.potatoes))
            else:
                print(dedent(rooms.Kitchen.descr_chill))

        elif choice == "Drop potatoes":
            if rooms.Kitchen.potatoes != 0:
                print("\nOkay.")
                add_points(rooms.Kitchen.potatoes * (-1))
                rooms.Kitchen.potatoes = 0
            elif rooms.Kitchen.potatoes == 0:
                print(rooms.Kitchen.descr_nopotatoes)

        elif choice == "Kiss potatoes":
            dead(dedent(rooms.Kitchen.descr_kiss))

        elif choice == "Enter pass-code":

            try:
                # Compare with passcode mannequin gave
                if rooms.DiningRoom.passcode != []:
                    n1 = int(input("\nEnter first digit: "))
                    n2 = int(input("Enter second digit: "))
                    n3 = int(input("Enter third digit: "))
                    n4 = int(input("Enter fourth digit: "))

                    pc1 = int(rooms.DiningRoom.passcode[0])
                    pc2 = int(rooms.DiningRoom.passcode[1])
                    pc3 = int(rooms.DiningRoom.passcode[2])
                    pc4 = int(rooms.DiningRoom.passcode[3])

                    correct = (n1 == pc1 and
                               n2 == pc2 and
                               n3 == pc3 and
                               n4 == pc4)

                    # Go to garden if pass-code is right and user has picked up
                    # all the potatoes
                    if correct and rooms.Kitchen.potatoes == 3:
                        print("\nThe door unlocks!")
                        add_points(10, 'kit_code')
                        enter_garden()

                    elif correct and rooms.Kitchen.potatoes != 3:
                        print(dedent(rooms.Kitchen.descr_noopen))

                    elif not correct:
                        input(dedent(rooms.Kitchen.descr_wrong))
                        dead(dedent(rooms.Kitchen.descr_explode))

                else:
                    print(dedent(rooms.Kitchen.descr_secondshot))

            except ValueError:
                print("\nWhole numbers only, nitwit!")

        elif choice == "Go right":
            enter_diningroom()

        else:
            common_input(choice, hints)


def enter_garden():
    """Handles event loop and game state for garden."""

    print(dedent(rooms.Garden.description))

    hints = rooms.Garden.get_choices()

    while True:
        choice = input("\n> ")
        choice = choice.strip()

        if choice == "Look around":
            print(dedent(rooms.Garden.choices.get(choice)))
            add_points(10, "gard_look")

        elif choice == "Follow cat":
            dead(dedent(rooms.Garden.choices.get(choice)))

        elif choice == "Look in well":
            print(dedent(rooms.Garden.choices.get(choice)))
            rooms.Garden.seen_ladder = True
            add_points(5, "gard_well")

        elif choice == "Go south":
            print(dedent(rooms.Garden.choices.get(choice)))
            add_points(1, 'gard_south')

        elif choice == "Go down ladder":
            if not rooms.Garden.seen_ladder:
                print("\nWhat ladder?")
            else:
                add_points(5, "gard_down")
                enter_well()

        else:
            common_input(choice, hints)


def enter_well():
    """Handles event loop and game state for well."""

    print(dedent(rooms.Well.description))

    while True:
        choice = input("\n> ")
        choice = choice.strip()

        if choice == "Go up ladder":
            print(dedent(rooms.Well.choices.get(choice)))
            enter_garden()

        elif choice == "Go down ladder":
            print(dedent(rooms.Well.choices.get(choice)))
            add_points(1, 'well_down')

        elif choice == "Let go of ladder":
            add_points(25, 'well_fall')
            win()

        # Don't use common input here For narrative reasons, players
        # are deliberately not told Hints nor is their input invalidated.
        elif choice in ["Score", "score"]:
            show_score()
        elif choice in ["Hint", "hint"]:
            print("\nFizzzzzzzzzzzzzzzzzzzzzzzzz....")
        elif choice in ["Quit", "quit"]:
            quit_game()
        else:
            pass


def win():
    """Handles final scene of game."""

    # Text-based animation of player 'falling'
    ascii_animation()

    print(dedent(rooms.Win.description))

    end_game()


def end_game():
    """Handles end of program contingent on player winning the game:
    displays final score and writes it to file; quits program.
    """
    global WINNER_NAME

    show_score()

    WINNER_NAME = input("\nWhat's your name? ")

    s_goodbye = f'''
    Thanks, {WINNER_NAME}, for playing SHADOW HOUSE. Hope to see you again sometime :-D!
    '''
    print(dedent(s_goodbye))

    write_winner_to_file()
    show_credits()
    quit_game()
