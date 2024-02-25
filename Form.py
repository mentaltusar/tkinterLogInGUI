# importing Library of tkinter(Tk,Label,Button,Entry,Canvas,messagebox)
from tkinter import *
from tkinter import messagebox

COLOR = "#6E6C6C"  # Add your Colour here
FONT = "ariel"  # Add your Font here...


def click():  # Form Handling
    usernameGot = usernameinput.get()
    password = passwordinput.get()
    if not usernameGot and not password:
        canva.itemconfig(message, text="Please Fill the Required Inputs...", font=(FONT, 20, "bold"))
    else:
        messagebox.showinfo(title="Successfully Logged in !\n", message=f"Welcome {usernameGot} !")


window = Tk()
window.config(bg="black", padx=200, pady=200, width=600, height=600)
canva = Canvas(width=800, height=100, bg=COLOR, highlightthickness=0)
message = canva.create_text(400, 50, text="Welcome To Tkinter Gui Log In ", font=(FONT, 25, "bold"), fill="white")
canva.grid(column=0, row=0, columnspan=3)
username = Label(text="Username :", font=(FONT, 20, "bold"), width=12, fg="white", bg="black")
usernameinput = Entry(width=40)
username.grid(column=0, row=1)
usernameinput.grid(column=1, row=1, columnspan=2)
password = Label(text="Password :", font=(FONT, 20, "bold"), width=12, fg="white", bg="black")
password.grid(column=0, row=2)
passwordinput = Entry(width=40)
passwordinput.grid(column=1, row=2, columnspan=2)
submit = Button(bg="green", fg="white", text="Log In", font=(FONT, 12, 'italic'))
submit.config(pady=10, padx=20, command=click)
submit.grid(column=0, row=5, columnspan=3)
window.mainloop()
