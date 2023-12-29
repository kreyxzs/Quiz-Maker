from tkinter import *

def quiz():
    root.destroy()
    import quiz

root = Tk()
root.geometry("800x500")
root.maxsize(height=500, width=800)
root.title("Quiz Maker")

mainFrame = Frame(root, bg='#6b9f82')
mainFrame.pack(side=TOP)
mainFrame.pack_propagate(False)
mainFrame.configure(width=800, height=500)

welcomeLabel = Label(master=mainFrame, text="Welcome!", font=('Georgia', 38), bg='#6b9f82')
welcomeLabel.pack(pady=100)

nameLabel = Label(master=mainFrame, text="Enter Code:", font=('Georgia', 14), bg='#6b9f82')
nameLabel.place(x=290, y=250)

code = Entry(master=mainFrame, width=8, font=('Georgia', 14))
code.place(x=400, y=250)

enterQuiz = Button(master=mainFrame, text="Enter", font=('Georgia', 13), bg='#1877f2', bd=3)
enterQuiz.place(x=320, y=310)

createQuiz = Button(master=mainFrame, text="Create a Quiz!", font=('Georgia', 16), bg='#1877f2', bd=5, command=quiz)
createQuiz.place(x=320, y=380)



root.mainloop()