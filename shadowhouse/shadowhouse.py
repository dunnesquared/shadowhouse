#!/usr/bin/env python3

"""Main script to start playing Shadow House game"""

import sys

import game


def print_intro():
    """Prints intro text of game."""
    print("")
    print("\t      ****************SHADOW HOUSE****************")
    print("\t          There's no place like home, except...")

    print("\n\t         Type 'Score' to show, um, your score.")
    print("\t       Type 'Quit' to leave the game at any time.")
    print("\t      ********************************************")


def run_game():
    """Starts game. Handles CTRL-C exception from users in case they
    quits game this way."""

    try:
        print_intro()
        game.enter_basement()
    except KeyboardInterrupt: # Player kills process with Ctrl-C
        print("\n")
        sys.exit()


if __name__ == "__main__":
    run_game()
