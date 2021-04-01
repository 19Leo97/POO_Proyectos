canvasx=500
canvasy=400
lado=10

def setup():
    global canvasx,canvasy
    size(canvasx,canvasy)

def draw():
    global canvasx,canvasy,lado
    for hor in range(canvasx/lado):
        for ver in range(canvasy/lado):
            rect(hor*lado,ver*lado,lado,lado)
