#########################################
# Lines and Dots
#########################################

t = 0
DELAY = 5 * 100
recording = False

def setup():
    background(31, 65, 59) #green
    size(800, 800)

def keyPressed():
    global recording
    
    if (key == 'r' or key == 'R'):
        recording = not recording
        print('recording: ' + str(bool(recording)))


def draw():
    background(31, 65, 59)
    #background(31, 65, 88) #blue
    
    global t

    translate(width / 2, height / 2)
    scale(0.75)

    for i in range(100):
        stroke(192, 155, 146)
        #stroke(243, 182, 162) #brighter pink
        strokeWeight(2)
        line(x(t + i), y(t + i), x1(t + i), y1(t + i))

    for i in range(50):
        stroke(255, 186, 69)
        strokeWeight(7)
        point(x3(t + i), y3(t + i))

    if (recording == True):
        saveFrame('movie_frames/lineDots_FrameOutput/lineDots_####.png')

    
    t = t + 0.135
    #t = t + 0.5

def mousePressed():
    pauseFrame()
    saveFrame('movie_frames/lineDots_SingleFrame/lineDots_####.png')

def pauseFrame():
    delay(DELAY)

def x(t):
    return sin(t / 10) * 80

def y(t):
    return cos(t / 10) + sin(t / 10) * 80 + cos(t / 10) * 100 + sin(t / 10) * 250

def x1(t):
    return sin(t / 10) * 200 + sin(t) * 2 + sin(t)

def y1(t):
    return cos(t / 20) * 200




def x3(t):
    return sin(-t / 10) * 250

def y3(t):
    return cos(t / 20) * 160
