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
