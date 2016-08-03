from Level import *
from Cat import *

LEVELNAME = 'level3'

# AUXILIAR FUNCTIONS
def read():
    action = raw_input()
    if action == 'quit': raise StandardError
    try: level.move_cat(action)
    except: pass

def process():
    pass

def write():
    global level

    data = level.get_data()
    dx = len(data)
    dy = len(data[0])
    for y in xrange(dy):
        line = ''
        for x in xrange(dx):
            it = data[x][y]
            if it == 'floor':
                line += " "
            elif it == 'cat':
                line += "#"
            elif it == 'bowl':
                line += 'o'
            elif it == 'food':
                line += '*'
            elif it == 'wall':
                line += 'l'
            elif it == 'box':
                line += 'm'
        line += '|'
        print line
    line = ''
    for x in xrange(dx):
        line += '-'
    line += '/'
    print line
    # print "%s" % (str(level))

def ending():
    print "GOOD JOB"

# MAIN FUNCTIONS
def setup():
    global level
    global LEVELNAME

    level = Level(LEVELNAME)
    write()

def draw():
    global level

    if not level.end():
        read()
        process()
        write()
    else:
        ending()
        raise StandardError

if __name__ == '__main__':
    setup()
    while True:
        try: draw()
        except: break
