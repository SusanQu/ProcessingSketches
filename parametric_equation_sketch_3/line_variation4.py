#########################################
# Lines variation 4
#########################################

scl = 30
t = 0
DELAY = 5 * 100

def setup():
    size(800, 800, P3D)

    global w
    global h
    global cols
    global rows
    global terrain

    w = 1400
    h = 1200
    cols = w / scl
    rows = h / scl


def draw():
    global t

    background(242, 242, 242)

    translate(-100, 0)
    scale(0.8)

    for y in range(rows):
        beginShape(LINES)
        for x in range(cols):
            stroke(51, 51, 51, y * 10)
            strokeWeight(3)
            noFill()

            vertex(x*scl, y*scl, yy(scl + t))
            vertex(x*scl, (y+10)*scl, xx(scl + t))

            #rect(x*scl, y*scl, scl, scl)
        endShape()


    t = t + 0.04

def xx(t):
    return sin(t/10) * 200

def yy(t):
    return cos(t / 10) * 300

def x1(t):
    return sin(t / 10) * 120

def y1(t):
    return cos(-t /10)*100

def mousePressed():
    pauseFrame()
    #saveFrame('movie_frames/lineDots_SingleFrame/points_####.png')

def pauseFrame():
    delay(DELAY)
