#########################################
# Quad
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

    for i in range(32):
        stroke(153, 153, 153)
        noFill()
        strokeWeight(2)
        quad(x(t + i), y(t + i), x1(t + i), y1(t + i),
             x(t - i), y(t - i), x1(t - i), y1(t - i))

    t = t + 0.1


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)

def x(t):
    return sin(-t / 10) * 300

def y(t):
    return cos(t / 10) * 160 + cos(t / 10) * 120
    #return cos(t / 10) * 220 + cos(t / 10) * 120

def x1(t):
    return sin(t / 10) * 250

def y1(t):
    return cos(-t /10)*100 + sin(t/10) * 110
