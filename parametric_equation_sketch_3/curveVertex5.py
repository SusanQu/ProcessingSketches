# #########################################
# curveVertex 5 - flower
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
    h = 1200
    cols = w / scl
    rows = h / scl


def draw():
    global t

    background(248, 248, 248)

    translate(width / 2, height / 2)


    # center lines
    for y in range(rows / 3):
        beginShape()
        for x in range(cols / 2):
            stroke(80, 80, 80, y * 6)
            strokeWeight(1)
            #fill(248, 248, 248)
            noFill()

            curveVertex(x, xx(y))
            curveVertex(xx(x*20  + t), yy(y+100  + t))
            curveVertex(x1(x + t), y1(y + t))
            curveVertex(x, 0)

        endShape()

    t = t + 0.06

def xx(t):
    return sin(t / 10) * 200

def yy(t):
    return sin(-t / 10) * 200

def x1(t):
    return sin(t/5 ) * -200

def y1(t):
    #return cos(-t / 10) * 40 + sin(t / 10) * 100
    return cos(-t / 10) * 70 + sin(t / 10) * 100

def mousePressed():
    pauseFrame()
    # saveFrame('movie_frames/lineDots_SingleFrame/points_####.png')

def pauseFrame():
    delay(DELAY)
