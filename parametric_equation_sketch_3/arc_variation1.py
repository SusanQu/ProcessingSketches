#########################################
# Arc 
#########################################

scl = 60
t = 0
DELAY = 5 * 100

def setup():
    size(800, 800)

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
    translate(100, 100)

    for y in range(rows/2):
        for x in range(cols/2):
            stroke(51, 51, 51)
            strokeWeight(5)
            noFill()
            arc(x*scl, y*scl, 30, 30, 0, PI)

    translate(0, 0)
    for y in range(rows/2):
        for x in range(cols/2):
            stroke(51, 51, 51)
            strokeWeight(5)
            noFill()
            arc( x*scl, y*scl, 30, xx(y+t), PI, TWO_PI)

    t = t + 0.05

def xx(t):
    return sin(t/1) * 100

def yy(t):
    return cos(t/10) * 200

def mousePressed():
    pauseFrame()
    saveFrame('movie_frames/lineDots_SingleFrame/points_####.png')

def pauseFrame():
    delay(DELAY)
