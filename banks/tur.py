import turtle

silly = turtle.Turtle()
i = 0

#four incresing size squares
while i < 4:
    silly.forward(50*(i+1))
    silly.right(90)     # Rotate clockwise by 90 degrees

    silly.forward(50*(i+1))
    silly.right(90)

    silly.forward(50*(i+1))
    silly.right(90)

    silly.forward(50*(i+1))
    silly.right(90)
    i +=1

#circle
silly.circle(100)

turtle.done()