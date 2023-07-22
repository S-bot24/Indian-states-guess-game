from turtle import Turtle, Screen
import pandas


screen = Screen()
screen.title("India Sates Game")
image = "map_of_india.gif"
screen.addshape(image)
t = Turtle()

t.shape(image)

data = pandas.read_csv("28_states_8_UTs.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 36:

    answer_state = screen.textinput(title=f"{len(guessed_states)}/36 (states and UTs) correct!",prompt="What's another state's name: ").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("Learn missing states.csv")

        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        S = Turtle()
        S.hideturtle()
        S.penup()
        state_data = data[data.state == answer_state]
        S.goto(int(state_data.x), int(state_data.y))
        S.write(answer_state,font=("Arial", 6, "normal"))

    if len(guessed_states) == 36:
        final_message_turtle = Turtle()
        final_message_turtle.hideturtle()
        final_message_turtle.penup()
        final_message_turtle.goto(0, 250)
        final_message_turtle.write("Hurry!! You Have Guessed All The States.", align="center", font=("Arial", 12, "bold"))




screen.exitonclick()
