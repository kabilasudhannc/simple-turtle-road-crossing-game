from turtle import Turtle

POSITION = (-250, 250)


class ScoreBoard(Turtle):
    def __init__(self):
        self.level = 1
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('black')
        self.goto(POSITION)
        self.write(arg=f'Level: {self.level}', move=False, align='center', font=('Arial', 15, 'normal'))
        self.move_speed = 0.1

    def next_level(self):
        self.clear()
        self.level += 1
        self.write(arg=f'Level: {self.level}', move=False, align='center', font=('Arial', 15, 'normal'))
        self.move_speed *= 0.9

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f'Game Over.', move=False, align='center', font=('Arial', 15, 'normal'))
