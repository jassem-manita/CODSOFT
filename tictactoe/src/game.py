# src/game.py

import numpy as np

class TicTacToe:
    def __init__(self):
        self.board = np.zeros((3, 3), dtype=int)  # 3x3 board initialized with zeros
        self.current_winner = None

    def print_board(self):
        # Print the board
        for row in self.board:
            print(row)

    def available_moves(self):
        # Return a list of available moves (i.e., empty cells)
        return [(r, c) for r in range(3) for c in range(3) if self.board[r, c] == 0]

    def empty_squares(self):
        # Return boolean indicating whether there are empty squares on the board
        return np.any(self.board == 0)

    def make_move(self, square, player):
        # Place a move on the board for a player (1 for 'X' and -1 for 'O')
        if self.board[square] == 0:
            self.board[square] = player
            if self.winner(square, player):
                self.current_winner = player
            return True
        return False

    def winner(self, square, player):
        # Check if the player has won
        row_ind, col_ind = square
        row_win = all([self.board[row_ind, i] == player for i in range(3)])
        col_win = all([self.board[i, col_ind] == player for i in range(3)])
        diag1_win = all([self.board[i, i] == player for i in range(3)]) if row_ind == col_ind else False
        diag2_win = all([self.board[i, 2 - i] == player for i in range(3)]) if row_ind + col_ind == 2 else False
        return row_win or col_win or diag1_win or diag2_win

    def num_empty_squares(self):
        return len(self.available_moves())
