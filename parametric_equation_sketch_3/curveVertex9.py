# #########################################
# curveVertex 9 - vase
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

    stroke(80, 80, 80)
    strokeWeight(25)
    #point(0, -100)
    point(70, 50)
    point(100, 200)
    point(yy(t*3), -250)
    point(xx(t*2), -200)

    # center lines
    for y in range(20):
        beginShape()
        for x in range(60):
            stroke(80, 80, 80, y)
            strokeWeight(1)
            #fill(248, 248, 248)
            noFill()

            #base
            #curveVertex(xx(x/10), 10)

            #longer vase
            curveVertex(xx(x/10), xx(y*10))
            curveVertex(xx(x+70+t), 50)
            curveVertex(yy(x+100+t), 200)
            curveVertex(yy(x-50+t), 200)

        endShape()

    #for a in range(10):
    stroke(80, 80, 80)
    noFill()
    strokeWeight(5)
    bezier(0, -100, 20, -150,
        20, -320, xx(t*2), -200)
    bezier(0, -100, 20, -200,
        40, -320, yy(t*3), -250)



    t = t + 0.06

def xx(t):
    return sin(t/10)*100

def yy(t):
    return sin(-t/10)*100

def x1(t):
    return cos(t/10)*100

def y1(t):
    #return cos(-t / 10) * 40 + sin(t / 10) * 100
    return sin(t/10 ) * 200

def mousePressed():
    pauseFrame()
    # saveFrame('movie_frames/lineDots_SingleFrame/points_####.png')

def pauseFrame():
    delay(DELAY)
