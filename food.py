from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.usable_screen = 280
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_len=0.4, stretch_wid=0.4)
        self.penup()
        self.refresh()
        self.title_buffer = 20

    def refresh(self):
        food_x = random.randrange(-self.usable_screen, self.usable_screen, 1)
        food_y = random.randrange(-self.usable_screen, self.usable_screen - 20, 1)
        self.goto(food_x, food_y)
