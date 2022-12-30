from tkinter import *

windows = Tk()
windows.minsize(width=200, height= 100)
windows.title("Mile to Km Converter")
windows.config(padx=30,pady=10)



#Entry
input = Entry(width=10)
input.grid(row=0,column=1)
def calculate():
    mile= input.get()
    calc= int(mile)*1.6
    result.config(text= calc)

label1= Label(text="Miles")
label1.grid(row=0,column=2)
label2= Label(text="is equal to")
label2.grid(row=1,column=0)
label3= Label(text="Km")
label3.grid(row=1,column=2)
result = Label(text="0")
result.grid(row=1, column=1)
button = Button(text="Calculate",command=calculate)
button.grid(row=2,column=1)





windows.mainloop()