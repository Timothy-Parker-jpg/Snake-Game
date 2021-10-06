from turtle import Screen
import time
from snake import Snake
from food import Food
from score import Score
from border import Border


screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
screen.listen()

score = Score()
snake = Snake()
food = Food()
border = Border()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        score.score += 1
        score.write_score()
        snake.extend()

    if snake.head.xcor() in [300, -300] or snake.head.ycor() in [300, -300]:
        score.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 15:
            game_is_on = False
            score.game_over()

    screen.onkeypress(snake.l, 'a')
    screen.onkeypress(snake.r, 'd')

screen.exitonclick()
