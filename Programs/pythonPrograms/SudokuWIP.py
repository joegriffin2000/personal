#
# SUDOKU WIP - A test script to try and make a sudoku board using tkinter to display it, My first attempt at trying to get tkinter to work
#
# Last Edited on February 5th, 2021 at 12:38 PM
# By Joe Griffin
#

import tkinter as tk
import os

class Application(tk.Frame):
    def __init__(self,SudokuPos,master=None):
        super().__init__(master)
        self.master = master
        self.contents = SudokuPos
        self.construct()
        self.grid()
        
    def construct(self):
        self.QuitButton()
        counter=0
        for i in self.contents:
            counter+=1
            counterString = str(counter)
            vars(self)[counterString]=self.Room(self.contents[i],i)
        
    def Room(self,PosDict,RoomPos):
        txtString = ""
        for i in PosDict:
            if i[1] == 3:
                txtString += PosDict[i] + "\n"
            else:
                txtString += PosDict[i]
        print("RoomPos:",RoomPos)    
        print(txtString)
        
        return tk.Message(self,text=txtString).grid(row=RoomPos[0],column=RoomPos[1])

        
    def QuitButton(self):
        self.quitbutton = tk.Button(self,text="Quit",command=quit,activeforeground="red",bg="grey")
        self.quitbutton.grid()

def insertNumbers(SudokuTable):
    for Room in SudokuTable:
        CurrentRoom=SudokuTable[Room]
        for i in range(1,4):
            for j in range(1,4):
                CurrentRoom[(i,j)]= "NA"
    return SudokuTable

def SudokuHub():
    SudokuTable = dict()
    for i in range(1,4):
        for j in range(1,4):
            SudokuTable[(i,j)] = dict()

    SudokuTable = insertNumbers(SudokuTable)
    return SudokuTable

if __name__ == "__main__":
    Sudoku = SudokuHub()
    root = tk.Tk()
    app = Application(Sudoku,master=root)
    app.master.title("My Do-Nothing Application")
    app.master.maxsize(720,600)
    app.master.minsize(720,600)
    app.mainloop()