""" Python program to  create a simple GUI calculator using Tkinter

To create a tkinter based event driven application:
    Import the module – tkinter
    Create the main window (container)
    Add any number of widgets to the main window
    Apply the event rigger on the widgets.
"""

import tkinter as tk

expression = ""      # string holds all button presses until CLR or = pressed

def delete_last_digit_DEL(new_expression):
    old_expression = new_expression[:-1]
    return old_expression
    

def press(pressed):
    """Handle the callbacks from the button presses."""
    global expression
    if pressed == 'CLR':
        expression = ''
        output.set('')
    elif pressed == 'DEL':
        old_expression = delete_last_digit_DEL(expression)
        output.set(old_expression)
    elif pressed == '=':
        total = str(eval(expression)) #Don't use "eval" in real life 
        output.set(total)
        expression = total
    else:
        expression = expression + pressed
        output.set(expression)


# set up the TKinter window
gui = tk.Tk()
gui.configure(background="black")
gui.title("Simple Calculator")
gui.geometry("335x145")
output = tk.StringVar()            # variable that auto-updates in the GUI
expression_field = tk.Entry(gui, textvariable=output)
expression_field.grid(columnspan=4, ipadx=70)  # output field
output.set("enter your expression")

# buttons_grid is list of (text, row, column) to be assigned to Button widgets
# during the for loop
buttons_grid = (
    ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('+', 2, 3), ('DEL', 2, 4),
    ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3), ('(', 3, 4),
    ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('*', 4, 3), (')', 4, 4),
    ('0', 5, 0), ('CLR', 5, 1), ('=', 5, 2), ('/', 5, 3),
)

# create the Button widgets one by one, and set in the grid
for (symbol, row, col) in buttons_grid:
    new_button = tk.Button(gui, text=symbol, fg='black', bg='grey',
                           command=lambda argument=symbol: press(argument),
                           height=1, width=7)
    new_button.grid(row=row, column=col)

# Start the event loop
gui.mainloop()
