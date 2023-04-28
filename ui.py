from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.label = Label(text=f"Score: {self.quiz.score}", fg="White", bg=THEME_COLOR)
        self.label.grid(column=1, row=0)
        
        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.word = self.canvas.create_text(150, 125, text="Sample", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.true_image = PhotoImage(file="Day 34 GUI Quiz App/quizzler-app/images/true.png")
        self.true_button = Button(image=self.true_image, highlightthickness=0, command=self.true)
        self.true_button.grid(column=0, row=2)
        
        self.false_image = PhotoImage(file="Day 34 GUI Quiz App/quizzler-app/images/false.png")
        self.false_button = Button(image=self.false_image, highlightthickness=0, command=self.false)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.word, text=q_text)
        else:
            self.canvas.itemconfig(self.word, text="You've reached the end of the quiz!")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
            
    def true(self):
        #user_answer = "True"
        #is_right = self.quiz.check_answer(user_answer)
        #self.quiz.check_answer("true")
        self.give_feedback(self.quiz.check_answer("true"))
        
    def false(self):
        #user_answer = "False"
        #is_right = self.quiz.check_answer(user_answer)
        #self.quiz.check_answer("false")
        self.give_feedback(self.quiz.check_answer("false"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
            
        self.window.after(1000, func=self.get_next_question)
