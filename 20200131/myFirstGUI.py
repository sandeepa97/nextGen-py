from tkinter import *

window = Tk()

# Init setup
window.configure(background = "red")
window.minsize(width = 250, height = 250)

def click_Yes():
    print("Yes!")


# Components
Label(window, text = "Full Name", bg = "black", fg = "white").grid(row = 0, column = 0, sticky = E)
Label(window, text = "Address", bg = "black", fg = "white").grid(row = 1, column = 0, sticky = E)
Label(window, text = "DOB", bg = "black", fg = "white").grid(row = 2, column = 0, sticky = E)
Label(window, text = "Is Sri Lankan?", bg = "black", fg = "white").grid(row = 3, column = 0, sticky = E)

txtFullName = Entry(window, width = 20, bg = "black", fg = "white")
txtAddress = Entry(window, width = 20, bg = "black", fg = "white")
txtDOB = Entry(window, width = 20, bg = "black", fg = "white")

txtFullName.grid(row = 0, column = 1, sticky = E)
txtAddress.grid(row = 1, column = 1, sticky = E)
txtDOB.grid(row = 2, column = 1, sticky = E)

def readEntry():
    print(txtFullName.get())

Checkbutton(window, text="Sri Lankan").grid(row = 3, column = 1, sticky = W)

Button(window, text = "Submit", width = 12, bd = 4, command = readEntry).grid(row = 4, column = 1)

window.mainloop()