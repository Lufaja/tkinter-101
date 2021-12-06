import tkinter
window = tkinter.Tk()

window.title("Clicker")
window.config(bg="grey")
window.geometry("350x200")
count = tkinter.IntVar()

#button to add to count
add = tkinter.Button(
    window,
    text="Up",
    width=25,
    height=1
)
add.pack()
add.place(anchor="center", x=175, y=50)

#button to lower count
subtract = tkinter.Button(
    window,
    text="Down",
    width=25,
    height=1
)
subtract.pack()
subtract.place(anchor="center",x=175, y = 150)

window.mainloop()