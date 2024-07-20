from tkinter import *
window = Tk()
window.title("Celsius to Farenheit Converter")
window.geometry("800x400")
window.config(background="dark orange")

def convert():
    temperature = enter.get()
    if temperature.isdigit():
        farenheit = (float(temperature)*9/5)+32
        label4.config(text="Temperature in Farenheit: {}".format(farenheit),bg="light grey")

label1 = Label(window,text="Celsius to Farenheit Converter",bg="dark orange",font=("times",14))
label1.pack()
label2 = Label(window,text="Celsius -> Farenheit",bg="light grey",font=("times",25),fg="grey").place(x=260,y=75)
label3 = Label(window,text="Enter temperature in celsius:",bg="light grey",font=("times",16)).place(x=150,y=150)
enter = Entry(window,width=30)
enter.place(x=400,y=150,height=27)
label4 = Label(window,bg="dark orange",font=("times",16))
label4.place(x=200,y=200)
button = Button(window,text="Convert",height=1,width=25,bg="green",font=("times",14,),command=convert).place(x=265,y=300)




window.mainloop()
