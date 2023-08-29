import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import hashlib

root = tk.Tk()
root.title('Login!')
#root.attributes('-fullscreen', True)
root.geometry('700x200')
root.resizable(False, False)


def check_guess(u, p):
    file = open("login/info.txt", "r")
    file2 = open("login/salt.txt", "r")

    username = u
    password = p + file2.read()
    username = hashlib.md5(username.encode('utf-8')).hexdigest()
    password = password.lower() + username

    str2 = ""

    arr1 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]
    arr2 = ["z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", " "]

    for x in password:
        try:
            str2 += arr2[arr1.index(x)]
        except:
            str2 += ";"

    password = hashlib.md5(str2.encode('utf-8')).hexdigest()

    if file.read() == username + "," + password:
        return "Success"
    else:
        return "Denied"

    file.close()
    file2.close()


# frame
frame = ttk.Frame(root)

# field options
options = {'padx': 5, 'pady': 5}

guess_label = ttk.Label(frame, text='Enter your Username')
guess_label.grid(column=0, row=0, sticky='W', **options)

# guess entry
guess = tk.StringVar()
guess_entry = ttk.Entry(frame, textvariable=guess)
guess_entry.grid(column=1, row=0, **options)
guess_entry.focus()

guess_label2 = ttk.Label(frame, text='Enter your Password')
guess_label2.grid(column=0, row=1, sticky='E', **options)

# guess entry
guess2 = tk.StringVar()
guess_entry2 = ttk.Entry(frame, textvariable=guess2)
guess_entry2.grid(column=1, row=1, **options)
guess_entry2.focus()


# convert button


def convert_button_clicked():
    """  Handle convert button click event
    """
    try:
        u = guess.get()
        p = guess2.get()
        c = check_guess(u, p)
        result = c
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


guess1_button = ttk.Button(frame, text='Login!')
guess1_button.grid(column=2, row=0, sticky='W', **options)
guess1_button.configure(command=convert_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=2, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

root.mainloop()