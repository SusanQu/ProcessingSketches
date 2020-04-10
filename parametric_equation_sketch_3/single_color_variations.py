############################################################
#substitude these x, y, x1, y1 values in the processing
#sketch to get different effects
############################################################

############################################################
# 1. circle with horizontal line
############################################################
def x(t):
    return sin(t/10) * 200

def y(t):
    return cos(t/10)

def x1(t):
    return sin(t/10) * 200 + sin(t)*2 + sin(t)

def y1(t):
    return cos(t/10) * 200

############################################################
# 2. more true circle
############################################################
def x(t):
    return sin(t/10) * 200

def y(t):
    return cos(t)

def x1(t):
    return sin(t/10) * 200

def y1(t):
    return cos(t/10) * 200

############################################################
# 3. circle with horizontal line with up and down edge waves
############################################################
def x(t):
    return sin(t/10) * 200

def y(t):
    return cos(t/10)

def x1(t):
    return sin(t/10) * 200

def y1(t):
    return cos(t/20) * 200  + sin(t)* 20


############################################################
# 4. circle with horizontal line with back and forth edge waves
############################################################
def x(t):
    return sin(t/10) * 100

def y(t):
    return cos(t/10)

def x1(t):
    return sin(t/10) * 200

def y1(t):
    return cos(t/20) * 200 + sin(t)*5 + sin(t)* 25


############################################################
# 5. circle with diagonal line
############################################################
def x(t):
    return sin(t/10) * 200

def y(t):
    return cos(t/10) + sin(t/10)*100

def x1(t):
    return sin(t/10) * 200 + sin(t)*2 + sin(t)

def y1(t):
    return cos(t/10) * 200

############################################################
# 6. cone shape with horizontal line
#this one looks more stable when lines are increased to 100
############################################################
def x(t):
    return sin(t/10) * 100

def y(t):
    return cos(t/10)

def x1(t):
    return sin(t/10) * 200 + sin(t)*2 + sin(t)

def y1(t):
    return cos(t/20) * 200

############################################################
# 7. cone shape with diagonal line
#found this variation to be particularly interesting with more lines initially defined in the for loop ex:
# increase for i in range(50) to range(100)
############################################################
def x(t):
    return sin(t/10) * 100

def y(t):
    return cos(t/10) + sin(t/10)*100

def x1(t):
    return sin(t/10) * 200 + sin(t)*2 + sin(t)

def y1(t):
    return cos(t/20) * 200

############################################################
# 8. oval shape with diagonal line variation 1
#with more line range(100)
############################################################
def x(t):
    return sin(t/10) * 100

def y(t):
    return cos(t/10) + sin(t/10)*100 + cos(t/5) * 50

def x1(t):
    return sin(t/10) * 200 + sin(t)*2 + sin(t)

def y1(t):
    return cos(t/20) * 200

############################################################
# 9. oval shape with diagonal line variation 2
#with more line range(100)
############################################################
def x(t):
    return sin(t/10) * 100

def y(t):
    return cos(t/10) + sin(t/10)*100 + cos(t/10) * 100

def x1(t):
    return sin(t/10) * 200 + sin(t)*2 + sin(t)

def y1(t):
    return cos(t/20) * 200


############################################################
# 10. cork screw with diagonal line
#with more line range(100)
############################################################
def x(t):
    return sin(t/10) * 80

def y(t):
    return cos(t/10) + sin(t/10)*80 + cos(t/10) * 100 + sin(t/10)*250

def x1(t):
    return sin(t/10) * 200 + sin(t)*2 + sin(t)

def y1(t):
    return cos(t/20) * 200

############################################################
# 11. cork screw with diagonal line variation 1
#with more line range(100)
############################################################
def x(t):
    return sin(t/10) * 80

def y(t):
    return cos(t/10) + sin(t/10)*80 + cos(t/10) * 100 + sin(t/10)*250

def x1(t):
    return sin(t/10) * 200 + sin(t)*2 + sin(t)

def y1(t):
    return cos(t/20) * 200 + cos(t/10) * 100

############################################################
# 12. cynider with vertical lines variation 1
#with more line range(100)
############################################################
def x(t):
    return sin(t/10) * 80

def y(t):
    return cos(t/10) + sin(t/10)*80 + cos(t/10) * 100 + sin(t/10)*250

def x1(t):
    return sin(t/20) * 300

def y1(t):
    return cos(t/20) * 200 + cos(t/10) * 100 + sin(t/10)*150


############################################################
# 13. cynider with vertical lines variation 2
#with more line range(100)
############################################################
def x(t):
    return sin(t/10) * 80

def y(t):
    return cos(t/10) + sin(t/10)*80 + cos(t/10) * 100

def x1(t):
    return sin(t/20) * 300

def y1(t):
    return cos(t/20) * 200 + cos(t/10) * 100 + sin(t/10)*150
