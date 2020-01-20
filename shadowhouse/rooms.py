"""Module containing the descriptions that make up Shadow House's story.

This module is made up of several classes that contain descriptions
of each room a player can enter. Within each room choices can be made
and each corresponding class has descriptions of those as well. Rooms
such as Basement, DiningRoom, etc., all inherit from parent class Room. None of
the classes currently instantiate objectsm and rather function more like
glorified dictionaries.

An important feature of most classes is that they contain class memeber
variables that are needed to define game state (e.g. In Basement, the boolean
value of notebook_read determines whether a player will ultimately
live or die!).

The decision to use class member variables is one of convenience and,
perhapsm not the best design decision. Using object member variables would've
meant either making the Room objects global or passing objects from room to
room. For a small game like this, however, the class member variable solution
works and decouples a lot of game data from game logic
in an arguably intuitve way.
"""

class Room():
    @classmethod
    def get_choices(cls):
        return list(cls.choices.keys())


class Basement(Room):

    notebook_read = False

    description = '''
    You are sitting on a cozy sofa in the basement of your childhood home.

    Night paints small windows that open on to the front lawn and the
    alley between your house and the neighbour’s. The air is cool down here.
    A sticky film of sweat coats your bare legs and arms.

    A TV remote sits next to your lap.
    A notebook lies on the table in front of you.
    A hairy spider, the size of a cupcake, crawls near your sandalled foot.'''

    descr_tv = '''
    You grab the remote and hit the POWER button. The TV hisses and
    cracks. Slowly, an image fades on to its glass. On top of the
    television, you notice an unbroken copy of “Infinite Jest”
    gathering dust.

    The images are, at once, foggy yet vividly clear. For only a few
    moments are you able to register what you’re seeing: a beautiful
    woman whose face is horribly disfigured; a wailing baby’s head which
    is zoomed into but never seen any closer, like a fractal.

    You cannot stop watching The Entertainment. Like a toppled Babushka
    doll, you fall from your perch on the sofa to the floor.

    Several hours later, a tubby coroner waves a lit Gauloise over your
    corpse as he tells Special Det. Alvin Gumby the autopsy's
    conclusion:

    “It’s textbook, Gum-man: death by dehydration and too much
    fuuuunnnn!”'''

    descr_spider = '''
    The teal silver-back Colombian jumping spider springs on to your
    foot and sinks its fangs. You kick your leg violently until
    the arachnid flies off. It cuts through the air like a spinning wad
    of wet toilet paper, hitting the the glass of your VCR/Nintendo
    cabinet with an assertive rattle and splat.

    A stinging, then a burning, then a numbness, first in your
    right pinky but not a minute later everywhere. You think of Agent
    Cooper, Laura Palmer and a white stallion galloping in black space.
    The last thing you see is a spinning ceiling fan. You think:

    "Who the hell has a ceiling fan in their basement?" "'''

    descr_upstairs = '''
    You climb the musty, blue carpet staircase, narrowly avoiding
    a slimy banana peel lying in the middle of a step.

    At the top of the stairs you walk a few paces down the hall and
    make a left.'''

    descr_notebook = '''
    The notebook turns out to be your old diary. You glaze over
    the many cringeworthy passages, but two shout out at you.
    You have no idea why.

    "Many die where they blindly tread.”
    “Peanut-butter-and-banana sandwiches rock!!”

    Your stomach rumbles.'''

    descr_around = "\nYou already did that."

    descr_banana = '''
    You climb the stairs, but slip on a slimy banana peel (yes —
    this can happen in real life, not just in cartoons). The fall
    forward, let’s say, makes you a lot less pretty than you were
    once renowned for. A lot less.'''

    choices = {
                "Watch TV": descr_tv,
                "Squash spider": descr_spider,
                "Go upstairs": descr_upstairs,
                "Read notebook": descr_notebook,
                "Look around": descr_around
              }



