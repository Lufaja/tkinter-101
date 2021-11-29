import tkinter
window = tkinter.Tk()

window.title("Hello")
window.config(bg = "green")
window.geometry("100x100")

widget = tkinter.Label(
    window,
    text = "Hello\n tkinter!\n",
    fg = "magenta",
    bg = "cyan",
    )
widget.pack(padx=25, pady=25)

window.mainloop()