#########################################
# Curve
#########################################

t = 0
p = 0
DELAY = 5 * 100

def setup():
    background(242, 242, 242)
    size(800, 600)

def draw():

    background(242, 242, 242)
    global t
    global p

    x = 0
    j = 0
    while(x < width):
        line(x, 0, x, 400)
        x = x + 5

    while(j < (width + 300)):
        line(j, 400, 200, j)
        j = j + 10

    obj()



    t = t + 0.1


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)



def obj():
    translate(550, 420)

    for i in range(20):
        stroke(51, 51, 51, i*10)
        fill(51, 51, 51)
        strokeWeight(2)
        ellipse(xx(t + i), yy(t + i), xx1(t + i), yy1(t + i))

def xx(t):
    return cos(t / 10) + sin(-t/10) * 100

def yy(t):
    return sin(t / 10) + sin(t/10) * 50

def xx1(t):
    return cos(t /10) * 200

def yy1(t):
    return cos(t / 10)
