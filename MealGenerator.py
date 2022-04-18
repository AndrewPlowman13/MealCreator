from MealSearch import search
from tkinter import *

# List to hold ingredient variables
ingredient_variables = ["Broccoli", "Onion", "Potato"]
# List to hold user choices
choices = []


def selected_ingredient(ingredient):
    if ingredient == 0:
        return "Broccoli"
    elif ingredient == 1:
        return "Onion"
    elif ingredient == 2:
        return "Potato"


def items_selected(event):
    selected_items = selection_list.curselection()
    for item in selected_items:
        choices.append(selected_ingredient(item))
    recipe_display.delete(1.0, END)
    for recipe in search(choices):
        recipe_display.insert(END, recipe + "\n")
    choices.clear()


# Create GUI with tkinker
root = Tk()
label_var = StringVar()
label = Label(root, textvariable=label_var, relief=RAISED)
label_var.set("Select the ingredients you want to use")
label.pack()

# Create listbox for ingredients
selection_list = Listbox(root, selectmode="multiple")
selection_list.pack(expand=YES, fill="both")
for i in range(len(ingredient_variables)):
    selection_list.insert(END, ingredient_variables[i])

selection_list.bind('<<ListboxSelect>>', items_selected)

recipe_display = Text(root, width=38, font=('Arial', 14))
recipe_display.pack()

root.mainloop()
