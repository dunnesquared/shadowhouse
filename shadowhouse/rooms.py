class Room():
    @classmethod
    def get_choices(cls):
        return list(cls.choices.keys())


class Basement(Room):

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

    def __init__(self):
        self.notebook_read = False


class DiningRoom(Room):

    passcode = None

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


    def __init__(self, seen_mannequin=False):
        self.talk_once = False


        self.talk_twice = False
        self.look_around = seen_mannequin

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
