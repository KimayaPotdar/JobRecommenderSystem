from tkinter import Tk, Frame, Label, Button
from time import sleep
global questions, index, button, window

class Question:
    global questions,index, button, window
    def __init__(self, question, answers):
        self.question = question
        self.answers = answers
        # self.correctLetter = correctLetter

    def check(self, option, view):
        # global right
        # if(letter == self.correctLetter):
        #     label = Label(view, text="Right!")
        #     right += 1
        # else:
        #     label = Label(view, text="Wrong!")
        # label.pack()
        selected_answer=option
        print(selected_answer)
        view.after(1000, lambda *args: self.unpackView(view))


    def getView(self, window):
        view = Frame(window)
        Label(view, text=self.question, font='Times 13').pack(pady=20)
        Button(view, text=self.answers[0], command=lambda *args: self.check(1, view),height=2, width=30,font='Times 12').pack(side='top',pady=5)
        Button(view, text=self.answers[1], command=lambda *args: self.check(2, view), width=30,font='Times 12').pack(side='top',pady=5)
        Button(view, text=self.answers[2], command=lambda *args: self.check(3, view), width=30,font='Times 12').pack(side='top',pady=5)
        Button(view, text=self.answers[3], command=lambda *args: self.check(4, view), width=30,font='Times 12').pack(side='top',pady=5)
        Button(view, text=self.answers[4], command=lambda *args: self.check(5, view), width=30,font='Times 12').pack(side='top',pady=5)
        return view

    def unpackView(self, view):
        view.pack_forget()
        askQuestion()

def exit():
    window.destroy()

def askQuestion():
    global questions, window, index, button, number_of_questions
    if(len(questions) == index + 1):
        Label(window, text="Thank you for answering " + str(number_of_questions) + " questions.").pack()
        Button(window, text="Exit",command=exit).pack()
        return
    button.pack_forget()
    index += 1
    questions[index].getView(window).pack()

def start_quiz():
    global questions,index, button, window, number_of_questions
    questions = []
    file = open("questions.txt", "r")
    line = file.readline()
    while(line != ""):
        questionString = line
        answers = []
        for i in range (5):
            answers.append(file.readline())

        questions.append(Question(questionString, answers))
        line = file.readline()
    file.close()
    index = -1
    right = 0
    number_of_questions = len(questions)

    window = Tk()
    window.geometry('925x425')
    button = Button(window, text="Start", command=askQuestion)
    button.pack()
    window.mainloop()

if __name__ == '__main__':
    start_quiz()