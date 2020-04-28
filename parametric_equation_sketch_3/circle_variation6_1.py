#########################################
# Circle - bloom - colour1
#########################################

t = 0
DELAY = 5 * 100

def setup():
    background(242, 242, 242)
    size(800, 800)

def draw():

    background(51, 51, 80)
    print(mouseX/2)
    global t

    translate(width / 2, height / 2)

    mouse_x = mouseX/2
    random_val = random(0, 255)

    for i in range(40):
        stroke(242, 242, mouse_x, i)
        #noFill()
        fill(242, 242, mouse_x, i)
        strokeWeight(2)
        circle(x(t + i), y(t + i), x1(t + i))

    for i in range(30):
        stroke(242, mouse_x, 242, i)
        #noFill()
        fill(242, mouse_x, 242, i)
        strokeWeight(2)
        circle(xx(t - i), yy(t - i), xx1(t - i))

    for i in range(30):
        stroke(mouse_x, 242, 242, i)
        #noFill()
        fill(mouse_x, 242, 242, i)
        strokeWeight(2)
        circle(xxx(t - i), yyy(t - i), xxx1(t - i))

    t = t + 0.15


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)

def x(t):
    return cos(-t / 10) * 150

def y(t):
    return sin(t / 20) + cos(t/10) * 75

def x1(t):
    return cos(-t /10) * 150


def xx(t):
    return cos(t / 10) * 150

def yy(t):
    return sin(-t / 20) + cos(t/10) * (-55)

def xx1(t):
    return cos(t /10) * 200


def xxx(t):
    return cos(t / 10) * 50

def yyy(t):
    return sin(-t / 20) + cos(t/10) * (200)

def xxx1(t):
    return cos(t /10) * 200
