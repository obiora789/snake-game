from turtle import Turtle
CURRENT_SCORE_FONT = ("Courier", 14, "normal")
ALIGNMENT = "center"
FINAL_SCORE_FONT = ('Arial', 28, 'bold')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(4, 30, 12)
        self.shape("square")
        self.penup()
        self.hideturtle()
        self.goto(0, 280)

    def current_score(self, score, high_score):
        """This method displays the current score at the top of the screen"""
        self.clear()
        self.goto(-10, 280)
        self.write(f"Current Score: {int(score)}  High Score: {int(high_score)}",
                   move=False, align=ALIGNMENT, font=CURRENT_SCORE_FONT)

    def final_score(self, score):
        """This method displays the final score on the screen."""
        self.clear()
        self.goto(0, 0)
        self.write(f"Game Over! The final score is {int(score)}.", move=False, align=ALIGNMENT,
                   font=FINAL_SCORE_FONT)


