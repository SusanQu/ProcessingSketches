#########################################
# Line - sun
#########################################

t = 0
DELAY = 5 * 100

def setup():
    background(242, 242, 242)
    size(800, 800)

def draw():

    background(242, 242, 242)
    global t

    for j in range(1, 12):
        leaf(2, 2, 1, 180)
        leaf(2, 2, 1, 180)
        leaf(2, 2, 1, 180)

    t = t + 0.13


def leaf(transX, transY, scale_val, rotate_val):
    translate(width / transX, height / transY)
    scale(scale_val)
    rotate(rotate_val)

    for i in range(20):
        stroke(51, 51, 51, i * 10)
        fill(51, 51, 51, i * 3)
        strokeWeight(2)
        line(x(t + i), y(t + i), x1(t + i), y1(t + i))


def mousePressed():
    pauseFrame()
    saveFrame('movie_frames/lineDots_SingleFrame/lineDots_####.png')

def pauseFrame():
    delay(DELAY)

def x(t):
    return sin(t/10) * 100

def y(t):
    return cos(t)

def x1(t):
    return sin(t/10) * 300

def y1(t):
    return cos(t/10) * 200
