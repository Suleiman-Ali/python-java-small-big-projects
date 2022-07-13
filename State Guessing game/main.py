import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
data = pandas.read_csv("50_states.csv")
indx = [s for s in data["state"]]
x = [a for a in data["x"]]
y = [f for f in data["y"]]
index = 0
doc = []
for o in indx:
   o = {
        "state": o,
        "x": x[index],
        "y": y[index]
   }
   index +=1
   doc.append(o)
Game_is_on = True
number_user_got = 0
total = 50
list = []
last_list = []
while Game_is_on:
    guess = turtle.textinput(f"{number_user_got}/{total} state correct:", "Enter state Name:")
    for indx in doc:
        if guess.title() == indx["state"] and indx["state"] not in list:
            t = turtle.Turtle()
            t.penup()
            t.color("Black")
            t.hideturtle()
            t.goto(x=indx["x"], y=indx["y"])
            t.write(indx["state"], False, "center", ("Arial", 8, "normal"))
            number_user_got += 1
            list.append(indx["state"])
            if number_user_got == 50:
                Game_is_on = False
    if guess.title() == "Exit":
        for n in data["state"]:
            if n not in list:
                last_list.append(n)
        d = pandas.DataFrame(last_list)
        d.to_csv("MissingStates.csv")
        Game_is_on = False




