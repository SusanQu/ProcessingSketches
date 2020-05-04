#########################################
# Triangle - Terrain
#########################################

scl = 20
moving = float(0)

def setup():
    size(800, 800, P3D)
    
    global w
    global h 
    global cols 
    global rows
    global terrain
    
    w = 1400
    h = 1200
    cols = w/scl
    rows = h/scl;
     
    terrain = [[0]*cols for i in range(cols+1)]

    

def draw():
    global moving
    
    moving = moving - 0.01
    
    yoff = moving
    for y in range(rows):
        xoff = float(0)
        for x in range(cols):
            terrain[x][y] = map(noise(xoff, yoff), 0, 1, -100, 100)
            xoff = xoff + 0.2
        yoff = yoff + 0.2

    background(28)
    stroke(255)
    noFill()
    
    translate(width/2, height/2)
    rotateX(PI/3)
    translate(-w/2, -h/2)
    
    for y in range(rows-1):
        beginShape(TRIANGLE_STRIP)
        for x in range(cols):
            vertex(x*scl, y*scl, terrain[x][y])
            vertex(x*scl, (y+1)*scl, terrain[x][y+1])

            #rect(x*scl, y*scl, scl, scl)
        endShape()
        
