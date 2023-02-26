import math
import tkinter as tk


def fator_escala(lat):
    k0 = 0.9996
    e = 0.081819190842621
    return (k0 * math.cos(lat)) / math.sqrt(1 - e*2 * math.sin(lat)*2)

def calculate():
    # Get the value entered by the user
    value = float(entry.get())
    
    # Multiply the value by 2
    result = fator_escala(value)
    
    # Update the label with the result
    label.config(text=f"Result: {result}")

# Create the GUI window
window = tk.Tk()
window.title("Scale Factor")

window.geometry("400x200")

# make the window non-resizable
window.resizable(False, False)

# Create the label and entry widgets
tk.Label(window, text="Enter a value:").pack()
entry = tk.Entry(window)
entry.pack()

# Create the button widget
button = tk.Button(window, text="Calculate", command=calculate)
button.pack()

# Create the label widget for the result
label = tk.Label(window, text="")
label.pack()

# Start the GUI event loop
window.mainloop()