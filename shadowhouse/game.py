import sys
from random import randint
from textwrap import dedent
from time import sleep
from datetime import datetime

import rooms


"""---------------------------------GLOBAL-----------------------------------"""

'''List of numbers to open garden door once defined'''
PASS_CODE = None

'''Accumulated points'''
POINTS = 0

'''Best possible score'''
TOTAL = 119

'''Dictionary to keep track of which points players has garnered'''
DICT_SCORE = {
            'base_read':False,
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
            'gard_south':False,
            'well_fall': False,
            'well_down': False
            }

'''Player's name'''
WINNER_NAME = 'Anonymous'

'''Number of potatos picked up in the kitchen; needs to be global for the case
where the player picks up the potatoes, goes back to dining room, then returns
to kitchen'''
NUM_POTATO = 0

"""----------------------------HELPER FUNCTIONS------------------------------"""
#Functions which if they did nothing would not really hinder game play, but
#would make it highly awkward

def show_hints(hints):
    '''Show possible commands for a given room'''

    print("\nPossible commands")
    print("------------------")
    for item in hints:
        print(item)


def add_points(num, id = None):
    '''Add points to score while ensuring players aren't double-dipping'''

    global POINTS
    global DICT_SCORE

    #if no id specified, just add the points
    #Otherwise, set id from False to True (first time scoring)
    #If already True, do nothing
    if id == None:
        POINTS += num
    elif DICT_SCORE[id] == False:
        DICT_SCORE[id] = True
        POINTS += num
    else:
        pass


def show_score():
    '''Show points accumulated thus far.'''
    global POINTS, TOTAL
    print(f"\nScore: {POINTS} out of {TOTAL} points")


def bad_input(s):
    '''Handle unknown words and no input'''
    if len(s.strip()) == 0:
        print("\nC'mon. Don't be a dweeb. Write something.")
    else:
        s_words = '''
        I do not understand many words and can only handle one space between
        the words that I do. Type \'Hint\' if you\'re getting nowhere.'''
        print(dedent(s_words))


def dead(why):
    '''Print why user died and exits game'''
    print(why)
    print("\nThanks for playing! Better luck next time :-p.\n")

    #Zero not necessary, but kept in make clear exiting here is normal
    quit()


def quit():
    '''Exits game.'''
    print("")
    sys.exit()


def ascii_animation():
    '''Trivial animation of player "falling" '''

    #Number of tabs generally required to center animation
    c = 4

    #Animation loop parameters (fps: frames per second)
    fps = 18
    sec = 5
    frames = int(sec * fps)

    #Falling down!
    for x in range(frames):

        if x % 2 == 0:
            print('\t'*c +"?" + "\n"*3)

        print('\t'*c +'  /00\\')
        print('\t'*c +'   ||')
        if x % 3 == 0:
            print('\t'*c +' >====v')
        if x % 3 == 1:
            print('\t'*c +' v====<')
        if x % 3 == 2:
            print('\t'*c +' >====<')
        print('\t'*c +'   ||')
        print('\t'*c +'   /\\')

        if x % 2 != 0:
            print("\n"*3 + '\t'*c + "\t?")

        print('\n'*5)

        #period of a single frame
        sleep(1/fps)


    #side = " ♘  ☯︎  ♞"
    #for x in range(int(len(side)*0.5)):
    #    print('\t'*(c) + side)

    #Dot
    print('\n'*15)
    print('\t'*(c) + '   ∙' )

    #Pause for three seconds
    sleep(3)


def write_winner_to_file():
    '''Write date, player's name and score to file'''

    global WINNER_NAME
    #Truncate any name to a max of 15 characters
    if len(WINNER_NAME) > 15:
        WINNER_NAME = WINNER_NAME[:15]
    #Add spaces to name to make it 15 characters long
    elif len(WINNER_NAME) <= 15:
        WINNER_NAME = WINNER_NAME + ' '*(15-len(WINNER_NAME))


    #Fetch current date and time; format as desired using format codes
    #right_now = datetime.now().strftime("%a, %b %d, %Y, %I:%M %p")
    right_now = datetime.now().strftime("%Y-%m-%d, %I:%M %p")

    #Format how to present the player's score
    s_score = f"{POINTS} out of {TOTAL} points"

    #Combine all parts together to form single string record
    rec = WINNER_NAME + '\t'*3 + right_now + '\t'*3 + s_score + "\n"

    #Put file in append mode
    file_handler = open("data/scores.txt", 'a')

    file_handler.write(rec +"\n")

    file_handler.close()


def credits():
    '''End credits'''
    s_credits = '''
    ***CREDITS***
    Story, writing and coding by Alex Dunne.
    Apologies to DFW and DL for using their big ideas for my very small ones.
    Special thanks to LK for additional dialogue concepts ;-).

    Copyright © Alex Dunne, 2018. All rights reserved.
    '''
    print(dedent(s_credits))


