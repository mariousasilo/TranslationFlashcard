import pandas
import random
import tkinter as tk
from tkinter import messagebox

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE = 'german'
FILE_PATH = f'data/{LANGUAGE}_words.csv'
df = pandas.read_csv(FILE_PATH)
language_list = df[LANGUAGE].to_list()
language_dict = {row[LANGUAGE]: row['english'] for (index, row) in df.iterrows()}
to_delete = ""


# Functions
def front_flip():
    global to_delete, language_list
    btn_check.config(command=no_res)
    btn_wrong.config(command=no_res)
    canvas.itemconfig(text_word_remaining, text=f"{len(language_list)} remaining", fill='black')
    try:
        language_word = random.choice(language_list)
    except IndexError:
        res = tk.messagebox.askyesno(title='Info', message='No more words left.\nDo you want to reshuffle')
        if res:
            language_list = df[LANGUAGE].to_list()
            to_delete = ""
            front_flip()
        else:
            root.destroy()
    else:
        to_delete = language_word
        canvas.itemconfig(text_language, text=LANGUAGE.title(), fill='black')
        canvas.itemconfig(text_word, text=language_word, fill='black')
        canvas.itemconfig(image_card, image=image_1)
        root.after(ms=3000, func=lambda: back_flip(language_word))


def back_flip(language_word):
    btn_check.config(command=check_next)
    btn_wrong.config(command=wrong_next)
    canvas.itemconfig(text_word_remaining, fill='white')
    english_word = language_dict[language_word]
    canvas.itemconfig(image_card, image=image_2)
    canvas.itemconfig(text_language, text='English', fill='white')
    canvas.itemconfig(text_word, text=english_word, fill='white')


def check_next():
    language_list.remove(to_delete)
    front_flip()


def wrong_next():
    front_flip()


def no_res():
    pass


# Create GUI
root = tk.Tk()
root.title(f'{LANGUAGE.title()} Flashcard')
root.minsize(width=10, height=10)
root.config(pady=50, padx=50, background=BACKGROUND_COLOR)

image_1 = tk.PhotoImage(file='images/card_front.png')
image_2 = tk.PhotoImage(file='images/card_back.png')
right_btn_img = tk.PhotoImage(file='images/right.png')
wrong_btn_img = tk.PhotoImage(file='images/wrong.png')

canvas = tk.Canvas(width=800, height=530, background=BACKGROUND_COLOR, highlightthickness=0)
image_card = canvas.create_image(400, 265, image=image_1)
text_language = canvas.create_text(400, 165, text=LANGUAGE.title(), font=('Arial', 26, 'italic'))
text_word = canvas.create_text(400, 265, text='', font=('Arial', 32, 'bold'))
text_word_remaining = canvas.create_text(400, 40, text=f"", font=('Arial', 12, 'normal'))
canvas.grid(row=0, column=0, columnspan=3)

btn_check = tk.Button(image=right_btn_img, highlightthickness=0, command=check_next)
btn_check.grid(row=1, column=2)
btn_wrong = tk.Button(image=wrong_btn_img, highlightthickness=0, command=wrong_next)
btn_wrong.grid(row=1, column=0)

front_flip()
root.mainloop()
