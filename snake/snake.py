from turtle import Turtle, Screen
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.offset = 0
        for i in range(3):
            snake_segment = Turtle("square")
            snake_segment.color("green")
            snake_segment.penup()
            snake_segment.goto(self.offset, 0)
            self.segments.append(snake_segment)
            self.offset -= 20
        self.head = self.segments[0]

    def l(self):
        self.segments[0].left(90)

    def r(self):
        self.segments[0].right(90)

    def move(self):
        for segment in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment - 1].xcor()
            new_y = self.segments[segment - 1].ycor()
            self.segments[segment].goto(new_x, new_y)
        self.head.fd(MOVE_DISTANCE)

    def extend(self):
        snake_segment = Turtle("square")
        snake_segment.color("green")
        snake_segment.penup()
        new_x = self.segments[-1].xcor()
        new_y = self.segments[-1].ycor()
        snake_segment.goto(new_x, new_y)
        self.segments.append(snake_segment)