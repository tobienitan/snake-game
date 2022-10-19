from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 23, 'normal')
from snake import Snake

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as data:
            self.highscore = int(data.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.write(f'highscore:{self.highscore} Score:{self.score}', align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f'highscore{self.highscore} Score:{self.score}', align=ALIGNMENT, font=FONT)



    def reset(self):
        if self.highscore < self.score:
            self.highscore = self.score
            with open('data.txt', 'w') as data:
                data.write(f'{self.highscore}')
        self.score = 0
        self.update_scoreboard()


    def increase_score(self):
        self.score += 1
        self.update_scoreboard()








