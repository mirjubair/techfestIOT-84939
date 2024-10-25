import tkinter as tk
import random
from tkinter import messagebox

# Initialize the game state
def init_game():
    global first, second, moves, pairs
    first = second = None
    moves = 0
    pairs = []
    random.shuffle(cards)
    for button in buttons:
        button.config(text='', state=tk.NORMAL)
    label.config(text="Moves: 0")

# Handle card flip
def flip_card(idx):
    global first, second, moves
    buttons[idx].config(text=cards[idx])
    buttons[idx].config(state=tk.DISABLED)
    if first is None:
        first = idx
    elif second is None:
        second = idx
        moves += 1
        label.config(text=f"Moves: {moves}")
        root.after(500, check_match)

# Check if two flipped cards match
def check_match():
    global first, second
    if cards[first] == cards[second]:
        pairs.append((first, second))
        if len(pairs) == len(cards) // 2:
            messagebox.showinfo("Memory Game", f"You win in {moves} moves!")
            init_game()
    else:
        buttons[first].config(text='', state=tk.NORMAL)
        buttons[second].config(text='', state=tk.NORMAL)
    first = second = None

# Set up GUI
root = tk.Tk()
root.title("Memory Matching Game")

cards = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F']
random.shuffle(cards)

buttons = []
for i in range(len(cards)):
    button = tk.Button(root, text='', font='Arial 20 bold', width=4, height=2,
                       command=lambda i=i: flip_card(i))
    button.grid(row=i // 4, column=i % 4)
    buttons.append(button)

label = tk.Label(root, text="Moves: 0")
label.grid(row=4, columnspan=4)

init_game()
root.mainloop()
