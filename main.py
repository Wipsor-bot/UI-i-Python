import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

def on_button_click():
    messagebox.showinfo("Besked", "Hej")

def close_window():
    root.destroy()

# Opret vinduet
root = tk.Tk()
root.geometry('500x500-5+40')
root.title("UI")



# Opret en knap
button_1 = tk.Button(root, text="Navn", command=on_button_click)
button_2 = tk.Button(root, text="Sted",)
button_3 = tk.Button(root, text="Login",)
button_4 = tk.Button(root, text="Kontakt",)
button_5 = tk.Button(root, text="Bonus",)
button_6 = tk.Button(root, text="Bonus 2",)
btn_close = tk.Button(root, text="Luk vindet", command=close_window)
#button_1 = tk.Button(root, text="Navn", command=on_button_click)
#btn_close = tk.Button(root, text="Luk vindet", command=close_window)


button_1.grid(row=0, column=0, padx=10, pady=5)  # Placeres i 1. række, 1. kolonne
button_2.grid(row=1, column=0, padx=10, pady=5)
button_3.grid(row=2, column=0, padx=10, pady=5)
button_4.grid(row=3, column=0, padx=10, pady=5)
button_5.grid(row=4, column=0, padx=10, pady=5)
button_6.grid(row=5, column=0, padx=10, pady=5)


#btn_close.pack(row=5, column=1 , padx=15, pady=20) 
#btn_close.grid(row=5, column=1, padx=10, pady=5)  
btn_close.place  (x=350, y=200)


# Start Tkinter event loop
root.mainloop()



# button.grid(row=0, column=0, padx=10, pady=5)  # Placeres i 1. række, 1. kolonne


