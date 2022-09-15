from turtle import Screen
import time
from collision_brain import DetectCollision
from score_modal import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Snake Game")
game_is_on = True
in_proximity = DetectCollision()
score = ScoreBoard()

while game_is_on:
    screen.update()
    time.sleep(0.15)
    score.current_score(in_proximity.score, in_proximity.high_score)
    in_proximity.move()
    if in_proximity.detect_food_hit():
        score.current_score(in_proximity.score, in_proximity.high_score)
    if in_proximity.detect_collision():
        in_proximity.reset()
        score.current_score(in_proximity.score, in_proximity.high_score)


screen.exitonclick()
