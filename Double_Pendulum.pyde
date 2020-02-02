x1 = 0
x2 = 0
x1p = 0
x2p = 0
y1 = 0
y1p = 0
y2 = 0
y2p = 0
a1 = PI
a2 = PI/2
v1 = 0
v2 = 0
ac1 = 0
ac2 = 0
l1 = 300
l2 = 450
m1 = 100
m2 = 100
g = 0.7
trailx = []
traily = []
counter = 0

mode = 1


def setup ():
    size (1800,1500)
    background(255)
    frameRate(60)
def draw():
    global a1, a2, v1, v2, x1, x2, ac1, ac2, l1, l2, trailx, traily, counter, x1p, x2p, y1p, y2p
    if mode == 1:
        translate(width/2,500)
        num1 = -1*g*(2*m1 + m2)*sin(a1)
        num2 = -1*m2*g*sin(a1 - 2*a2)
        num3 = -1*2*sin(a1-a2)*m2
        num4 = (v2*v2*l2 + v1*v1*l1*cos(a1-a2))
        numerator1 = num1 + num2 + num3*num4
        denominator1 = l1 * (2*m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
        ac1 = numerator1/denominator1
        num5 = 2*sin(a1-a2)
        num6 = v1*v1*l1*(m1 + m2)
        num7 = g*(m1+m2)*cos(a1)
        num8 = v2*v2*l2*m2*cos(a1-a2)
        numerator2 = num5*(num6+num7+num8)
        denominator2 = l2*(2*m1 + m2 - m2*cos(2*a1 - 2*a2))
        ac2 = numerator2/denominator2
        x1 = l1*sin(a1)
        y1 = l1*cos(a1)
        x2 = x1 + l2*sin(a2)
        y2 = y1 + l2*cos(a2)
        v1 += ac1
        v2 += ac2
        a1 += v1
        a2 += v2
        background(255)
        fill (0)
        line(0,0,x1,y1)
        ellipse(x1,y1,m1,m1)
        line(x1,y1,x2,y2)
        ellipse(x2,y2,m2,m2)
        stroke (2)    
        #trailx.append(x2)
        #traily.append(y2)
        
        # for i in range (0,counter):
        #     ellipse(trailx[i], traily[i], 1, 1)
        #     stroke (0)
        #     i+=1
            
        #counter += 1 
    elif mode == 2:
        translate(width/2,height/2)
        num1 = -1*g*(2*m1 + m2)*sin(a1)
        num2 = -1*m2*g*sin(a1 - 2*a2)
        num3 = -1*2*sin(a1-a2)*m2
        num4 = (v2*v2*l2 + v1*v1*l1*cos(a1-a2))
        numerator1 = num1 + num2 + num3*num4
        denominator1 = l1 * (2*m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
        ac1 = numerator1/denominator1
        num5 = 2*sin(a1-a2)
        num6 = v1*v1*l1*(m1 + m2)
        num7 = g*(m1+m2)*cos(a1)
        num8 = v2*v2*l2*m2*cos(a1-a2)
        numerator2 = num5*(num6+num7+num8)
        denominator2 = l2*(2*m1 + m2 - m2*cos(2*a1 - 2*a2))
        ac2 = numerator2/denominator2
        x1 = l1*sin(a1)
        y1 = l1*cos(a1)
        x2 = x1 + l2*sin(a2)
        y2 = y1 + l2*cos(a2)
        v1 += ac1
        v2 += ac2
        a1 += v1
        a2 += v2
        fill (0)
        ellipse(x1,y1,2,2)
        ellipse(x2,y2,2,2)
        stroke (2)
    elif mode == 3:
        translate(width/2,500)
        num1 = -1*g*(2*m1 + m2)*sin(a1)
        num2 = -1*m2*g*sin(a1 - 2*a2)
        num3 = -1*2*sin(a1-a2)*m2
        num4 = (v2*v2*l2 + v1*v1*l1*cos(a1-a2))
        numerator1 = num1 + num2 + num3*num4
        denominator1 = l1 * (2*m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
        ac1 = numerator1/denominator1
        num5 = 2*sin(a1-a2)
        num6 = v1*v1*l1*(m1 + m2)
        num7 = g*(m1+m2)*cos(a1)
        num8 = v2*v2*l2*m2*cos(a1-a2)
        numerator2 = num5*(num6+num7+num8)
        denominator2 = l2*(2*m1 + m2 - m2*cos(2*a1 - 2*a2))
        ac2 = numerator2/denominator2
        x1 = l1*sin(a1)
        y1 = l1*cos(a1)
        x2 = x1 + l2*sin(a2)
        y2 = y1 + l2*cos(a2)
        v1 += ac1
        v2 += ac2
        a1 += v1
        a2 += v2
        fill (0)
        if counter != 0:
            line (x2,y2, x2p, y2p)
            strokeWeight(3)
        stroke (2)
        x1p = x1
        x2p = x2
        y1p = y1
        y2p = y2
        counter += 1
    if mode == 4:
        translate(width/2,height/2)
        num1 = -1*g*(2*m1 + m2)*sin(a1)
        num2 = -1*m2*g*sin(a1 - 2*a2)
        num3 = -1*2*sin(a1-a2)*m2
        num4 = (v2*v2*l2 + v1*v1*l1*cos(a1-a2))
        numerator1 = num1 + num2 + num3*num4
        denominator1 = l1 * (2*m1 + m2 - m2 * cos(2 * a1 - 2 * a2))
        ac1 = numerator1/denominator1
        num5 = 2*sin(a1-a2)
        num6 = v1*v1*l1*(m1 + m2)
        num7 = g*(m1+m2)*cos(a1)
        num8 = v2*v2*l2*m2*cos(a1-a2)
        numerator2 = num5*(num6+num7+num8)
        denominator2 = l2*(2*m1 + m2 - m2*cos(2*a1 - 2*a2))
        ac2 = numerator2/denominator2
        x1 = l1*sin(a1)
        y1 = l1*cos(a1)
        x2 = x1 + l2*sin(a2)
        y2 = y1 + l2*cos(a2)
        v1 += ac1
        v2 += ac2
        a1 += v1
        a2 += v2
        background(255)
        fill (0)
        line(0,0,x1,y1)
        ellipse(x1,y1,m1,m1)
        line(x1,y1,x2,y2)
        ellipse(x2,y2,m2,m2)
        trailx.append(x2)
        traily.append(y2)
        stroke(0)
        noFill()
        beginShape()
        for i in range (0,counter):
            vertex(trailx[i], traily[i],)
            stroke (0)
            i+=1
        counter += 1 
        endShape()
    
    
