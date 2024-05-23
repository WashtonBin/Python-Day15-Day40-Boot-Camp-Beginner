import turtle
import pandas
ALIGNMENT = "center"
FONT = ('Courier', 10, 'normal')


screen = turtle.Screen()
screen.title("US. States Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

guess_states = []

while len(guess_states) < 50:
    answer_state = screen.textinput(title=f"{len(guess_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    # states to learn csv
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guess_states:
                missing_states.append(state)
        df = pandas.DataFrame(missing_states)
        df.to_csv("missing states.csv")
        break
    if answer_state in all_states:
        guess_states.append(answer_state)
        state_data = data[data.state == answer_state]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(state_data.x.iloc[0]), int(state_data.y.iloc[0]))
        t.write(state_data.state.item())









screen.exitonclick()





# def get_mouse_click_coor(x, y):
#     print(x, y)
#
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()



