from food import Food


class BigFood(Food):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shapesize(stretch_wid=1.5, stretch_len=1.5)
        self.hideturtle()
