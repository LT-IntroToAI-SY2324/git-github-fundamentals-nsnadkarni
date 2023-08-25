import random
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror

root = tk.Tk()
root.title('Guess the number game! (1-100)')
#root.attributes('-fullscreen', True)
root.geometry('700x200')
root.resizable(False, False)

number = random.randint(1, 100)
print(number)
guessAmount = 0


def check_guess(n):
    global guessAmount
    n = int(n)
    guessAmount += 1

    if n == number:
        return "Correct! You guessed it in " + str(guessAmount) + " guess(es). " + "You win " + str(int(100/guessAmount)) + " points "
    elif n > number:
        return str(n) + " Is too high!, " + "you have guessed " + str(guessAmount) + " amount of times"
    elif n < number:
        return str(n) + " Is too low!, " + "you have guessed " + str(guessAmount) + " amount of times"


# frame
frame = ttk.Frame(root)

# field options
options = {'padx': 5, 'pady': 5}

guess_label = ttk.Label(frame, text='Enter a guess')
guess_label.grid(column=0, row=0, sticky='W', **options)

# guess entry
guess = tk.StringVar()
guess_entry = ttk.Entry(frame, textvariable=guess)
guess_entry.grid(column=1, row=0, **options)
guess_entry.focus()


# convert button


def convert_button_clicked():
    """  Handle convert button click event
    """
    try:
        n = float(guess.get())
        c = check_guess(n)
        result = c
        result_label.config(text=result)
    except ValueError as error:
        showerror(title='Error', message=error)


guess1_button = ttk.Button(frame, text='Guess!')
guess1_button.grid(column=2, row=0, sticky='W', **options)
guess1_button.configure(command=convert_button_clicked)

# result label
result_label = ttk.Label(frame)
result_label.grid(row=1, columnspan=3, **options)

# add padding to the frame and show it
frame.grid(padx=10, pady=10)

root.mainloop()