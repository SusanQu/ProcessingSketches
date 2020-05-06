#########################################
# Compostion 4 - square background
#########################################

t = 0
p = 0
DELAY = 5 * 100
xoff = float(0.0)

def setup():
    background(242, 242, 242)
    size(800, 800)

def draw():

    background(242, 242, 242)
    global t
    global p
    global xoff

    x = 0
    j = 0
    e = 0
    b = 0
    xoff = xoff + 1


    while(x < width):
        line(x , 0, x , 550)
        stroke(51, 51, 51)
        strokeWeight(2)
        x = x + 3


    while(j < (width + 600)):
        line(j, 550, 0, j)
        strokeWeight(1.25)
        j = j + 10



    obj(550, 600, 1.15, 0)
    obj1(130, -150)
    cloud()


    t = t + 0.11




def mousePressed():
    pauseFrame()
    saveFrame('movie_frames/SingleFrame/composition_####.png')

def pauseFrame():
    delay(DELAY)



def obj(transX, transY, scaleX, rotateObj):
    translate(transX, transY)
    scale(scaleX)
    rotate(rotateObj)

    for i in range(40):
        stroke(242, 242, 242, i*10)
        fill(242, 242, 242)
        strokeWeight(2)
        ellipse(xx(t + i), yy(t + i), xx1(t + i, 400), yy1(t + i))

def obj1(transX, transY):
    translate(transX, transY)

    for i in range(50):
        stroke(242, 242, 242, i*2)
        fill(242, 242, 242)
        strokeWeight(1)
        ellipse(xxx(t + i), yyy(t + i), xxx1(t + i), yyy1(t + i))

def cloud():
    translate(-250, -120)
    for s in range(40):
        stroke(242, 242, 242, s*3)
        #noFill()
        fill(242, 242, 242, s*0.5)
        strokeWeight(5)
        bezier(xs(t + s), ys(t + s), xs1(t +s), ys1(t+s),
                 xs(t -s), ys(t - s), xs1(t - s), ys1(t-s))



def xx(t):
    return cos(t / 10) + sin(-t/10) * 125

def yy(t):
    return sin(t / 10) + sin(t/10) * 50

def xx1(t, w):
    return cos(t /10) * w

def yy1(t):
    return cos(t / 10)



def xxx(t):
    return sin(t / 10)

def yyy(t):
    return cos(t / 10) + sin(-t/10) * 50

def xxx1(t):
    return cos(t / 10)  * 100

def yyy1(t):
    return cos(t /10)


def xs(t):
    return cos(t / 10) * 200

def ys(t):
    return sin(-t / 10) * 200  - sin(-t / 20) * 250

def xs1(t):
    return cos(-t /10) * 325

def ys1(t):
    return sin(t / 10) * 120 + cos(-t /10) * 250