"""----------------------------STORY FUNCTIONS------------------------------"""
def enter_basement():
    '''Basement Room'''
    basement = rooms.Basement()
    hints = rooms.Basement.get_choices()

    # Use dedent to remove unseemly indentations in the above long string
    print(dedent(rooms.Basement.description))

    # Get input
    while(True):
        choice = input("\n> ")
        choice = choice.strip()

        if choice == "Quit" or choice == "quit": quit()

        if choice == "Watch TV":
            dead(dedent(rooms.Basement.choices.get(choice)))
        elif choice == "Squash spider":
            dead(dedent(rooms.Basement.choices.get(choice)))
        elif choice == "Go upstairs":
            if basement.notebook_read == False:
                dead(dedent(rooms.Basement.descr_banana))
            else:
                print(dedent(rooms.Basement.choices.get(choice)))
                add_points(5, 'base_upstairs')
                enter_diningroom()
        elif choice == "Read notebook":
            print(dedent(rooms.Basement.choices.get(choice)))
            basement.notebook_read = True
            add_points(10, 'base_read')
        elif choice == "Look around":
            print(dedent(rooms.Basement.choices.get(choice)))
        elif choice == "Score" or choice == "score": show_score()
        elif choice == "Hint" or choice == "hint": show_hints(hints)
        else: bad_input(choice)


def enter_diningroom(seen_mannequin = False):
    '''Dining room Room'''

    print("\nYou are in the dining room.")

    #initialize variables
    global PASS_CODE
    talk_once = False
    talk_twice = False
    look_around = seen_mannequin

    hints = ["Look around", "Eat veggie straws", "Touch mannequin",
    "Talk to mannequin", "Go left", "Go downstairs"]

    while(True):
        choice = input("\n> ")

        #remove leading and trailing white spaces from user's commands
        choice = choice.strip()

        #choices
        if choice=="Look around":
            s_diningroom = '''
            A naked mannequin sits at the head of an oak table. Except for the
            contours of her plastic body, she is featureless, her face as bare
            as an egg. The primer-white surface neck and chest gleam under the
            fluorescent lights of the chandelier. The Venetian blinds
            behind the mannequin are shut. The dining room has a suffocating
            aspect to it.

            A standing fan in the corner laps you with warm air.

            A bowl of veggie straws sits on the mannequin’s placemat.

            There is a doorway on the other end of the room to your left.

            Downstairs is the basement.'''
            print(dedent(s_diningroom))
            look_around = True

            add_points(10, 'din_look')

        #eat food
        elif choice == "Eat veggie straws":
            s_veggiestraws = '''
            You hesitate. Which colour to pick? Green? Orange? Yellow? How to
            decide??

            After an hour of embarrassing indecision, you timidly extract a
            spinach straw. You glance at the mannequin as you gobble it up,
            unable to shake the feeling that she is judging you.

            Although the veggie straw's airirness is pleasing, it is clearly
            under-seasoned. You take a seat at the table and continue to munch
            from the bowl, which is apparently inexhaustible. The hope that
            you’ll find a more flavourful straw is replaced by the gloomy
            realization that life is also often under-seasoned.

            You eat ad infinitum.'''
            dead(dedent(s_veggiestraws))

        elif choice == "Touch mannequin":
            print("\nShame on you! This is not that kind of game ;-).")
            add_points(1, 'din_touch')

        elif choice == "Talk to mannequin":

            if look_around == True:

                if talk_once == False:

                    talk_once = True

                    s_talkonce = '''
                    At first the mannequin ignores your blather when suddenly
                    she says:

                    "The fruits of all our labours will not be wasted on
                    soul-consuming tasks.”'''

                    print(dedent(s_talkonce))

                    add_points(5, 'din_talk1')

                elif talk_twice == False:

                    talk_twice = True

                    #Generate random pass-code each time player plays game
                    PASS_CODE = [randint(0,9), randint(0,9), randint(0,9),
                    randint(0,9)]

                    s = f"{PASS_CODE[0]} {PASS_CODE[1]} {PASS_CODE[2]} {PASS_CODE[3]}"
                    print(f"\n\"Remember these numbers: {dedent(s)}\"")

                    add_points(10, 'din_talk2')

                else:
                    s_toomuch = '''
                    The mannequin has nothing more to say to you. She's an
                    introvert -- stop draining her energy with purposeless
                    conversation!'''
                    print(dedent(s_toomuch))

                    add_points(1,'din_talk3')

            else:
                print("\nWuh?? What mannequin?")

        elif choice == "Go left":
            if look_around == True:
                add_points(5, 'din_left')
                enter_kitchen()
            else:
                s_slowdown = '''
                Slow down there, cowboy. What's the rush? Maybe you should look
                around first...'''
                print(dedent(s_slowdown))

        elif choice == "Go downstairs":
            print("\nDo you really want to go back down there? Hello, spider…")
            add_points(1,'din_down')

        elif choice == "Hint":
            show_hints(hints)

        elif choice == "Quit" or "quit":
            quit()

        elif choice == "Score":
            show_score()

        else:
            bad_input(choice)


