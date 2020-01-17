#!/usr/bin/env python3

"""SHADOW_HOUSE_BETA.PY (VERSION 3, BETA 01)

A short text game.

The game requires Python 3.6 or 3.7 to run. Other lower 'three' have not
been tested. It will not work on Python 2.7.x without some gerry-mandering to
the code.

You can feed the game file directly to the interpreter as so.

    $ python3 shadow_house_beta.py

Alternatively, you can run the bash script "shadow_house." It's not really
different except the font is bold white on a black background and everything
on your console is 'cleared' when the game is launched. I recommend making the
bash file into an executable first.

    $ chmod +x shadow_house     #make into executable
    $ ./shadow_house            #run game

Author:
    Alex Dunne

Last updated:
    September 15, 2018

Todo:
    - download python3 to L's computer
    - readme.txt: how to play how to see scores
    - easy way for player to see score list
    - instal and test on L's computer
    - upload latest version to Pythonanyhere


Done/Handled:
    - create account at pythonanywhere.com and test
    - create executable chmod +x
    - edit shell script to present game the way you want it.
        script must be launched from console
    - start text really centered??
    - beta test with L
    - fix potato bug: pick up potatoes; leave kitchen; return to kitchen;
      no potatoes!!

Unable/did not do:


Credits:
--------
Story, writing and coding by Alex Dunne.
Apologies to DFW and DL for using their big ideas for my very small ones.
Special thanks to LK for additional dialogue concepts ;-).

Copyright © Alex Dunne, 2018. All rights reserved.
"""

import scenes

def run_game():
    '''Start running game. Handle CTRL-C exception from user in case she
    quits game this way (avoids printing ugly stack trace)'''

    print("")
    print("\t      ****************SHADOW HOUSE****************")
    print("\t          There's no place like home, except...")

    print("\n\t         Type 'Score' to show, um, your score.")
    print("\t       Type 'Quit' to leave the game at any time.")
    print("\t      ********************************************")

    try:
        scenes.basement()
    except KeyboardInterrupt: #user kills process with Ctrl-C
        print("\n")
        exit(0)



"""----------------------------------MAIN------------------------------------"""
if __name__ == "__main__":
    run_game()
