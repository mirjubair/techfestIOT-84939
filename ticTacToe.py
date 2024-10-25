import tkinter as tk
from tkinter import messagebox

# Initialize board
board = [' ' for _ in range(9)]

# Check if someone has won
def check_winner(b, mark):
    return ((b[0] == b[1] == b[2] == mark) or
            (b[3] == b[4] == b[5] == mark) or
            (b[6] == b[7] == b[8] == mark) or
            (b[0] == b[3] == b[6] == mark) or
            (b[1] == b[4] == b[7] == mark) or
            (b[2] == b[5] == b[8] == mark) or
            (b[0] == b[4] == b[8] == mark) or
            (b[2] == b[4] == b[6] == mark))

# Minimax algorithm for AI
def minimax(b, depth, is_maximizing):
    if check_winner(b, 'O'):
        return 10 - depth
    if check_winner(b, 'X'):
        return depth - 10
    if ' ' not in b:
        return 0

    if is_maximizing:
        best_score = -1000
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'O'
                score = minimax(b, depth + 1, False)
                b[i] = ' '
                best_score = max(score, best_score)
        return best_score
    else:
        best_score = 1000
        for i in range(9):
            if b[i] == ' ':
                b[i] = 'X'
                score = minimax(b, depth + 1, True)
                b[i] = ' '
                best_score = min(score, best_score)
        return best_score

# AI makes its move
def ai_move():
    best_score = -1000
    move = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > best_score:
                best_score = score
                move = i
    board[move] = 'O'
    buttons[move].config(text="O")
    if check_winner(board, 'O'):
        messagebox.showinfo("Tic Tac Toe", "Computer Wins!")
        reset_board()

# Player makes a move
def player_move(btn, idx):
    if board[idx] == ' ':
        board[idx] = 'X'
        btn.config(text="X")
        if check_winner(board, 'X'):
            messagebox.showinfo("Tic Tac Toe", "You Win!")
            reset_board()
        elif ' ' not in board:
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_board()
        else:
            ai_move()

# Reset the board for a new game
def reset_board():
    global board
    board = [' ' for _ in range(9)]
    for btn in buttons:
        btn.config(text=" ")

# GUI setup
root = tk.Tk()
root.title("Tic-Tac-Toe")

buttons = []
for i in range(9):
    btn = tk.Button(root, text=' ', font='Arial 20 bold', height=3, width=6,
                    command=lambda i=i: player_move(buttons[i], i))
    btn.grid(row=i // 3, column=i % 3)
    buttons.append(btn)

root.mainloop()
