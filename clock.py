import tkinter
import time

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   widget.config(text=time_live) 
   widget.after(200, digital_clock)

window = tkinter.Tk()

window.title("Clock")
window.config(bg = "green")
window.geometry("50x25")
window.resizable(1,1)

widget = tkinter.Label(
    window,
    font= ("Helvetica", 12, "bold"),
    background = "green",
    foreground= "white"
    )
widget.pack(padx=0, pady=0)
digital_clock()
window.mainloop()