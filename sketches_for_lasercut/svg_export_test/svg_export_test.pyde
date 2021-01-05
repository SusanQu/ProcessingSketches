#########################################
# sketches for laser cutting
#########################################
add_library('svg')
print PGraphicsSVG


record = bool()
print('0')
print(bool(record))

def setup():
    background(242, 242, 242)
    size(800, 800)


def draw():

    global record
    
    if record:
        print('A')
        beginRecord(SVG, 'svg/frame-####.svg')

    line(mouseX, mouseY, width/2, height/2)
    
    if record:
        print('B')
        endRecord()
        record = False
    
def mousePressed():
    global record
    record = True
    print('C', record)
