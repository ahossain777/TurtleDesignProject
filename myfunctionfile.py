#Create a polygon function that accepts a turtle, side, and distance.
#myfunctions file
def polygon (t,s,d) : #parameters -> (information)        
    a = 360/s #angle variables is inside the function
    t.begin_fill()
    for times in range (s) :
        t.forward(d)
        t.right(a)
        
    t.end_fill()

def  jump (t,x,y) :
    t.penup()
    t.goto(x,y)
    t.pendown()

def cool (t,d,c1,c2) :
    t.color(c1)
    polygon (t,4,d)
    t.color(c2)
    polygon (t,3,d)

def circle (t,r,c) :
    t.begin_fill()
    t.color(c) 
    t.circle(r)
    t.end_fill()
    
def circle2 (t,r,c2) :
    t.begin_fill()
    t.color(c2) 
    t.circle(r)
    t.end_fill()

def circle3 (t,r,c3) :
    t.begin_fill()
    t.color(c3) 
    t.circle(r)
    t.end_fill()

def circle4 (t,r,c4) :
    t.begin_fill()
    t.color(c4)
    t.circle(r)
    t.end_fill()
    
def rc (t,r,d) :
    for times in range(20):
        t.begin_fill()
        t.circle(r)
        t.forward(d)
        t.left(times)
        t.end_fill()

def lc (t,r,d) :
    for times in range(20):
        t.begin_fill()
        t.circle(r)
        t.forward(d)
        t.right(times)
        t.end_fill()

def ro (t) :
    t.begin_fill()
    rc(t,1,27)
    rc(t,1,24)
    t.end_fill()






    

    




