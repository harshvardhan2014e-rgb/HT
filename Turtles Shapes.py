import turtle

turtle.Screen().bgcolor("#08bfad")
board = turtle.Turtle()

pen = turtle.Turtle()

# Draw a square
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)
pen.forward(100)
pen.right(90)

# Draw a rectangle
pen.forward(150)
pen.right(90)
pen.forward(80)
pen.right(90)
pen.forward(150)
pen.right(90)
pen.forward(80)
pen.right(90)

turtle.done()             


