import turtle
import pandas

screen = turtle.Screen()
screen.title("US STATES GAME")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tom = turtle.Turtle()
tom.penup()
tom.hideturtle()

state_data = pandas.read_csv("50_states.csv")
state_list = state_data["state"].to_list()
unanswered_states = state_list

total = 50
score = 0
while score < total:
    answer_state = screen.textinput(title=f"{score}/{total} States Correct", prompt="Enter value:").title()

    if answer_state == "Exit":
        break

    if answer_state in state_list:
        state_answered = state_data[state_data["state"] == answer_state]
        new_x = int(state_answered.x)
        new_y = int(state_answered.y)
        tom.setpos(new_x, new_y)
        tom.write(answer_state)
        score += 1
        print(answer_state)
        unanswered_states.remove(answer_state)

# print(unanswered_states)
data = pandas.DataFrame(unanswered_states)
# print(data)
data.to_csv("states_to_learn.csv")
