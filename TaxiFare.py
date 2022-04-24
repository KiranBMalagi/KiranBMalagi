from tkinter import *
import datetime
from tkinter.font import *
from tkinter import messagebox

root = Tk()

root.geometry("800x1080")
root.config(bg="light blue")

label = root.title("Taxi Fare Calculator")

font1 = Font(family='Verdana', size=15, weight='bold')
font2 = Font(family='Verdana', size=12, weight='bold')
font3 = Font(family='Verdana', size=10, weight='bold')
font4 = Font(family='Verdana', size=8, weight='bold')
font5 = Font(family='Verdana', size=5, weight='bold')


photo = PhotoImage(file="C:\\Users\\Kiran B Malagi\\Pictures\\Photos\\image3.png")
Label(root, image=photo).grid(row=0, column=1)

headlabel = Label(root, text='Welcome to Taxi fare Calculator', fg='black', bg="pink", font=font1)
headlabel.grid(row=1, column=1)
starting = Label(root, text='Enter Starting point', fg='black', bg="white", font=font2)
starting.grid(row=2, column=0,pady=10)
startentry = Entry(root, width=40, borderwidth=8)
startentry.grid(row=2, column=1)
startentry.insert(0, "")

destination = Label(root, text='Enter destination', fg='black', bg="white", font=font2)
destination.grid(row=3, column=0,pady=10)
dest = Entry(root, width=40, borderwidth=8)
dest.grid(row=3, column=1)
dest.insert(0, "")

options = ["Auto", "Mini", "SUV", "Luxury"]
clicked = StringVar()
clicked.set("Select type of Vehicle")
drop = OptionMenu(root, clicked, *options)
drop.config(font=font4)
drop.grid(row=4, column=1, pady=10)

distances = Label(root, text='Enter the distance in KM', fg='black', bg="white", font=font2)
distances.grid(row=5, column=0,pady=10)
dista = Entry(root, width=40, borderwidth=8)
dista.grid(row=5, column=1)
dista.insert(0, "")

time = Label(root, text='Date & Time ', fg='black', bg="white", font=font3)
time.grid(row=6, column=0, pady=10)
current_time = datetime.datetime.now()
dt = Label(root, text=current_time)
dt.grid(row=6, column=1,pady=10)

cost = StringVar()
surges = StringVar()

def buton_clear():
    startentry.delete(0, END)
    dest.delete(0, END)
    dista.delete(0, END)

def buton_clear1():
    startentry.delete(0, END)
    dest.delete(0, END)
    dista.delete(0, END)
    total.delete(0, END)
    surgeamt.delete(0, END)

def buton_exit():
    exit(0)

def submit():
    if len(startentry.get()) == 0:
        response = messagebox.showerror("Error", "Please enter the starting point")
        Label(root, text=response).pack()
    elif ((startentry.get()).isalpha()) == False:
        response = messagebox.showerror("Error", "Please enter valid starting point")
        Label(root, text=response).pack()
    elif len(dest.get()) == 0:
        response = messagebox.showerror("Error", "Please enter the drop point")
        Label(root, text=response).pack()
    elif ((dest.get()).isalpha()) == False:
        response = messagebox.showerror("Error", "Please enter valid drop point")
        Label(root, text=response).pack()
    elif clicked.get() == "Select type of Vehicle":
        response = messagebox.showerror("Error", "Please select the type of vehicle")
        Label(root, text=response).pack()
    elif len(dista.get()) == 0:
        response = messagebox.showerror("Error", "Please enter the distance")
        Label(root, text=response).pack()
    elif (dista.get()).isalpha() == True:
        response = messagebox.showerror("Error", "Please enter the numeric value for distance")
        Label(root, text=response).pack()
    else:
        vehicle = clicked.get()
        dist = dista.get()
        distf = float(dist)

        base = 0
        total = 0
        perkm = 0
        surge = 0
        distance = distf
        current_time = datetime.datetime.now()
        cur = current_time.hour
        if (vehicle == 'Auto'):
            base = 30
            perkm = (distance - 2) * 15
        if (vehicle == 'Mini'):
            base = 30
            perkm = (distance - 2) * 18.54
        if (vehicle == 'Luxury'):
            base = 40
            perkm = (distance - 2) * 21.63
        if (vehicle == 'SUV'):
            base = 50
            perkm = (distance - 2) * 29.87
        total = base + perkm
        if (cur >= 22 or cur <= 6):
            surge = (total) / 2.0
        total = total + surge
        surges.set(surge)
        cost.set(total)


myButton = Button(root, text="SUBMIT", bg='blue', fg='black', command=submit, font=font3)
myButton.grid(row=7, column=1, pady=10)

button1 = Button(root, text="CLEAR ALL", bg="red", fg="black", command=buton_clear, font=font3)
button1.grid(row=8, column=1, pady=10)

total_amt = Label(root, text='TOTAL', fg='black', bg="white", font=font3)
total_amt.grid(row=9, column=0, pady=20)
total = Entry(root, text=cost, width=40, borderwidth=8)
total.grid(row=9, column=1)

surge_amt = Label(root, text='Surge Amount', fg='black', bg="white", font=font3)
surge_amt.grid(row=10, column=0, pady=20)
surgeamt = Entry(root, text=surges, width=40, borderwidth=8)
surgeamt.grid(row=10, column=1)

button2 = Button(root, text="CLEAR ALL", bg="red", fg="black", command=buton_clear1, font=font3)
button2.grid(row=10, column=2,pady=10)

button3 = Button(root, text="EXIT", bg="red", fg="black", command=buton_exit, font=font3)
button3.grid(row=10, column=3,pady=10)

root.mainloop()
