from turtle import  Screen
from border import Border
from snake import Snake
from food import Food
from Scoreboard import  Scoreboard
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

snake=Snake()
food=Food()
scores=Scoreboard()
border=Border()


screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

# Main game loop
game = True
while game:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #collision between food and sanke
    if snake.head.distance(food)<15:
        food.refresh()
        snake.extend()
        scores.on_board()
     
    #collision with the wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scores.game_over()
        game=False
    
    #collision with the segment
    for segment in snake.segments[1:]:
        # if segment==snake.head:
        #     pass
        if snake.head.distance(segment)<10:
            scores.game_over()
            game=False


screen.exitonclick()