def enter_kitchen():
    '''Kitchen Room'''
    print("\nYou are in the kitchen.")

    global NUM_POTATO
    hints = ["Look around", "Open door", "Pick up potato", "Drop potatoes",
    "Kiss potatoes", "Enter pass-code", "Go right"]

    #choices
    while(True):
        choice = input("\n> ")

        #remove leading and trailing white spaces from user's commands
        choice = choice.strip()

        if choice == "Look around":
            s_potatoes = '''
            Scattered on the black and white chequered linoleum floor are three
            potatoes.

            A door leads to the garden.

            The dining room is to your right.'''
            print(dedent(s_potatoes))

            add_points(10, 'kit_look')

        elif choice == "Open door":
            print("\nThe door is locked. You notice a keypad on the door.")
            add_points(1,'kit_open')

        elif choice == "Pick up potato":
            if NUM_POTATO < 3:
                NUM_POTATO +=1
                print("")
                print(NUM_POTATO, "potato.")
                add_points(1, 'kit_pot' + str(NUM_POTATO))
            else:
                s_chill = '''
                Dude, you picked up all the potatoes.

                Chill, Janelle. Chill.'''
                print(dedent(s_chill))

        elif choice == "Drop potatoes":
            if(NUM_POTATO != 0):
                print("\nOkay.")
                add_points(NUM_POTATO * (-1))
                NUM_POTATO = 0
            elif NUM_POTATO == 0:
                print("\nWuhhh? You don't have any potatoes.")


        elif choice == "Kiss potatoes":
            s_kiss = '''
            Oh, baby! You and the potatoes fall in love and beget a cute family
            of tater-tots. You grow old, greasy and happy. Life could not have
            turned out better. And yet, when you’re alone and see a shooting
            star split in the twilit sky, you wonder what your future would’ve
            been like had you stayed on your quest.'''
            dead(dedent(s_kiss))

        elif choice == "Enter pass-code":

            try:

                #Fetch pass code from global variable
                #More readable to compare with user input
                if PASS_CODE != None:

                    n1 = int(input("\nEnter first digit: "))
                    n2 = int(input("Enter second digit: "))
                    n3 = int(input("Enter third digit: "))
                    n4 = int(input("Enter fourth digit: "))

                    pc1 = int(PASS_CODE[0])
                    pc2 = int(PASS_CODE[1])
                    pc3 = int(PASS_CODE[2])
                    pc4 = int(PASS_CODE[3])

                    correct = n1 == pc1 and n2 == pc2 and n3 == pc3 and n4 == pc4

                    #Go to garden if pass-code is right and user has picked up
                    #all the potatoes
                    if correct == True and NUM_POTATO == 3:
                        print("\nThe door unlocks!")
                        add_points(10, 'kit_code')
                        enter_garden()

                    elif correct == True and NUM_POTATO != 3:
                        s_nopotatoes = '''
                        The deadbolt retracts and then shoots out again. You
                        pull and twist the door knob several times, but it
                        won’t give.

                        You stare menacingly at the potatoes on the floor…'''
                        print(dedent(s_nopotatoes))

                    elif correct == False:
                        s_wrong = '''
                        Did you really think that was going to work? Seriously,
                        I'm curious: '''
                        input(dedent(s_wrong))

                        s_explode = '''
                        Interesting, but, meh, what can you do.

                        The universe explodes and everyone dies. Nice work. As
                        today's youth would say: YOLO!'''
                        dead(dedent(s_explode))

                else:
                    s_secondshot = '''
                    I'm going to be nice here and give you a second shot at
                    this. Maybe you forgot to talk to someone or something...'''
                    print(dedent(s_secondshot))


            except ValueError:
                print("\nWhole numbers only, nitwit!")

        elif choice == "Go right":
            enter_diningroom(True)

        elif choice == "Hint":
            show_hints(hints)

        elif choice == "Quit" or "quit":
            quit()

        elif choice == "Score":
            show_score()

        else:
            bad_input(choice)


