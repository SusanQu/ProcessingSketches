#########################################
# Curve
#########################################

t = 0
p = 0
DELAY = 5 * 100

def setup():
    background(242, 242, 242)
    size(800, 800)

def draw():

    background(242, 242, 242)
    global t
    global p

    translate(width/2 , height / 2)



    for i in range(64):
        stroke(153, 153, 153)
        noFill()
        strokeWeight(2)
        line( y1(t + i), x(t + i),  y(t + i), x1(t + i))

    t = t + 0.1


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)

def x(t):
    return sin(t/10) * 200

def y(t):
    return cos(t/10)

def x1(t):
    return sin(t/10) * 200

def y1(t):
    return cos(t/40) * 200
