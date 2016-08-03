from Level import *

# CONSTANTS
BLACK = color(0, 0, 0)
WHITE = color(255, 255, 255)
RED = color(237, 41, 57)
YELLOW = color(254, 223, 0)
BLUE = color(0, 123, 163)
ORANGE = color(255, 191, 0)
PURPLE = color(112, 41, 99)
GREEN = color(147, 197, 114)
BROWN = color(205, 133, 63)
GREY = color(110, 127, 128)

LEVELNAME = loadStrings('level.txt')[0]

# GUI FUNCTIONS
def create_colours():
    colour = {}
    
    colour['black'] = BLACK
    colour['white'] = WHITE
    colour['red'] = RED
    colour['yellow'] = YELLOW
    colour['blue'] = BLUE
    colour['orange'] = ORANGE
    colour['purple'] = PURPLE
    colour['green'] = GREEN
    colour['brown'] = BROWN
    colour['grey'] = GREY

    return colour

def create_moves():
    move = {}

    move['W'] = 'up'
    move['S'] = 'down'
    move['A'] = 'left'
    move['D'] = 'right'
    # move['q'] = 'quit'

    buttons = []
    for button in move:
        buttons.append(button) 
    for button in buttons:
        move[button.swapcase()] = move[button]

    return move

def load_images(inlet):
    outlet = {}

    for it in inlet:
        img = loadImage(it + '.gif')
        outlet[it] = img

    return outlet


def ending():
    println("GOOD JOB\a")

# AUXILIAR FUNCTIONS
def process():
    global level
    global actions

    for act in actions:
        try:
            level.move_cat(act)
        except:
            pass

    actions = []

def write():
    global level
    global colours
    global sprites

    old_method = """
    background(BLACK)
    translate(width / 4, height / 4)

    R = 10
    world = level.get_data()
    des = str(world)
    dx = len(world)
    dy = len(world[0])
    
    for i, strip in enumerate(world):
        for j, it in enumerate(strip):
            fill(colours[level.get_colour(it)])
            ellipse(R + 2 * i * R, R + 2 * j * R, R, R)
    """

    R = 50
    world = level.get_data()
    dy, dx = level.get_dimensions()
    
    background(BLACK)
    translate((width - (dx * R)) / 2, (height - (dy * R)) / 2)

    for i, strip in enumerate(world):
        for j, it in enumerate(strip):
            image(sprites[it], i * R, j * R)

# USER INPUT IMPLEMENTATIONS
def keyPressed():
    global actions
    global moves

    if moves.has_key(key):
        actions.append(moves[key])

# MAIN FUNCTIONS
def setup():
    global level
    global colours
    global moves
    global sprites
    global actions

    size(600, 400)
    
    # noLoop()
    noStroke()
    frameRate(16)
    smooth(4)

    level = Level(LEVELNAME)
    loader = Loader()
            
    colours = create_colours()
    sprites = load_images(level.colours)
    moves = create_moves()
    actions = []

def draw():
    global level

    if not level.end():
        process()
        write()
    else:
        ending()
        exit()


