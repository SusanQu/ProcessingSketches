#########################################
# Quad
#########################################

t = 0
DELAY = 5 * 100

def setup():
    background(248, 248, 248)
    size(800, 800)

def draw():

    background(248, 248, 248)
    global t

    translate(width / 2, height / 2)
    #rotate(3)

    for i in range(32):
        #stroke(153, 153, 153)
        stroke(204, 102, 0, i*5)
        fill(204, 102, 0, i*5)
        strokeWeight(20)

        # variation a
        quad(x(t - i), y(t - i), x1(t - i), y1(t - i),
             x(t - i), y(t - i), x1(t - i), y1(t - i))

        #rotate(PI/1.0*i)

        # variation b
        #quad(x(t - i), y(t - i), x1(t - i), y1(t - i),
         #    x(t + i), y(t + i), x1(t - i), y1(t - i))

        # variation c
        #quad(x(t - i), y(t - i), x1(t + i), y1(t - i),
         #    x(t - i), y(t + i), x1(t - i), y1(t - i))

        # variation d
        #quad(x(t - i), y(t + i), x1(t + i), y1(t - i),
         #    x(t + i), y(t + i), x1(t - i), y1(t - i))


    t = t + 0.1


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)

def x(t):
    return sin(t / 10) * 100

def y(t):
    return cos(t / 10) * 110

def x1(t):
    return sin(t / 10) * 100

def y1(t):
    return  sin(t / 10) * 110
