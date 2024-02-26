import tkinter as tk
from tkinter import messagebox

def on_click(row, col):
    global player
    
    # Check if the button is already clicked
    if buttons[row][col]['text'] != "" or winner is not None:
        return
    
    buttons[row][col]['text'] = player
    
    # Check for win or draw
    check_for_winner()
    
    # Switch player
    if winner is None:
        player = 'O' if player == 'X' else 'X'
        label.config(text=f"It's {player}'s turn")

def check_for_winner():
    global winner
    for i in range(3):
        # Check rows and columns
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != "":
            winner = buttons[i][0]['text']
            break
        elif buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != "":
            winner = buttons[0][i]['text']
            break
    # Check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        winner = buttons[0][0]['text']
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        winner = buttons[0][2]['text']
    
    if winner:
        messagebox.showinfo("Game Over", f"Player {winner} wins!")
    elif all(buttons[i][j]['text'] != "" for i in range(3) for j in range(3)):
        messagebox.showinfo("Game Over", "It's a draw!")

def reset_game():
    global player, winner
    player = 'X'
    winner = None
    label.config(text="It's X's turn")
    for row in buttons:
        for button in row:
            button.config(text="")

# Set up the main window
root = tk.Tk()
root.title("Tic Tac Toe")

player = 'X'  # The current player (X or O)
winner = None  # The winner (None if no winner yet)

# Create the UI components
buttons = [[None, None, None], [None, None, None], [None, None, None]]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=('normal', 40), width=5, height=2,
                                  command=lambda i=i, j=j: on_click(i, j))
        buttons[i][j].grid(row=i, column=j)

label = tk.Label(text="It's X's turn", font=('normal', 20))
label.grid(row=3, column=0, columnspan=3)

reset_button = tk.Button(root, text="Reset Game", command=reset_game)
reset_button.grid(row=4, column=0, columnspan=3)

# Start the GUI event loop
root.mainloop()
