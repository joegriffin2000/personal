from tkinter import *

window=Tk()
button=Button(window, text="This Should Close The Frame", fg='blue',command=root.destroy)
button.place(x=80, y=100)

window.title('Admin Login')
window.geometry("300x200+10+20")
window.mainloop()



