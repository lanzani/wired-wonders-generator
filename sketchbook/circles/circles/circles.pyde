w, h = 1000, 1000


def deformed_circle(x, y, r, deformation):
    translate(x, y)
    
    points = []
    for i in range(0, 360, 15):
        points.append((r/2*sin(radians(i)), r/2*cos(radians(i))))
        
    # Create the deformed circle
    final = []
    for p in points:
        x_change = p[0] / 55.0
        y_change = p[1] / 55.0
        
        change = random(-deformation, deformation)
        p = (p[0] + x_change * change, p[1] + y_change * change)
        final.append(p)
        
    beginShape()
    fill(0)
    for p in final:
        curveVertex(*p)
    curveVertex(*final[0])
    curveVertex(*final[1])
    curveVertex(*final[2])
    endShape()


def setup():
    size(w, h)
    
    background(255)
    strokeWeight(4)
    noFill()
    
    deformed_circle(500, 500, 300)
