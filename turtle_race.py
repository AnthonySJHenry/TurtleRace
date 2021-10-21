from turtle import *
import random

race_started = False
colors = ["brown", "blue", "orange", "purple", "pink"]
positions = [-280, -140, 0, 140, 280]
turtles = []
mode("logo") # turtles will face north

def start_race(guess):
    race_started = True
    while(race_started):
        for turtle in turtles:
            distance_to_move = random.randint(0, 10)
            turtle.forward(distance_to_move)
        
            if turtle.ycor() >= 350 and race_started:
                race_started = False
                winning_color = turtle.color()[0]               
                if winning_color == guess:
                    s.bgcolor("green")
                    print("You were right!", winning_color.capitalize(), "won!")
                else:
                    s.bgcolor("red")
                    print("Sorry.", guess.capitalize(), "did not win.", winning_color.capitalize(), "won.")
                

def make_guess():
    for turtle in range(0, 5):
        t = Turtle(shape="turtle")
        t.color(colors[turtle])
        t.penup()# if this were not here, turtles would leave lines wherever they go
        t.goto(positions[turtle], -300)
        turtles.append(t)
    guess = s.textinput("Who will win?" , "Guess:")
    if guess:
        guess = guess.lower()
        start_race(guess)

s = Screen()
s.setup(700, 700)
s.ontimer(make_guess, 1000)
s.exitonclick()

