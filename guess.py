from tkinter import *
import random
import tkinter.messagebox as tmsg

# Initialize the Tkinter application
app = Tk()
count = 0
comp = 0

# Function to generate a random number between 1 and 100
def generate():
    global comp
    comp = random.randint(1, 101)

# Function to start the game and setup the UI
def basic():
    global count
    count = 0
    app.title("Number Guessing game")
    app.geometry("500x500")
    app.configure(bg='lavender')  # Set background color to lavender

    # Main game interface
    heading = Label(app, text='Number Guessing game', font="Helvetica 18 bold", bg='black', fg='white')
    heading.pack(pady=10)

    # Previous score label
    try:
        with open('score.txt', 'r') as f:
            hg = f.read()
    except FileNotFoundError:
        hg = '0'
    sc = Label(app, text=f'Previous score: {hg}', font='Helvetica 10 bold', bg='lavender')
    sc.pack(anchor=E, padx=25, pady=5)

    # User input
    global userv
    userv = StringVar()
    user = Entry(app, textvariable=userv, justify=CENTER, relief=FLAT, borderwidth=2, font='Helvetica 18 bold')
    user.pack(pady=10)

    # Submit button
    submit = Button(app, text='Submit', command=result, font='Helvetica 18 bold', relief=FLAT)
    submit.pack(pady=10)

    # Result display
    global show
    show = Label(app, text='', font='Helvetica 12 bold', bg='lavender')
    show.pack(pady=10)

    generate()

# Function to handle the result of user's guess
def result():
    global count
    number = userv.get()
    if number == '':
        tmsg.showerror('Error', "Please enter a value")
    else:
        n = int(number)
        count += 1
        if count == 10:
            tmsg.showinfo('Game over', 'You lose the Game!')
        elif comp == n:
            score = 11 - count
            tmsg.showinfo('Win', f'You guessed the right number!\nYour score {score}')
            show.config(text='Win!', fg='green')
            with open('score.txt', 'w') as f:
                f.write(str(score))
            generate()
            tmsg.showinfo('Next number', 'Click OK to guess another number')
        elif comp > n:
            show.config(text='Select a greater number', fg='red')
        else:
            show.config(text='Select a smaller number', fg='red')

# Function to restart the game
def restart():
    generate()
    tmsg.showinfo('Reset', "Game reset!")

# Function to show About information
def call1():
    str1 = 'This game is developed by Siddharth Dyamgond.\n\nCopyright @ 2023'
    tmsg.showinfo('About', str1)

# Main setup
basic()

# Buttons for menu options
menu_frame = Frame(app, bg='lavender')
menu_frame.pack(pady=20)

buttons = [
    ('Start', basic),
    ('Restart', restart),
    ('About', call1),
    ('Quit', quit)
]

for text, command in buttons:
    btn = Button(menu_frame, text=text, command=command, font='Helvetica 12 bold', relief=FLAT)
    btn.pack(side=LEFT, padx=10)

app.mainloop()
