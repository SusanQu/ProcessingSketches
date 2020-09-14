# #########################################
# curveVertex 13 - flickering lamp 
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
    background(21, 62, 92)
    


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

    for i in range(20):
        stroke(242, 242, 242, i*0.8)
        #noFill()
        fill(242, 242, 242, i)
        strokeWeight(2)
        circle(xx(t*2 + i), yy(t*2 + i), xx1(t*2 + i))

    translate(0, -200)
    
    '''
    #gradient background
    for a in range(height):
        for b in range(width):
            distanceFromCenter = dist(a, b, width/2, height/2)
            stroke(distanceFromCenter)
            point(a, b)
    '''
    #leaf
    
    for y in range(25):
        beginShape()
        #for x in range(63):
        for x in range(63):
            stroke(242, 190, 84, y*3)
            strokeWeight(1)
            #fill(248, 248, 248)
            noFill()

            #base
            #curveVertex(xx2(x/10), 10)

            #longer vase

            curveVertex(-50, 10)
            curveVertex(yy2(x+100+t), 100)
            curveVertex(noise(yy2(x-100)), 200)
            curveVertex(noise(yy2(x-100)), 200)
            curveVertex(x2(x-200+t), 300)
            curveVertex(noise(y2(x-100)), 350)
            curveVertex(-150, 300)

        endShape()



    t = t + 0.05

def xx2(t):
    return sin(t/10)*150

def yy2(t):
    return sin(-t/10)*50

def x2(t):
    return cos(t/10)*100

def y2(t):
    #return cos(-t / 10) * 40 + sin(t / 10) * 100
    return cos(t / 10) * 5


def xx(t):
    return cos(t / 10)

def yy(t):
    return sin(t / 10)  * 100

def xx1(t):
    return cos(t /10) * 550


def mousePressed():
    pauseFrame()
    saveFrame('movie_frames/lamp_SingleFrame/lamp_####.png')

def pauseFrame():
    delay(DELAY)
