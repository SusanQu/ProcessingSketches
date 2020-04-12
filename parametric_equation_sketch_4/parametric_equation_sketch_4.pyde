t = 0
DELAY = 5*100

def setup():
    background(116, 138, 161) #gray blue
    #background(51, 85, 139) #cobalt blue
    #background(92, 112, 105) #sap green
    size(800, 800)

def draw():
    background(103, 127, 152) #gray blue
    #background(51, 85, 139) #cobalt blue
    #background(92, 112, 105) #sap green
    global t
    
    translate(width/2, height/2)
    
    for i in range(50):
        stroke(235, 161, 142)#light pink
        #stroke(241, 128, 59) #warm orange
        #stroke(241, 158, 98) #faint warm orange

        strokeWeight(2)
        line(x(t+i), y(t+i), x1(t+i), y1(t+i))
           
    t=t+0.125


def mousePressed():
    pauseFrame()

def pauseFrame():
    delay(DELAY)
    
def x(t):
    return sin(t/10) * 100

def y(t):
    return cos(t/10) + sin(t/10)*100 + cos(t/10) * 100

def x1(t):
    return sin(t/10) * 200 + sin(t)*2 + sin(t)

def y1(t):
    return cos(t/20) * 200
