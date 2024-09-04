from tkinter import *
from tkinter import messagebox
root = Tk()

show = Label(root,text="Durban Online Parking",fg="red")
show.grid(row=0)

show1 = Label(root, text="Name",fg="blue")
show1.grid(row=1, column=0)

show2 = Label(root, text="Vehicle Registration Number",fg="blue")
show2.grid(row=2, column=0)

show3 = Label(root, text="Duration Value",fg="blue")
show3.grid(row=3, column=0)

name = Entry(root, border=6,fg="blue")
name.grid(row=1, column=1)

vehicle_number = Entry(root, border=6,fg="blue")
vehicle_number.grid(row=2, column=1)

duration_value = Entry(root,border=6,fg="blue")
duration_value.grid(row=3, column=1)

def validate_input():
    if not name.get():
        messagebox.showerror("Invalid Input", "Please enter your name.")
        return False
    
    if not vehicle_number.get():
        messagebox.showerror("Invalid Input", "Please enter your vehicle registration number.")
        return False

    try:
        int(duration_value.get())
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for duration you wish to park.")
        return False
    return True

def hour():
    if not validate_input():
        return
    
    duration_values = int(duration_value.get())
    parking_rate = 14

    if duration_values == 1:
        fee = parking_rate * 1
        messagebox.showinfo("Durban Online Parking", f"Hi {name.get()} with car registration number {vehicle_number.get()}, your parking cost is R{fee}")

    elif duration_values > 1 and duration_values <= 3:
        discount = 4
        fee = (duration_values * parking_rate)- discount
        messagebox.showinfo("Durban Online Parking", f"Hi {name.get()} with car registration number {vehicle_number.get()}, your parking cost is R{fee}")

    elif duration_values > 3 and duration_values <= 6:
        discount = 6
        fee = (duration_values *parking_rate) - discount
        messagebox.showinfo("Durban Online Parking", f"Hi {name.get()} with car registration number {vehicle_number.get()}, your parking cost is R{fee}")


    elif duration_values > 6:
        discount = 11
        fee = (duration_values * parking_rate) - discount
        messagebox.showinfo("Durban Online Parking", f"Hi {name.get()} with car registration number {vehicle_number.get()}, your parking cost is R{fee}")

    else:
        duration_values <= 0
        messagebox.showerror("Durban Online Parking","Invalid Input!!! Please Enter Valid Number Hour" )

def days():
    if not validate_input():
        return
    
    duration = int(duration_value.get())
    daily_hours = 24
    discount = 180
    parking_rate = 14
    fee = ((duration * daily_hours) * parking_rate)- discount
    if duration > 0:
        messagebox.showinfo("Durban Online Parking", f"Hi {name.get()} with car registration number {vehicle_number.get()}, your parking cost is R{fee}")

    else:
        duration <= 0
        messagebox.showerror("Durban Online Parking", "Invalid Input!!! Please Enter Valid Number Of Days")

def monthly():
    if not validate_input():
        return
    
    duration = int(duration_value.get())
    daily_price = 156
    days_in_Month = 31

    if duration <= 4 and duration > 0:
        discount = 1500
        fee = ((duration *daily_price) * days_in_Month) - discount
        messagebox.showinfo("Durban Online Parking", f"Hi {name.get()} with car registration number {vehicle_number.get()}, your parking cost is R{fee}")

    elif duration > 4 and duration < 12:
        discount = 2500
        fee = ((duration * daily_price ) * days_in_Month)-discount
        messagebox.showinfo("Durban Online Parking", "Durban Online Parking", f"Hi {name.get()} with car registration number {vehicle_number.get()}, your parking cost is R{fee}")

    elif duration >= 12:
        messagebox.showwarning("Durban Online Parking",f"Hi {name.get()}, Please Go to Year Deals")

    else:
        duration <= 0
        messagebox.showerror("Durban Online Parking", "Invalid Input!!! Please Enter Valid Number Of Days")

def years():
    if not validate_input():
        return
    
    duration = int(duration_value.get())

    if duration <= 4 and duration > 0: 
        discount = 5000
        monthly_price = 3336
        fee = (duration * (monthly_price * 12)) -discount
        messagebox.showinfo("Durban Online Parking", f"Hi {name.get()} with car registration number {vehicle_number.get()}, your parking cost is R{fee} ")

    elif duration > 4:
        discount = 8000
        month_price = 2336
        fee = (duration * (month_price * 12)) -discount
        messagebox.showinfo("Durban Online Parking", f"Hi {name.get()} with car registration number {vehicle_number.get()}, your parking cost is R{fee}")
        
    else:
        duration <= 0
        messagebox.showerror("Durban Online Parking", "Invalid Input!!! Please Enter Valid Number of Years")

def help():
    messagebox.showinfo("Durban Online Parking", "Fill in your name, Thabiso.\n"
                                "Fill in your vehicle registration number, ND 11262.\n"
                                "Fill in duration value you wish to park and must be a whole number like, 2.\n"
                                "Then choose one appropriate button to calculate your parking fees:\n"
                                "- Click 'Calculate Hours' for hourly rates.\n"
                                "- Click 'Calculate Days' for daily rates.\n"
                                "- Click 'Calculate Months' for monthly rates.\n"
                                "- Click 'Calculate Years' for yearly rates.")


mybutton = Button(root, text="Calculate Hours", command=hour,border=10,bg="cyan")
mybutton.grid(row=4, column=0)

daybutton = Button(root, text="Calculate Days",command=days,border=10,bg="yellow")
daybutton.grid(row=5,column=0)

monthbutton = Button(root, text="Calculate Months", command=monthly,border=10, bg="dark green",fg="white")
monthbutton.grid(row=4, column=1)

yearbutton = Button(root, text="Calculate Years", command=years,border=10,bg="dark orange",fg="white")
yearbutton.grid(row=5, column=1)

helpbutton =  Button(root, text="Help", command=help, fg="white", bg="grey", width= 10, border=11)
helpbutton.grid(row=10, column=0)

exitbutton = Button(root, text="Exit",command=root.quit, bg="red", border=6,fg="white",width=5)
exitbutton.grid(row=8, column=3)

root.mainloop()
