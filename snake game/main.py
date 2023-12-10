from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time


my_Screen = Screen()
my_Screen.setup(width=600, height=600)
my_Screen.bgcolor('black')
my_Screen.title("Snake Game")
my_Screen.listen()
my_Screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

my_Screen.onkey(snake.up, "w")
my_Screen.onkey(snake.down, "s")
my_Screen.onkey(snake.right, "d")
my_Screen.onkey(snake.left, "a")
game_on = True
while game_on:
    my_Screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        food.refresh()
        score.increase_score()

    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        score.reset()

    for i in snake.segment[1:]:
        if snake.head.distance(i) < 10:
            snake.reset()
            score.reset()


my_Screen.exitonclick()
