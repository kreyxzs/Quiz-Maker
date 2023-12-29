from tkinter import *

def main():
    root.destroy()
    import main

root = Tk()
root.geometry("800x500")
root.maxsize(height=500, width=800)
root.title("Quiz Maker")
root.configure(bg='#f2f4f3')

mainFrame = Frame(root, bg='#f2f4f3')
mainFrame.pack(side=TOP)
mainFrame.pack_propagate(False)
mainFrame.configure(width=800, height=500)

topFrame = Frame(master=mainFrame, bg='#6b9f82')
topFrame.pack(side=TOP)
topFrame.pack_propagate(False)
topFrame.configure(width=800, height=50)

downFrame = Frame(master=mainFrame, bg='#bbc3bf')
downFrame.pack(side=BOTTOM)
downFrame.pack_propagate(False)
downFrame.configure(width=800, height=50)
        
back = Button(master=mainFrame, text="Back", font=('Georgia', 12), bg='#1877f2', command=main)
back.place(x=9, y=9)



root.mainloop()