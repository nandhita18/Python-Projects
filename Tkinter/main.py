from tkinter import *
def button_clicked():
    print("I am clicked")
    value = input.get()
    my_label.config(text=value)

window = Tk()
window.title("My first GUI program")
window.minsize(width=500, height= 300)

#lable
my_label = Label(text="My label", font=("Arial" , 20, "italic"))
my_label["text"] = "New Text"
my_label.config(text="New Text")
my_label.grid(row=0,column=0)
#can also add padding around widgets by using widget.config(padx=.. , pady=..)
#Entry
input = Entry(width=10)
input.grid(row=3,column=2)

#button
button = Button(text="Click Me", command=button_clicked)
button.grid(row=1,column=1)
button2 = Button(text="Am the Newest" , command=button_clicked)
button2.grid(row=0, column=2)


window.mainloop()
