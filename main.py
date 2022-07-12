from turtle import Turtle, Screen
from random import randint

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title= "Make your bet", prompt="Which turtle win the race? Enter a color : ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=-100 + turtle_index * 40)
    all_turtles.append(new_turtle)



if user_bet:
    is_race_on = True
while is_race_on :


    for turtle in all_turtles:
        if turtle.xcor() > 230 :
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print(f"it is right. {winning_color} is the winner" )
            else :
                print(f"you lose. {winning_color} is the winner")
        rand_distance = randint(0, 10)
        turtle.forward(rand_distance)








screen.exitonclick()