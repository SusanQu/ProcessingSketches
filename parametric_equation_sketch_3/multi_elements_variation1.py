#########################################
# Lines - layers 
#########################################

t = 0
j = 0
DELAY = 5 * 100

def setup():
    background(242, 242, 242)
    size(800, 800)

def draw():

    background(242, 242, 242)
    global t
    global j

    translate(width / 2, height / 2)



    for i in range(50):
        stroke(153, 153, 153)
        strokeWeight(2)
        line(x2(j + i), y2(j + i), x3(j + i), y3(j + i))

    for i in range(50):
        stroke(153, 153, 153)

        strokeWeight(2)
        line(xx2(j + i), yy2(j + i), xx3(j + i), yy3(j + i))

    for i in range(40):
        stroke(153, 153, 153)
        strokeWeight(2)
        line(xxx2(t + i), yyy2(t + i), xxx3(t + i), yyy3(t + i))

    for i in range(40):
        stroke(153, 153, 153)
        strokeWeight(2)
        line(xxxx2(t + i), yyyy2(t + i), xxxx3(t + i), yyyy3(t + i))



    t = t + 0.11
    j = j + 0.08


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)


#################

def x2(t):
    return sin(t/10) * 150

def y2(t):
    return cos(t/10) * 200 + sin(t/10) *250

def x3(t):
    return sin(t/10) * 200

def y3(t):
    return cos(t/10) * 100

###################

def xx2(t):
    return sin(-t/10) * 150

def yy2(t):
    return cos(-t/10) * 150 + sin(-t/10) * 150

def xx3(t):
    return sin(-t/10) * 185

def yy3(t):
    return cos(-t/10) * 80

###################

def xxx2(t):
    return sin(t/10) * 120

def yyy2(t):
    return cos(t/10) * 100 + sin(t/10) * 100

def xxx3(t):
    return sin(t/10) * 140

def yyy3(t):
    return cos(t/10) * 70

###################

def xxxx2(t):
    return sin(-t/10) * 90

def yyyy2(t):
    return cos(-t/10) * 80 + sin(-t/10) * 50

def xxxx3(t):
    return sin(-t/10) * 105

def yyyy3(t):
    return cos(-t/10) * 60

###################

def xxxxx2(t):
    return sin(t/10) * 70

def yyyyy2(t):
    return cos(t/10) * 65 + sin(t/10) * 15

def xxxxx3(t):
    return sin(t/10) * 80

def yyyyy3(t):
    return cos(t/10) * 40
