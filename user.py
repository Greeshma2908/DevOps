from tkinter import *
from tkinter import ttk
window = Tk()
window.title("User Registration Form")
window.geometry('400x400')

l1 = Label(window ,text = "First Name").place(x=70,y=100)  
l2= Label(window ,text = "Last Name").place(x=58,y=150)  
l3= Label(window ,text = "Email Id").place(x=94,y=200)  
l4= Label(window ,text = "Contact Number").place(x=82,y=250)  
e1 = Entry(window).place(x=200,y=100)  
e2 = Entry(window).place(x=200,y=150)  
e3 = Entry(window).place(x=200,y=200)  
e4 = Entry(window).place(x=200,y=250)  
l5 = Label(window, text="Event",width=20,font=("bold", 10))  
l5.place(x=100,y=280)  
vars= IntVar()  
Radiobutton(window, text="Hackathon",padx = 5, variable=vars, value=1).place(x=130,y=280)  
Radiobutton(window, text="Relay Code",padx = 20, variable=vars, value=2).place(x=200,y=280)  
  
def clicked():
   print("You have registered successfully!")
   
btn = ttk.Button(window ,text="Submit",command=clicked).place(x=220,y=380)
window.mainloop()