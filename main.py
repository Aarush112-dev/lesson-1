from tkinter import *
import calendar
def show_calender():
    window2 = Tk()
    window2.title("window 2")
    window2.geometry("450x450")
    window2.config(background="white")
    fetch_year = int(enter.get())
    calender_content = calendar.calendar(fetch_year)
    calender_year = Label(window2,text=calender_content,bg="white",font=("times",10,"bold")).place(x=50,y=225)
    window2.mainloop()
if __name__ == "__main__":
    window = Tk()
    window.title("window 1")
    window.geometry("800x600")
    window.config(background="green")
    calender = Label(window,text="Hello, welcome to my Calender",bg="green",font=("times",20,"bold")).place(x=50,y=50)
    year = Label(window,text="Enter Year: ",bg="blue",font=("times",14,"bold"),fg="white").place(x=50,y=100)
    enter = Entry(window,width=20)
    enter.place(x=160,y=105)
    button = Button(window,text="Show calender",bg="blue",font=("times",14,"bold"),command=show_calender).place(x=70,y=150)

    window.mainloop()