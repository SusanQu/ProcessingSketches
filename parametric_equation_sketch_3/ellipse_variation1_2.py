#########################################
# ellipse - flower - fatter pedals
#########################################

t = 0
DELAY = 5 * 100

def setup():
    background(242, 242, 242)
    size(800, 800)

def draw():

    background(242, 242, 242)
    global t


    for j in range(1, 10):
        leaf(2, 2, 1, 0)
        leaf(2, 2, 1, 180)
        leaf(2, 2, 1, 180)



    t = t + 0.14



def leaf(transX, transY, scale_val, rotate_val):
    translate(width/transX, height/transY)
    scale(scale_val)
    rotate(rotate_val)

    for i in range(20):
        stroke(51, 51, 51, i*10)
        fill(51, 51, 51, i*3)
        strokeWeight(2)
        ellipse(x(t + i), y(t + i), x1(t + i), xx(t + i))


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)

def x(t):
    return cos(t / 10) + sin(t/10) *100

def y(t):
    return sin(t / 10) + sin(t/10) * 100

def x1(t):
    return cos(t /10) * 250

def xx(t):
    return cos(t / 10)


def x2(t):
    return cos(t / 10)

def y2(t):
    return sin(t / 10)

def x12(t):
    return cos(t /10) * 250
