from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('black')
        self.goto(x=0, y=-280)
        self.setheading(90)

    def move(self):
        new_y = self.ycor() + 10
        self.goto(0, new_y)