def enter_garden(seen_ladder = False):
    '''Garden Room'''

    print("\nYou are in the back garden.")

    hints = ["Look around", "Follow cat", "Look in well", "Go south",
    "Go down ladder"]

    while(True):

        choice = input("\n> ")

        #remove leading and trailing white spaces from user's commands
        choice = choice.strip()

        if choice =="Look around":
            s_dark ='''
            It is dark, but, by the glow of the half-moon, you can make out the
            lip of a well twelve paces ahead of you.

            An orange and white cat walks toward a hole in the back fence.

            South is the kitchen.'''
            print(dedent(s_dark))

            add_points(10, "gard_look")

        elif choice == "Follow cat":
            s_cat = '''
            The cat nonchalantly slinks through a tear in the mesh fence,
            unperturbed by the pointy bits garlanding its edges. The hole is too
            small for you to go through yourself, so you opt to use the fence
            door, which, for whatever reason, you always find to be ajar.

            You follow the cat down the back alley across a busy street, almost
            losing sight of her as you try to avoid a city bus from running you
            over. Weaving through sleepy residential areas on the other
            side, you stare at the cat, mesmerized: the way she sashays, hides
            under cars, licks her fur, stops to look around, deciding where to
            explore next…

            Unknowingly, you begin to transform. You shrink, your skin gets
            hairier, and you start walking on your hands and knees until your
            hands and knees become paws. You stop and think you hear squeaking.
            Maybe if you bring a mouse back as a gift, your sapient serf will
            set out tuna for dinner.'''
            dead(dedent(s_cat))

        elif choice == "Look in well":
            s_inwell = '''
            The hollow of the well is pitch-black. A rope ladder hangs from the
            the top of the well and along its inner wall.'''
            print(dedent(s_inwell))
            seen_ladder = True

            add_points(5, "gard_well")

        elif choice == "Go south":
            s_cant = '''
            You try to go back to the kitchen, but the door is locked. Oddly,
            there is no door knob, let alone a keypad on this side of the
            door.'''
            print(dedent(s_cant))

            add_points(1,'gard_south')

        elif choice == "Go down ladder":
            if(seen_ladder == False):
                print("\nWhat ladder?")
            else:
                add_points(5, "gard_down")
                enter_well()

        elif choice == "Hint":
            show_hints(hints)

        elif choice == "Quit" or "quit":
            quit()

        elif choice == "Score":
            show_score()

        else:
            bad_input(choice)


def enter_well():
    '''Well room'''

    s_rung = '''
    You reach the ladder's final rung and sense you are nowhere near the well’s
    bottom. Your stretched-out foot cuts empty air.

    There seems to be a twinkling dot far far below. But maybe it’s just an
    illusion.'''

    print(dedent(s_rung))

    while(True):

        choice = input("\n> ")

        #remove leading and trailing white spaces from user's commands
        choice = choice.strip()

        if choice == "Go up ladder":
            s_upladder = '''
            You climb the ladder and get out of the well. A wise decision'''
            print(dedent(s_upladder))
            enter_garden(seen_ladder=True)

        elif choice == "Go down ladder":
            s_downladder = '''You're on the final rung--you can't technically
            go down any more than you already have.'''
            print(dedent(s_downladder))
            add_points(1, 'well_down')

        elif choice == "Let go of ladder":
            add_points(25, 'well_fall')
            win()

        elif choice == "Score":
            show_score()

        elif choice == "Quit" or "quit":
            quit()

        else:
            pass


def win():
    '''You win! Game over.'''

    #Trivial animation of player 'falling'
    ascii_animation()

    s_win = '''
    Although it seems to take an infinite amount of energy to release your
    grip, you let go of the ladder and begin to drop through the void.

    The first moments (minutes? hours? days?) are a blank—you must’ve have
    blacked out from shock. You vaguely remember the feeling of gravity sucking
    your skeleton and innards through the pores of your skin. Just a feeling,
    fortunately.

    Now conscious and calm, you open your body such that you are no longer
    tumbling but falling spreadeagled. Where your fingertips ought to be
    grazing the well's walls is nothing. Only darkness and the restorative
    perfume of the earth after a thunderstorm, petrichor, surrounds you.
    As you plummet, a breeze rather than a gale caresses your face. It is more
    like someone’s cool breath than air resistance.

    Below, the twinkling dot whose existence you initially doubted has
    gotten no bigger but is more defined. It is a sun's disc, a mote of gold.
    Looking at it somehow drives away all the angst and loneliness you have
    suffered quietly all your life. And, although you cannot see them, you
    somehow know that there are others like yourself serenely soaring toward
    this convergence point for all things true.

    END'''

    print(dedent(s_win))

    end_game()


def end_game():
    '''It's all over: show the final score; write winner's name to file; roll
    the credits; exit.'''

    global WINNER_NAME

    show_score()

    WINNER_NAME = input("\nWhat's your name? ")

    s_goodbye = f'''
    Thanks, {WINNER_NAME}, for playing SHADOW HOUSE. Hope to see you again
    some time :-D!
    '''
    print(dedent(s_goodbye))

    write_winner_to_file() #Optional: game will run fine if you comment this out

    credits()

    quit()
