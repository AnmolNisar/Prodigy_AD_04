import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        
        # Initialize the game board
        self.board = [["" for _ in range(3)] for _ in range(3)]
        
        # Create buttons for the grid
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=("Arial", 36), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
        
        # Initialize the game state
        self.current_player = "X"
        self.game_over = False

        # Reset button
        reset_button = tk.Button(self.root, text="Reset", font=("Arial", 20), command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, sticky="nsew")

    def on_click(self, row, col):
        """Handle a button click, marking the board and checking for a winner."""
        if not self.game_over and self.board[row][col] == "":
            # Mark the board with the current player's symbol
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
            
            # Check if the current player has won
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.game_over = True
            elif self.is_draw():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.game_over = True
            else:
                # Switch the current player
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        """Check if the current player has won the game."""
        for row in range(3):
            if self.board[row][0] == self.board[row][1] == self.board[row][2] != "":
                return True
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def is_draw(self):
        """Check if the game is a draw (all cells are filled and no winner)."""
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == "":
                    return False
        return True

    def reset_game(self):
        """Reset the game to start a new match."""
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
        self.current_player = "X"
        self.game_over = False

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
