#########################################
# Triangle variation 1
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

    w = 1400
    h = 1200
    cols = w / scl
    rows = h / scl


def draw():
    global t

    background(173, 237, 224)

    translate(180, height/2)
    scale(0.7)
    rotateX(PI/3)

    for y in range(rows):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols/2):
            stroke(51, 51, 51, y * 8)
            strokeWeight(3)
            fill(173, 237, 224)

            vertex(x*scl, xx(y*scl), y1(scl*x + t))
            #vertex(x*scl, xx((y+10)*scl), y1(scl*x + t))
        endShape()


    t = t + 0.07

def xx(t):
    return sin(t/10) * 200

def yy(t):
    return cos(t / 10) * 300

def x1(t):
    return sin(t / 10) * 120

def y1(t):
    return cos(-t /10)*100 + sin(t/20) * 100

def mousePressed():
    pauseFrame()
    #saveFrame('movie_frames/lineDots_SingleFrame/points_####.png')

def pauseFrame():
    delay(DELAY)
