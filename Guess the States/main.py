import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pd.read_csv("50_states.csv")
states = data.state.tolist()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"Guessed States: {len(guessed_states)}/50",
                                    prompt="What's another state's name? (Type 'End' to finish)").title()
    if answer_state == "End":
        remaining_states = set(states) - set(guessed_states)
        new_values = pd.DataFrame(remaining_states, columns=["State"])
        new_values.to_csv("states_to_learn.csv", index=False)
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        state_data = data[data.state == answer_state].iloc[0]
        x = int(state_data.x)
        y = int(state_data.y)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.pendown()
        t.write(answer_state, align="center", font=("Arial", 8, "normal"))
        t.penup()


