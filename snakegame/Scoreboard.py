from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.score=0
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write(arg="GAME OVER!!!",align="center",font=("Arial",24,"normal"))

    def update_scoreboard(self):
        self.write(arg=f"Score:{self.score} ",align="center",font=("Arial",24,"normal"))

    def on_board(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()
       

