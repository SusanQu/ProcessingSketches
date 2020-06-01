# #########################################
# curveVertex 6
###########################################


scl = 30
t = 0
DELAY = 5 * 100

def setup():
    size(800, 800, P3D)

    global w
    global h
    global cols
    global rows

    w = 1400
    h = 1400
    cols = w / scl
    rows = h / scl


def draw():
    global t

    background(248, 248, 248)

    translate(width / 2, height / 2)

    # center lines
    for y in range(rows/2 ):
        beginShape()
        for x in range(cols/2):
            stroke(80, 80, 80, y * 5)
            strokeWeight(1)
            #fill(248, 248, 248)
            noFill()

            curveVertex(x, y)
            curveVertex(x, y1(y + t))
            curveVertex(x1(y + t), 100)
            curveVertex(0, 200)

        endShape()

    t = t + 0.05

def xx(t):
    return sin(t / 10) * 100

def yy(t):
    return sin(-t / 10) * 100

def x1(t):
    return sin(t / 5) * 200

def y1(t):
    # return cos(-t / 10) * 40 + sin(t / 10) * 100
    return cos(-t / 10) * 100 + sin(t / 10) * 100

def mousePressed():
    pauseFrame()
    saveFrame('movie_frames/curveVertex_SingleFrame/bnwCurve_####.png')

def pauseFrame():
    delay(DELAY)
