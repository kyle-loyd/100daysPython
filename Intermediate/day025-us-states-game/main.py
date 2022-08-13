from turtle import Screen, shape
from writer import Writer
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
shape(image)

write = Writer()
data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
# failure = states[states.state == "Chicken"]

number_correct = 0
while number_correct < 50:
    answer_state = screen.textinput(title=f"{number_correct}/50 Guessed", prompt="Enter state name: ").title()
    state_data = data[data.state == answer_state]
    if state_data.empty:
        continue
    else:
        write.state(int(state_data.x), int(state_data.y), answer_state)
        number_correct += 1

screen.mainloop()
