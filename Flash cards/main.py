from tkinter import *
import pandas
from random import choice
to_learn_dic = {}
current_card = {}
try:
    data = pandas.read_csv("words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("french_words.csv")
    to_learn_dic = original_data.to_dict(orient="records")
else:
    to_learn_dic = data.to_dict(orient="records")


def flip_card():
    canvas.itemconfig(back_ground,image=back_photo)
    canvas.itemconfig(card_title,fill="white", text="English")
    canvas.itemconfig(card_word,fill="white", text=current_card["English"])


def next_card():
    global current_card, flip_timer, to_learn_list
    canvas.after_cancel(flip_timer)
    current_card = choice(to_learn_dic)
    canvas.itemconfig(card_title, text="French")
    canvas.itemconfig(card_word,text=current_card["French"])
    canvas.itemconfig(back_ground, image=front_Photo)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    flip_timer = window.after(3000, flip_card)


def is_known():
    to_learn_dic.remove(current_card)
    data = pandas.DataFrame(to_learn_dic)
    data.to_csv("words_to_learn.csv", index=False)
    next_card()

# Window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg="#B1DDC6")
flip_timer = window.after(3000, flip_card)
# Front canvas
back_photo = PhotoImage(file="card_back.png")
front_Photo = PhotoImage(file="card_front.png")
canvas = Canvas(width =800, height=526)
back_ground = canvas.create_image(400, 263, image=front_Photo)
card_title = canvas.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg="#B1DDC6", highlightthickness=0)
canvas.grid(row=0, column=0,columnspan=2)
# Wrong Button
wrong = PhotoImage(file="wrong.png")
button_wrong = Button(image=wrong, highlightthickness=0, command=next_card)
button_wrong.grid(row=1, column=0)
# Right Button
right = PhotoImage(file="right.png")
button_right = Button(image=right, highlightthickness=0, command=is_known)
button_right.grid(row=1, column=1)

next_card()

window.mainloop()
