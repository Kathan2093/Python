from turtle import Turtle
position = [(0, 0), (-20, 0), (-40, 0)]
segment = []
distance = 20
down = 270
up = 90
left = 180
right = 0


class Snake():
    def __init__(self):
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for i in position:
            self.add_segment(i)

    def reset(self):
        for i in self.segment:
            i.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def add_segment(self, i):
        snake = Turtle('square')
        snake.color('white')
        snake.penup()
        snake.goto(i)
        self.segment.append(snake)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def move(self):
        for i in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[i - 1].xcor()
            new_y = self.segment[i - 1].ycor()
            self.segment[i].goto(new_x, new_y)
        self.head.forward(distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
