from tkinter import *
window = Tk()
window.title("Celsius to Farenheit Converter")
window.geometry("800x400")
window.config(background="dark orange")
label1 = Label(window,text="Celsius to Farenheit Converter",bg="dark orange",font=("times",14)).place(x=275,y=30)
label2 = Label(window,text="Celsius -> Farenheit",bg="light grey",font=("times",25),fg="grey").place(x=255,y=70)
label3 = Label(window,text="Enter temperature in celsius:",bg="light grey",font=("times",16)).place(x=150,y=150)
enter = Entry(window,width=20).place(x=400,y=155)
label4 = Label(window,text="Temperature in Farenheit:",bg="light grey",font=("times",18)).place(x=180,y=225)
button = Button(window,text="Convert",height=1,width=25,bg="green",font=("times",14,)).place(x=255,y=300)

window.mainloop()