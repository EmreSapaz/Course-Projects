import time
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States")
screen.setup(725,491)
image = "states.gif"
screen.register_shape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
state_list = data.state.to_list()
guessed_states = set()

while len(guessed_states) < 50:

    user_answer = screen.textinput(f"{len(guessed_states)}/50 States Correct","Enter the State name").title()

    if user_answer == "Exit":
        missing_states = []
        for state in state_list:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        break

    if user_answer in state_list:
        if user_answer in guessed_states:
            f = turtle.Turtle()
            f.hideturtle()
            f.penup()
            f.goto(0,215)
            f.write("Already Guessed",align="center",font=("Arial", 20, "normal"))
            time.sleep(1.5)
            f.clear()

        else:
            guessed_states.add(user_answer)
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state_data = data[data.state == user_answer]
            t.goto(state_data.x.item(),state_data.y.item())
            t.write(user_answer,False,"center")
            time.sleep(1)
    else:
        g = turtle.Turtle()
        g.hideturtle()
        g.penup()
        g.goto(0, 180)
        g.write("Wrong!!", align="center", font=("Arial", 40, "normal"))
        time.sleep(1.5)
        g.clear()
