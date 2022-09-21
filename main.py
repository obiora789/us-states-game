import turtle
import pandas
ALIGNMENT = "center"
FONT = ('Arial', 10, 'normal')
FINAL_FONT = ('Courier', 20, 'normal')
NUMBER_OF_STATES = 50

screen = turtle.Screen()
write_answer = turtle.Turtle()
write_answer.penup()
write_answer.hideturtle()
screen.title("United States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
# def get_click_coordinates(x, y):
# this method gets the x and y coordinates from the clicked location and prints it to the console
#    print(x, y)
# turtle.onclick(get_click_coordinates)

states_data = pandas.read_csv("50_states.csv")
list_of_states = states_data.state.tolist()
guessed_states = []
game_is_on = True
while game_is_on:
    if len(guessed_states) > 0:
        answer = screen.textinput(title=f"{len(guessed_states)}/{NUMBER_OF_STATES} States Correct",
                                  prompt="Guess another State name").title()
    else:
        answer = screen.textinput(title="Guess the State", prompt="Guess another State name").title()
    if answer in list_of_states:
        answer_row = states_data[states_data["state"] == answer]
        answer_x = int(answer_row.x)
        answer_y = int(answer_row.y)
        write_answer.goto(answer_x, answer_y)
        write_answer.write(arg=answer, move=False, align=ALIGNMENT, font=FONT)
        list_of_states.remove(answer)
        guessed_states.append(answer)
    elif answer == "Exit":
        game_is_on = False
        missed_states = {
            "States Not Guessed": list_of_states,
        }
        guessed_data = pandas.DataFrame(missed_states)
        guessed_data.to_csv("states_missed.csv")
    elif len(guessed_states) == NUMBER_OF_STATES:
        game_is_on = False
        turtle.write(arg="Congrats on guessing all states", align="center", font=FINAL_FONT)
    print(len(list_of_states), len(guessed_states))