class DiningRoom(Room):

    passcode = None
    talk_once = False
    talk_twice = False
    look_around = False

    description = "\nYou are in the dining room."

    descr_around = '''
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

    descr_straws = '''
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

    descr_touch = "\nShame on you! This is not that kind of game ;-)."

    descr_talk = '''
    At first the mannequin ignores your blather when suddenly
    she says:

    "The fruits of all our labours will not be wasted on
    soul-consuming tasks.”'''

    descr_toomuch = '''
    The mannequin has nothing more to say to you. She's an
    introvert -- stop draining her energy with purposeless
    conversation!'''

    descr_nomannequin = "\nWuh?? What mannequin?"

    descr_slowdown = '''
    Slow down there, cowboy. What's the rush? Maybe you should look
    around first...'''

    descr_left = ""

    descr_down = "\nDo you really want to go back down there? Hello, spider…"

    descr_passcode = "Remember these numbers:"

    choices = {
                "Eat veggie straws": descr_straws,
                "Touch mannequin": descr_touch,
                "Talk to mannequin": descr_talk,
                "Go left": descr_left,
                "Go downstairs": descr_down,
                "Look around": descr_around
              }


    @classmethod
    def stringify_passcode(cls):
        return f"{cls.passcode[0]} {cls.passcode[1]} {cls.passcode[2]} {cls.passcode[3]}"


class Kitchen(Room):


    description = "\nYou are in the kitchen."

    potatoes = 0

    descr_door = "\nThe door is locked. You notice a keypad on the door."

    descr_around = '''
    Scattered on the black and white chequered linoleum floor are three
    potatoes.

    A door leads to the garden.

    The dining room is to your right.'''

    descr_chill = '''
    Dude, you picked up all the potatoes.

    Chill, Janelle. Chill.'''

    descr_nopotatoes = "\nWuhhh? You don't have any potatoes."

    descr_kiss = '''
    Oh, baby! You and the potatoes fall in love and beget a cute family
    of tater-tots. You grow old, greasy and happy. Life could not have
    turned out better. And yet, when you’re alone and see a shooting
    star split in the twilit sky, you wonder what your future would’ve
    been like had you stayed on your quest.'''

    descr_noopen = '''
    The deadbolt retracts and then shoots out again. You
    pull and twist the door knob several times, but it
    won’t give.

    You stare menacingly at the potatoes on the floor…'''

    descr_wrong = '''
    Did you really think that was going to work? Seriously,
    I'm curious: '''

    descr_explode = '''
    Interesting, but, meh, what can you do.

    The universe explodes and everyone dies. Nice work. As
    today's youth would say: YOLO!'''

    descr_secondshot = '''
    I'm going to be nice here and give you a second shot at
    this. Maybe you forgot to talk to someone or something...'''

    choices = {
                "Open door": descr_door,
                "Pick up potato": None,
                "Drop potatoes": None,
                "Go right": None,
                "Kiss potatoes": descr_kiss,
                "Enter pass-code": None,
                "Look around": descr_around
              }


class Garden(Room):

    seen_ladder = False

    description = "\nYou are in the back garden."

    descr_around = '''
    It is dark, but, by the glow of the half-moon, you can make out the
    lip of a well twelve paces ahead of you.

    An orange and white cat walks toward a hole in the back fence.

    South is the kitchen.'''

    descr_cat = '''
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

    descr_well = '''
    The hollow of the well is pitch-black. A rope ladder hangs from the
    the top of the well and along its inner wall.'''

    descr_south = '''
    You try to go back to the kitchen, but the door is locked. Oddly,
    there is no door knob, let alone a keypad on this side of the
    door.'''


    choices = {
                "Follow cat": descr_cat,
                "Look in well": descr_well,
                "Go south": descr_south,
                "Go down ladder": None,
                "Look around": descr_around
              }


class Well(Room):
    description = '''
    You reach the ladder's final rung and sense you are nowhere near the well’s
    bottom. Your stretched-out foot cuts empty air.

    There seems to be a twinkling dot far far below. But maybe it’s just an
    illusion.'''

    descr_upladder = '''
    You climb the ladder and get out of the well. A wise decision'''

    descr_downladder = '''
    You're on the final rung--you can't technically go down any more
    than you already have.'''

    choices = {
                "Go up ladder": descr_upladder,
                "Go down ladder": descr_downladder
              }

class Win(Room):
    description = '''
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
