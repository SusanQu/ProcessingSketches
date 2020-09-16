#########################################
# line variation - tree trunk
#########################################

t = 0
DELAY = 5 * 100
y_axis = int(1)
x_axis = int(2)
c1 = color(255)
c2 = color(0)

def setup():
    background(242, 242, 242)
    size(800, 800)
    


def draw():

    background(250)
   
    global t
    global c1
    global c2


    translate(width / 2, height / 2)
    
    # layer 1, inner most
    for j in range(tl(1)):
        stroke(180)
        noFill()
        strokeWeight(0.5)
        line(x(t + j, 0, 0), y(t + j, 0), x1(t + j, 90, 10), y1(t + j, 85))


    # layer 2
    for i in range(tl(5)):
        stroke(160)
        noFill()
        strokeWeight(0.5)
        line(x(-t + i, 45, -3), y(-t + i, 45), x1(-t + i, 110, 10), y1(-t + i, 110))
    
    # layer 2new
    for i in range(tl(2)):
        stroke(100)
        noFill()
        strokeWeight(1)
        line(x(-t*2 + i, 82, -1), y(-t*2 + i, 82), x1(-t*2 + i, 90, -2), y1(-t*2 + i, 90))
   
   # layer 2.5
    for i in range(10, tl(1)):
        stroke(140, i)
        noFill()
        strokeWeight(10)
        line(x(-t*2 + i, 110, 10), y(-t*2 + i, 110), x1(-t*2 + i, 145, 10), y1(-t*2 + i, 150))
   
    # layer 3
    for i in range(tl(6)):
        stroke(130)
        noFill()
        strokeWeight(0.5)
        line(x(-t + i, 90, -5), y(-t + i, 90), x1(-t + i, 220, 20), y1(-t + i, 220))

    # layer 3.5
    for i in range(20, 90):
        stroke(153, 153, 153, i*0.75)
        noFill()
        strokeWeight(18)
        line(x(t*2 + i, 180, 10), y(t*2 + i, 180), x1(t*2 + i, 220, 10), y1(t*2 + i, 210))

    # layer 4
    for i in range(tl(14)):
        stroke(80)
        noFill()
        strokeWeight(1)
        line(x(-t + i, 220, 10), y(-t + i, 220), x1(-t + i, 225, 10), y1(-t + i, 225))

    # layer 5
    for i in range(tl(6)):
        stroke(100)
        noFill()
        strokeWeight(1)
        line(x(-t + i, 225, 10), y(-t + i, 225), x1(-t + i, 235, 10), y1(-t + i, 240))


    t = t + 0.01
    
    

#trunk lines
def tl(x):
    return 63 * x

# c for the irregular curve of the circle
def x(t, x_start, c_start):
    return sin(t/10) * x_start + cos(t/5) * c_start

def y(t, y_start):
    return cos(t/10) * y_start 

def x1(t, x_end, c_start):
    return sin(t/10) * x_end + cos(t/5) * c_start

def y1(t, y_end):
    return cos(t/10) * y_end

#gradient
def setGradient(x, y, w, h, c1, c2, axis):
    noFill()
    if axis == x_axis:
        for i in range(x, x+w):
            inter = map(i, x, x+w, 0, 1)
            c = lerpColor(c1, c2, inter)
            stroke(c)
            line(i, y, i, y+h)

def mousePressed():
    pauseFrame()
    saveFrame('movie_frames/treetrunk_SingleFrame/trunk_####.png')
    
def pauseFrame():
    delay(DELAY)
    
