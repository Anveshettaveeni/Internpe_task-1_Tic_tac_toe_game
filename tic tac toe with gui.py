import tkinter as tk
from tkinter import messagebox

# Create the game board
board = [' ' for _ in range(9)]

# Function to display the board
def display_board():
    for i in range(9):
        buttons[i]['text'] = board[i]

# Function to check for a winning combination
def check_win(player):
    win_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]               # Diagonals
    ]
    for combination in win_combinations:
        if all(board[i] == player for i in combination):
            return True
    return False

# Function to handle button click
def button_click(position):
    global current_player
    if board[position] == ' ':
        board[position] = current_player
        buttons[position]['text'] = current_player

        if check_win(current_player):
            messagebox.showinfo('Game Over', 'Player ' + current_player + ' wins!')
            reset_game()
        elif ' ' not in board:
            messagebox.showinfo('Game Over', "It's a tie!")
            reset_game()
        else:
            current_player = 'O' if current_player == 'X' else 'X'
    else:
        messagebox.showwarning('Invalid Move', 'That position is already taken. Try again.')

# Function to reset the game
def reset_game():
    global board, current_player
    board = [' ' for _ in range(9)]
    current_player = 'X'
    display_board()

# Create the GUI
root = tk.Tk()
root.title('Tic-Tac-Toe')

buttons = []
for i in range(9):
    button = tk.Button(root, text=' ', font=('Arial', 20), width=6, height=3,
                       command=lambda pos=i: button_click(pos))
    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

reset_button = tk.Button(root, text='Reset', font=('Arial', 14), width=10, height=2, command=reset_game)
reset_button.grid(row=3, column=0, columnspan=3)

# Start the game
current_player = 'X'
display_board()

# Run the GUI event loop
root.mainloop()
