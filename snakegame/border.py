from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-280,-280)
        self.pendown()
        self.square()

    def square(self):
        for i in range(4):
            self.forward(560)
            self.left(90)
    
    

   
