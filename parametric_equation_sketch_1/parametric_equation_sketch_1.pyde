t = 0
DELAY = 3*100

def setup():
    background(20)
    size(600, 600)

def draw():

    background(20)
    global t
    
    translate(width/2, height/2)
    
    for i in range(50):
        stroke(255)
        strokeWeight(5)
        line(x(t+i), y(t+i), x1(t+i), y1(t+i))
    
    for i in range(20):
        stroke(204, 102, 0)
        strokeWeight(5)
        line(x2(t+i), y2(t+i), x3(t+i), y3(t+i))
        
    t=t+0.15


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)

def x(t):
    return sin(t/10) * 100 + sin(t/5)*20 + sin(t/5)*100

def y(t):
    return cos(t/10) * 100

def x1(t):
    return sin(t/10) * 200 + sin(t)*2 + sin(t/5)

def y1(t):
    return cos(t/20) * 200 + cos(t/12) * 20



def x2(t):
     return sin(-t/10) * 100 + sin(t/5)*20

def y2(t):
    return cos(-t/10) * 100

def x3(t):
    return sin(-t/10) * 200 + sin(t)*2

def y3(t):
    return cos(-t/20) * 200 + cos(t/12) * 20
