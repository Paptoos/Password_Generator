# Imports
# Import random libery to creaet random numbers
import random
# Import string libery to creaet random strings
import string
# Import tkinrer Moudle to Creaet Grafical App
import tkinter as tk


# variable sets
# We push all of the lower case alphabet in a array
lowecase_letters = string.ascii_lowercase
# We push all of the lower case alphabet in a array
uppercase_letters = string.ascii_uppercase
# We push the valiud symbols in a array
symbols = ['!', '@', '#', '$', '%', '^', '&', '*']


# Create Grafical Window
# root is master windows
root = tk.Tk()
root.iconbitmap('logo.ico')
root.title('Paptoos Password Genaretor')
root.geometry('1000x500')
menubar = tk.Menu(root)
root.config(menu=menubar)


def show_entry_fields():
    pass_lenght = e1.get()
    pass_lenght = int(pass_lenght)
    result_creator('018', pass_lenght)
    tk.Label(root, text="Your code is : " + result,
             font=('tahoma', 40), wraplength=1200).pack()
    copy_to_clipboard(result)


def result_creator(result_create: str, lenght_of_result: int):
    for x in range(0, lenght_of_result):
        char_type = ["numbers", "symbols",
                     "uppercase_letters", "lowercase_letters"]
        char_type_result = random.choice(char_type)
        if char_type_result == "numbers":
            result_create += str(random.randint(1, 9))
        elif char_type_result == "symbols":
            result_create += random.choice(symbols)
        elif char_type_result == "uppercase_letters":
            result_create += random.choice(uppercase_letters)
        elif char_type_result == "lowercase_letters":
            result_create += random.choice(lowecase_letters)
    global result
    result = result_create


def copy_to_clipboard(content_for_copy):
    root.clipboard_clear()
    root.clipboard_append(content_for_copy)


def show():
    global e1
    e1 = tk.Entry(root)
    e1.insert(10, "10")

    e1.pack()
    tk.Button(root, text='Calculate', command=show_entry_fields).pack()


show()
root.mainloop()
