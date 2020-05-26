#########################################
# helix_variation4
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

    background(248, 248, 248)

    #translate(90, height/2)
    translate(width / 2, 90)
    scale(0.45)
    rotateX(PI / 2)
    rotateY(PI / 2)

    # center lines
    for y in range(rows):
        beginShape(LINES)
        for x in range(cols):
            stroke(80, 80, 80, y * 5)
            strokeWeight(2)
            #fill(248, 248, 248)
            noFill()

            vertex(x * scl, y, xx(scl * x + t))
            #vertex(x*scl, x+200, y1(scl*y + t))
        endShape()

    # side dots
    for a in range(rows):
        #beginShape(POINTS)
        for b in range(cols):
            stroke(80, 80, 80)
            strokeWeight(10)
            #fill(173, 237, 224)
            noFill()

            point(b*scl+10, a*scl+100, xx(scl * b + t))
        #endShape()

    t = t + 0.07

def xx(t):
    return sin(t / 10) * 300

def yy(t):
    return sin(-t / 10) * 300

def x1(t):
    return sin(t / -10) * 300

def y1(t):
    return (-t / 10) + (t / 20) * 100

def mousePressed():
    pauseFrame()
    # saveFrame('movie_frames/lineDots_SingleFrame/points_####.png')

def pauseFrame():
    delay(DELAY)
