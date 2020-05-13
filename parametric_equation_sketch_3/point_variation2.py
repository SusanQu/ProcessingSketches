#########################################
# Triangle - Terrain
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

    background(242, 242, 242)
    translate(width / 2, height / 2)

    for y in range(rows/2):
        for x in range(cols/2):
            stroke(51, 51, 51, x * 10)
            strokeWeight(10)
            noFill()
            point(xx(t + x*scl), yy(t+y*scl))

    t = t + 0.05

def xx(t):
    return sin(t/10) * 100

def yy(t):
    return cos(t/10) * 200

def mousePressed():
    pauseFrame()
    saveFrame('movie_frames/lineDots_SingleFrame/points_####.png')

def pauseFrame():
    delay(DELAY)
