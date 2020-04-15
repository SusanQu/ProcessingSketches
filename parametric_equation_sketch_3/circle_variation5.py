#########################################
# Circle - body
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
        stroke(153, 153, 153)
        noFill()
        strokeWeight(2)
        circle(x(t - i), y(t - i), x1(t + i))

    for i in range(30):
        stroke(153, 153, 153)
        noFill()
        strokeWeight(2)
        circle(xx(t - i), yy(t - i), xx1(t + i))

    t = t + 0.1


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)

def x(t):
    return cos(-t / 10) * 150

def y(t):
    return sin(t / 20) + cos(t/10) *75

def x1(t):
    return cos(-t /10) * 150


def xx(t):
    return cos(t / 10) * 150

def yy(t):
    return sin(-t / 20) + cos(t/10) * (-75)

def xx1(t):
    return cos(t /10) * 150
