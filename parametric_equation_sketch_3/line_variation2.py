#########################################
# Line variation 3
#########################################

scl = 30
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

    #background(242, 242, 242)
    background(241, 228, 209)
    translate(width / 2, height / 2)

    for y in range(rows/2):
        for x in range(cols/2):
            stroke(51, 51, 51, x * 10)
            strokeWeight(2)
            noFill()
            line(x1(t + x*scl), y1(t+y*scl), x1(t + x*scl)+15, y1(t+y*scl)-15)

    t = t + 0.03

def xx(t):
    return sin(t/10) * 100

def yy(t):
    return cos(t/10) * 200

def x1(t):
    return sin(t/10) * 150

def y1(t):
    return cos(t/20) * 200 + sin(t)*5 + sin(t)* 25

def mousePressed():
    pauseFrame()
    saveFrame('movie_frames/lineDots_SingleFrame/lines_####.png')

def pauseFrame():
    delay(DELAY)
