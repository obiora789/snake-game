from turtle import Turtle, Screen
TITLE_BUFFER = 79


class Snake:
    def __init__(self):
        self.screen = Screen()
        self.WALL = 350
        self.vertical_start = 0
        self.horizontal_start = 0
        self.turtle_list = self.create_new_snake("green")
        self.snake_head = self.turtle_list[0]
        self.RIGHT_ANGLE = 0
        self.UP_ANGLE = 90
        self.LEFT_ANGLE = 180
        self.DOWN_ANGLE = 270
        self.pace = 20
        self.extend_segment = self.turtle_list[-1]

    def create_new_snake(self, color):
        """This method creates the snake and assigns its color."""
        turtle_list = []
        pace = 20
        for turtle in range(3):
            new_turtle = self.add_segment(color)
            new_turtle.goto(self.horizontal_start - (pace * turtle), self.vertical_start)
            turtle_list.append(new_turtle)
        return turtle_list

    def add_segment(self, color):
        new_turtle = Turtle(shape="square")
        new_turtle.penup()
        new_turtle.speed(9)
        new_turtle.color(color)
        return new_turtle

    def extend_snake(self):
        new_segment = self.add_segment(color=self.extend_segment.color()[0])
        new_segment.setposition(self.extend_segment.position())
        return new_segment

    def move_up(self):
        """This method controls the upward movement of the snake."""
        if self.snake_head.heading() != self.DOWN_ANGLE:
            self.snake_head.setheading(self.UP_ANGLE)

    def move_right(self):
        """This method controls the right movement of the snake."""
        if self.snake_head.heading() != self.LEFT_ANGLE:
            self.snake_head.setheading(self.RIGHT_ANGLE)

    def move_down(self):
        """This method controls the downward movement of the snake."""
        if self.snake_head.heading() != self.UP_ANGLE:
            self.snake_head.setheading(self.DOWN_ANGLE)

    def move_left(self):
        """This method controls the left movement of the snake."""
        if self.snake_head.heading() != self.RIGHT_ANGLE:
            self.snake_head.setheading(self.LEFT_ANGLE)

    def null_function(self):
        """Null method for when the snake goes off the screen"""
        return

    def hold_wall(self):
        """This keeps the snake in its trajectory once snake is approaching the wall.
        This also repositions the snake to the other side of the screen once the snake hits the wall."""
        if self.snake_head.xcor() > self.WALL - 3 * self.pace or \
                self.turtle_list[0].xcor() < -self.WALL + 3 * self.pace:
            self.screen.listen()
            self.screen.onkey(fun=self.null_function, key="Up")
            self.screen.onkey(fun=self.null_function, key="Down")
        if self.turtle_list[0].ycor() > self.WALL - 3 * self.pace or \
                self.turtle_list[0].ycor() < -self.WALL + 3 * self.pace:
            self.screen.listen()
            self.screen.onkey(fun=self.null_function, key="Left")
            self.screen.onkey(fun=self.null_function, key="Right")

        for turtle in self.turtle_list:
            turtle.hideturtle()
            if turtle.xcor() > self.WALL:
                turtle.setx(-self.WALL)
            elif turtle.xcor() < -self.WALL:
                turtle.setx(self.WALL)
            elif turtle.ycor() > self.WALL - TITLE_BUFFER:
                turtle.sety(-self.WALL)
            elif turtle.ycor() < -self.WALL:
                turtle.sety(self.WALL - TITLE_BUFFER)
            turtle.showturtle()

    def move(self):
        """This method controls the general movement of the snake."""
        for turtle_num in range(len(self.turtle_list) - 1, 0, -1):
            x = self.turtle_list[turtle_num - 1].xcor()
            y = self.turtle_list[turtle_num - 1].ycor()
            self.turtle_list[turtle_num].goto(x, y)
            self.turtle_list[turtle_num - 1].forward(self.pace)
            if turtle_num == 0:
                self.turtle_list[turtle_num].forward(self.pace)

        self.screen.listen()
        self.screen.onkey(fun=self.move_up, key="Up")
        self.screen.onkey(fun=self.move_down, key="Down")
        self.screen.onkey(fun=self.move_left, key="Left")
        self.screen.onkey(fun=self.move_right, key="Right")
        self.hold_wall()
