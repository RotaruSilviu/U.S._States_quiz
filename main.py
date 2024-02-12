import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Quiz")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

text_turtle = turtle.Turtle()
text_turtle.hideturtle()
text_turtle.penup()

data = pandas.read_csv("50_states.csv")

all_states = data.state.to_list()
guessed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another states's name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    for pos in all_states:
        if pos == answer_state:
            guessed_states.append(pos)
            title = data[data.state == pos]
            x_cor_state = int(title.x.iloc[0])
            y_cor_state = int(title.y.iloc[0])
            text_turtle.goto(x_cor_state, y_cor_state)
            text_turtle.write(pos, align="center", )
