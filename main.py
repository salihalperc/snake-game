from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

import time
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("My snack game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()


screen.listen()
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.snake_left, "Left")
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect the collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.add_score()
        score_board.update_scoreboard()

    #Detect the collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score_board.reset()
        snake.reset()

    my_segments = snake.squares[1::1]
    for _ in my_segments:
        if snake.head.distance(_) < 10: 
            game_is_on = False
            score_board.reset()
            snake.reset()

screen.exitonclick()