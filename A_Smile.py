from turtle import *

class Face:
    def draw_face(self):
        penup()
        goto(0, -100)
        pendown()
        circle(100)
    def draw_eyes(self):
        penup()
        goto(-35, 40)
        pendown()
        dot(20)

        penup()
        goto(35, 40)
        pendown()
        dot(20)
    def draw_nose(self):
        penup()
        goto(0, 20)
        pendown()

        goto(-10, -20)
        goto(10, -20)
        goto(0, 20)
    def draw_mouth(self):
        penup()
        goto(-40, -50)
        setheading(-60)
        pendown()
        circle(50, 120)

face = Face()
face.draw_face()
face.draw_eyes()
face.draw_nose()
face.draw_mouth()
        