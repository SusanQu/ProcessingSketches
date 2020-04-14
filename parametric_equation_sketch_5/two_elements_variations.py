#########################################
# Line and Dots
#########################################

t = 0
DELAY = 5 * 100

def setup():
    background(242, 242, 242)
    size(800, 800)

def draw():

    background(242, 242, 242)
    global t

    translate(width / 2, height / 2)

    for i in range(100):
        stroke(153, 153, 153)
        strokeWeight(2)
        line(x(t + i), y(t + i), x1(t + i), y1(t + i))

    for i in range(50):
        stroke(153, 153, 153)
        strokeWeight(5)
        point(x3(t + i), y3(t + i))

    t = t + 0.13


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)

def x(t):
    return sin(t / 10) * 80

def y(t):
    return cos(t / 10) + sin(t / 10) * 80 + cos(t / 10) * 100 + sin(t / 10) * 250

def x1(t):
    return sin(t / 10) * 200 + sin(t) * 2 + sin(t)

def y1(t):
    return cos(t / 20) * 200




def x3(t):
    return sin(-t / 10) * 250

def y3(t):
    return cos(t / 20) * 160
