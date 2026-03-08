from tkinter import *

windows = Tk()
windows.title("Miles to KM")
windows.config(padx=50, pady=50, bg="white")

miles_entry = Entry(width=7)
miles_entry.grid(row=0, column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0, column=2)

is_equalto_label = Label(text="is equal to")
is_equalto_label.grid(row=1, column=0)

km_result = Label(text="0")
km_result.grid(row=1, column=1)

km_label = Label(text="KM")
km_label.grid(row=1, column=2)

def convert():
    miles = float(miles_entry.get())
    km = miles * 1.60934
    km_result.config(text=f"{km:.2f}")

button = Button(text="Calculate", command=convert)
button.grid(row=2, column=1)

windows.mainloop()