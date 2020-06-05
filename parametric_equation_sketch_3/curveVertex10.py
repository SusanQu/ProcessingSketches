# #########################################
# curveVertex 10 - mushroom
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

    translate(width / 2, height / 2+15)

    stroke(80, 80, 80)
    strokeWeight(10)
    '''
    point(0, 10)
    point(70, 50)
    point(100, 200)
    point(-50, 200)
    '''

    # base

    for y in range(15):
        beginShape()
        for x in range(64):
            stroke(80, 80, 80, y)
            strokeWeight(1)
            #fill(248, 248, 248)
            noFill()

            #base
            #curveVertex(xx(x/10), 10)

            #longer vase
            curveVertex(xx(x/10), xx(y+t*1.25))
            curveVertex(xx(x+70+t), 50)
            curveVertex(yy(x+100+t), 200)
            curveVertex(yy(x-50+t), 200)

        endShape()


    translate(0, -200)


    #cap

    for y in range(15):
        beginShape()
        #for x in range(63):
        for x in range(53):
            stroke(80, 80, 80, y)
            strokeWeight(1)
            #fill(248, 248, 248)
            noFill()

            #base
            #curveVertex(xx2(x/10), 10)

            #longer vase
            curveVertex(xx2(x/10), xx(y+t))
            curveVertex(xx2(x+10+t), 50)
            #curveVertex(yy2(x+50+t), 200)
            curveVertex(yy2(x+100+t), 200)
            #curveVertex(x2(x-200+t), 300+y2(t))
            curveVertex(x2(x-200), 300+y2(t))
            curveVertex(x2(x-100+t), 200)

        endShape()



    t = t + 0.08


def xx(t):
    return sin(t/10)*100


def yy(t):
    return sin(-t/10)*100

def x1(t):
    return cos(t/10)*200

def y1(t):
    #return cos(-t / 10) * 40 + sin(t / 10) * 100
    return cos(-t / 10)

def xx2(t):
    return sin(t/10)*150

def yy2(t):
    return sin(-t/10)*200

def x2(t):
    return cos(t/10)*100

def y2(t):
    #return cos(-t / 10) * 40 + sin(t / 10) * 100
    return cos(t / 10) * 80


def mousePressed():
    pauseFrame()
    # saveFrame('movie_frames/lineDots_SingleFrame/points_####.png')

def pauseFrame():
    delay(DELAY)
