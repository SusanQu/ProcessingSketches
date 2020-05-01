#########################################
# ellipse - circle to square
#########################################

t = 0
DELAY = 5 * 100

def setup():
    background(242, 242, 242)
    size(700, 700)

def draw():

    background(242, 242, 242)
    global t

    ellipseMode(CENTER)
    stroke(121, 102, 72)
    fill(255, 193, 7)
    strokeWeight(1)
    ellipse(width/2, height / 2, 200, 200)


    translate(width / 2, height / 2)

    for i in range(80):
        stroke(121, 102, 72, i*10)
        fill(255, 193, 7, i)
        #noFill()
        strokeWeight(1)
        ellipse(x2(t + i), y2(t + i), x3(t + i), y3(t + i))

    t = t + 0.075


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)

def x2(t):
    return sin(t/10)

def y2(t):
    return cos(t/10)

def x3(t):
    return sin(t/10) * 200

def y3(t):
    return cos(t/10) * 200
