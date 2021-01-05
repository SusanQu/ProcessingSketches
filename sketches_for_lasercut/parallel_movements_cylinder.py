#########################################
# Arc 2
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
    translate(width / 2, height / 2)


    translate(0, 0)
    for i in range(25):
        for j in range(1):
            stroke(51, 51, 51)
            strokeWeight(i/5)
            noFill()
            line( x(t + i),  y(t + j), x(t + i) + 100,  y(t + j)+100 )
            line( x(t + i)-100,  y(t + j)-110, x(t + i) - 100,  y(t + j)-100 )
            line( x(t + i)- 100, yy(t + j), x(t + i) + 100,  y(t + j) +100 )


    t = t + 0.05

def x(t):
    return sin(t/10) * 200

def y(t):
    return cos(t)

def x1(t):
    return sin(t/10) * 200

def y1(t):
    return cos(t/10) * 50 + 50

def xx(t):
    return sin(t/1) * 100

def yy(t):
    return cos(t/10) * 100

def mousePressed():
    pauseFrame()
    #saveFrame('movie_frames/png/points_####.png')

def pauseFrame():
    delay(DELAY)
