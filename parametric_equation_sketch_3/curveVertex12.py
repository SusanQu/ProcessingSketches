#########################################
# curveVertex 12 - sea creature
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

    translate(width/2-80, height/2)
    #scale(0.7)
    rotateY(PI/3)
    rotateX(PI/3)

    for y in range(rows/2):
        beginShape()
        for x in range(cols/2):
            #stroke(51, 51, 51, y*10)
            #dark red
            stroke(129, 36, 41, y*10)
            #red
            #stroke(174, 50, 47, y*10)
            strokeWeight(5)
            noFill()

            curveVertex(x*scl, xx(y*scl), y1(scl*x/10 + t))
            #dark red
            #stroke(129, 36, 41, y*10)
            #red
            stroke(174, 50, 47, y*10)
            curveVertex(x*scl+40, y1(scl*x/10 + t))

        endShape(OPEN)


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
    saveFrame('movie_frames/seaCreature_SingleFrame/SeaCreature_####.png')

def pauseFrame():
    delay(DELAY)
