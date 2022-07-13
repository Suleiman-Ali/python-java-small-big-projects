from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
reset_time = None

# --------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    global reps
    global marks
    window.after_cancel(reset_time)
    reps = 0
    timer.config(text="Timer", fg=RED, font=(FONT_NAME,30, "bold"), bg=YELLOW)
    check_mark.config(text="",fg=RED, font=(FONT_NAME,20,"bold"),bg=YELLOW)
    canvas.itemconfig(timer_text, text="00:00")




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 == 0:
        timer.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    elif reps % 8 == 0:
        timer.config(text="Long Break", fg=RED)
        count_down(long_break_sec)
    else:
        timer.config(text="Work", fg=GREEN)
        count_down(work_sec)




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(number):
    global reps
    global reset_time
    global marks
    if number >= 0:
        min = math.floor(number / 60)
        sec = number % 60
        if sec == 0:
            sec = "00"
        elif sec < 10:
            sec = f"0{sec}"
        canvas.itemconfig(timer_text, text=f"{min}:{sec}")
        reset_time = window.after(1000, count_down, number - 1)
    else:
        start_timer()
        num_of_sessions = math.floor(reps/2)
        marks = ""
        for i in range(num_of_sessions):
            marks += "✔"
        check_mark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
# Window
window = Tk()
window.title("Pomodoro Timer.")
window.config(padx=100, pady=50, bg=YELLOW)
# Canvas
image = PhotoImage(file="tomato.png")
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)
# Timer label
timer = Label(text="Timer", fg=RED, font=(FONT_NAME,30, "bold"), bg=YELLOW)
timer.grid(column=1, row=0)
# Check mark label
check_mark = Label(fg=RED, font=(FONT_NAME,20,"bold"),bg=YELLOW)
check_mark.grid(column=1, row=4)
# button for start
start = Button(text="Start", highlightthickness=0, command=start_timer)
start.grid(column=0, row=3)
# button for reset
reset = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=3)
window.mainloop()
