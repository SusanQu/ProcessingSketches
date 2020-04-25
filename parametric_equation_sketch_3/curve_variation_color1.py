#########################################
# Curve
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


    for i in range(30):

        stroke(204, 102, 0, i*5)
        fill(204, 102, 0, i*5)
        strokeWeight(2)

        curve(x(t + i), y(t + i), x1(t + i), y1(t + i),
             x(t - i), y(t - i), x1(t - i), y1(t - i))




    t = t + 0.1


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)

def x(t):
    return cos(t / 10) * 100

def y(t):
    return sin(-t / 10) * 100

def x1(t):
    return cos(t /10) * 100

def y1(t):
    return sin(t / 10) * 120 - cos(-t /10) * 100
