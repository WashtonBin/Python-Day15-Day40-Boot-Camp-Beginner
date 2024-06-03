from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain ):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text=f"Score: 0",
                                 bg=THEME_COLOR,
                                 fg="white", font=("Arial", 12, "bold"))
        self.score_label.grid(column=1, row=0, pady=10)


        self.canvas = Canvas(width=300, height=250, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                text="Some questions text",
                                width=280,
                                font=("Arial", 20, "italic"),
                                fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        true_png = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_png, highlightthickness=0, command=self.true_pressed)
        self.true_button.grid(column=0, row=2)

        false_png = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_png, highlightthickness=0, command=self.false_pressed)
        self.false_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    def false_pressed(self):
        is_right = self.quiz.check_answer("false")
        self.give_feedback(is_right)


    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)



    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, func=self.get_next_question)


