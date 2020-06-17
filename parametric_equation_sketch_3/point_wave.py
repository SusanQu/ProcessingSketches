#########################################
# Wave - Dots
#########################################

scl = 30
t = 0
DELAY = 5 * 100
moving = float(0)

def setup():
    size(800, 800, P3D)

    global w
    global h
    global cols
    global rows
    global surface

    w = 1200
    h = 1200
    cols = w / scl
    rows = h / scl

    surface = [[0]*cols for i in range(cols+1)]


def draw():
    global t
    global moving

    background(237, 204, 195)
    translate(-70, height / 2 )
    #rotateY(PI/3)
    rotateX(PI/3)

    moving = moving - 0.01

    yoff = moving

    for y in range(rows):
        xoff = float(0)
        for x in range(cols):
            surface[x][y] = map(noise(xoff, yoff), 0, 1, -20, 20)
            xoff = xoff + 0.1
        yoff = yoff + 0.1

    strokeWeight(2)
    stroke(87, 85, 89)
    z = surface[x][y]
    line(620, 0, z, 655, 0, z)
    line(610, 5, z, 660, 5, z)
    line(650, -50, z, 640, 5, z)
    line(645, -20, z, 655, 0, z)

    for y in range(rows):
        for x in range(cols):
            stroke(114, 156, 188, y*7)
            strokeWeight(10)
            noFill()
            point(x*scl,  yy(y+t/2), surface[x][y])


    translate(0, 200)
    for a in range(rows/2):
        for b in range(cols):
            stroke(114, 156, 188, a*5)
            strokeWeight(10)
            noFill()
            point(b*scl,  yy(a+t/2), surface[b][a])

    t = t + 0.05

def xx(t):
    return sin(t/10) * 200

def yy(t):
    return cos(t/20) * 250

def mousePressed():
    pauseFrame()
    saveFrame('movie_frames/lineDots_SingleFrame/points_####.png')

def pauseFrame():
    delay(DELAY)
