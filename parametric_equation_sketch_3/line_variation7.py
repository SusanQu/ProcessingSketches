#########################################
# line variation - tree trunk
#########################################

t = 0
DELAY = 5 * 100

def setup():
    background(242, 242, 242)
    size(800, 800)

def draw():

    background(242, 242, 242)
    global t


    translate(width / 2, height / 2)

    # layer 1, inner most
    for j in range(63):
        stroke(153, 153, 153)
        noFill()
        strokeWeight(2)
        line(x(t + j, 0, 0), y(t + j, 0), x1(t + j, 90, 10), y1(t + j, 85))

    # layer 2
    for i in range(63):
        stroke(153, 153, 153)
        noFill()
        strokeWeight(2)
        line(x(-t + i, 80, 10), y(-t + i, 80), x1(-t + i, 220, 20), y1(-t + i, 220))

    # layer 3
    for i in range(126):
        stroke(153, 153, 153)
        noFill()
        strokeWeight(2)
        line(x(-t + i, 210, 10), y(-t + i, 210), x1(-t + i, 250, 20), y1(-t + i, 250))


    t = t + 0.05



def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)


# c for the irregular curve of the circle
def x(t, x_start, c_start):
    return sin(t/10) * x_start + cos(t/5) * c_start

def y(t, y_start):
    return cos(t/10) * y_start

def x1(t, x_end, c_start):
    return sin(t/10) * x_end + cos(t/5) * c_start

def y1(t, y_end):
    return cos(t/10) * y_end
