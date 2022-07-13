from tkinter import *
THEME_COLOR = "#375362"
from quiz_brain import QuizBrain

class UiApp:
    def __init__(self, quiz:QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label(text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 13, "italic"))
        self.score.place(x=125, y=0)

        self.canvas = Canvas(width=300, height=250, bg="White")
        self.question_text = self.canvas.create_text(150, 125, text="Text goes here,", fill= THEME_COLOR, font=("Arial", 20, "italic"), width=280)
        self.canvas.grid(row=0, column=1, columnspan=2, pady=50)

        self.true = PhotoImage(file="true.png")
        self.true_button = Button(bg=THEME_COLOR ,image=self.true, highlightthickness=0, command=self.right_answer)
        self.true_button.grid(row=3, column=2)

        self.false = PhotoImage(file="false.png")
        self.false_button = Button(bg=THEME_COLOR, image=self.false, highlightthickness=0, command=self.wrong_answer)
        self.false_button.grid(row=3, column=1)

        self.get_quiz_text()

        self.window.mainloop()

    def get_quiz_text(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            quiz_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=quiz_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the Quiz.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def right_answer(self):
        self.give_feed_back(self.quiz.check_answer("true"))

    def wrong_answer(self):
        self.give_feed_back(self.quiz.check_answer("false"))

    def give_feed_back(self, is_right: bool):
        if is_right:
           self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_quiz_text)



