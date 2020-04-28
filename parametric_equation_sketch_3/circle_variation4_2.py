#########################################
# Circle - plain - darkground 1
#########################################

t = 0
DELAY = 5 * 100

def setup():
    background(242, 242, 242)
    size(800, 800)

def draw():

    background(51, 51, 51)

    global t

    translate(width / 2, height / 2)

    for i in range(10):
        stroke(242, 242, 242, i*10)
        #noFill()
        fill(242, 242, 242, i*20)
        strokeWeight(2)
        circle(x(t + i), y(t + i), x1(t + i))

    t = t + 0.1


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)

def x(t):
    return cos(t / 10) + cos(t / 10) * 100

def y(t):
    return sin(t / 10) + cos(t / 10) * 100

def x1(t):
    return cos(t /10) * 250
