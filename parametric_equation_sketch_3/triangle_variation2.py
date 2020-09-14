#########################################
# Triangle
#########################################

t = 0
num_tris = 90

def setup():
    size(800, 800)

def draw():
    global t
    background(242, 242, 242)
    translate(width/2, height/2)
    noFill()
    stroke(51, 51, 51)

    for i in range(num_tris):
        rotate(radians(360/num_tris))
        strokeWeight(1)
        pushMatrix()
        translate(200, 0)
        rotate(radians(t+60/num_tris))
        tri(50, t/2)
        popMatrix()

    t += 0.2

def tri(length, t):
    strokeJoin(ROUND)
    strokeCap(ROUND)
    triangle(0, sin(t/20) * 500,
             -length*sqrt(3)/2, length/2,
             length*sqrt(6)/2, length/2)
