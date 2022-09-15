from food import Food
import threading
import time
from snake import Snake
from big_food import BigFood


class DetectCollision(Snake):
    def __init__(self):
        super().__init__()
        self.IDEAL_TIME = 50
        self.count = 1
        self.food = Food()
        self.big_food = BigFood()
        self.hit_food = False
        self.score = 0
        self.boost = 100
        self.timer = 50
        self.pace = 20
        self.high_score = self.read_high_score()

    def read_high_score(self):
        """This method reads the high score from a local file stored in your PC."""
        with open("data.txt", mode="r") as file:
            h_score = int(file.read())
        return h_score

    def countdown_timer(self):
        """Handles the duration the big food remains on the screen.
        It does an extra job of detecting any collision"""
        self.hit_food = False
        while self.timer > 0 and not self.hit_food:
            time.sleep(0.1)
            self.timer -= 1
            if self.snake_head.distance(self.big_food) < self.pace:
                self.hit_food = True
                if self.timer >= self.IDEAL_TIME / 2:
                    self.score += self.boost
                elif self.timer >= self.IDEAL_TIME / 5:
                    self.score += self.boost / 2
                else:
                    self.score += self.boost / 5
        self.big_food.hideturtle()

    def detect_food_hit(self):
        """This function detects when the snake is in contact with any pellet,
        and adds it to the snake accordingly."""
        if self.snake_head.distance(self.food) < self.pace:
            self.hit_food = True
            if self.count % 5 != 0 or self.count == 0:
                self.food.hideturtle()
                self.turtle_list.append(self.extend_snake())
                self.score += 3
            else:
                self.food.hideturtle()
            self.hit_big_food()
            self.count += 1
            self.food = Food()
        return self.hit_food

    def hit_big_food(self):
        """This function detects big food and activates the countdown.
        It resets the timer after the snake has either collided or missed the big food."""
        t1 = threading.Thread(target=self.countdown_timer)
        if self.count % 5 == 0 and self.count != 0:
            self.big_food.showturtle()
            if self.timer > 0:
                t1.start()
        elif self.timer < 50 and self.count % 5 == 1:
            self.timer = 50
        return self.hit_food

    def detect_collision(self):
        """Detects when snake's head is in contact with any part of the snake."""
        new_list = self.turtle_list[1:]
        for num in range(len(new_list)):
            segment = new_list[num]
            if self.snake_head.distance(segment) < 1:
                return True

    def reset(self):
        """This method activates once the snake head collides with any other part of its body"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                h_score = int(self.high_score)
                file.write(str(h_score))
        self.score = 0
        self.count = 1
        new_list = self.turtle_list[:3]
        for turtle in self.turtle_list:
            turtle.hideturtle()
        self.turtle_list = new_list
