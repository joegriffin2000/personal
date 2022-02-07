# tkinter project. Where I figure out how to use the tkinter project so i dont get fucked by it in the future
# 
# 
# 

from tkinter import *

class Application(Frame):
    def __init__(self,master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.setButtons()
        self.setSize()
        
    def setSize(self):
        self.size = (400,400)
        
    def setButtons(self):
        self.quit = Button(self, text="Quit", command=self.quitButton)
        self.quit.pack()
        
    def quitButton(self):
        self.master.destroy()
        quit()
        

def mainViewer():
    myWindow = Tk()
    myWindow.title("Loading User Interface")
    
    myApp = Application(master=myWindow)
    myApp.mainloop()

if __name__ == "__main__":
    mainViewer()