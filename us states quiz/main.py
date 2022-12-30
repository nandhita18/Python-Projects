import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image= "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guessed_state =[]


#extracting state names:

data = pandas.read_csv("50_states.csv")
state = list(data["state"])
while len(guessed_state) < 50:
    inpt = screen.textinput(title=f"{len(guessed_state)}/50 states guessed correctly",
                                    prompt="What's another state's name?")
    answer_state = inpt.title()
    if answer_state == "Exit":
        missing_states = []
        for i in state:
            if i not in guessed_state:
                missing_states.append(i)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in state:
        guessed_state.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        coordinate = data[data.state == answer_state]
        t.goto(int(coordinate.x), int(coordinate.y))
        t.write(answer_state)





screen.exitonclick()
