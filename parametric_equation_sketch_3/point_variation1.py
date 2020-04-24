#########################################
# Point - Oval
#########################################

t = 0
DELAY = 5 * 100

def setup():
    background(242, 242, 242)
    size(800, 800)

def draw():

    background(242, 242, 242)
    global t
    global j

    translate(width / 2, height / 2)

    for i in range(40):
        stroke(153, 153, 153)
        strokeWeight(2)
        point(xxxxx3(t + i), yyyyy3(t + i))


    t = t + 0.1


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)


def xxxxx3(t):
    return sin(t/10) * 80

def yyyyy3(t):
    return cos(t/10) * 40
