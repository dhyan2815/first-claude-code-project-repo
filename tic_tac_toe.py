#!/usr/bin/env python3
"""Simple command‑line Tic‑Tac‑Toe game.

Two players alternate entering a position number (1‑9) to place their mark
(X for Player 1, O for Player 2). The board is displayed after each move.
The game ends when a player wins or the board fills (draw).
"""

def print_board(board):
    # board is a list of 9 strings: ' ', 'X', or 'O'
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def check_winner(board, mark):
    win_patterns = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
        (0, 4, 8), (2, 4, 6)              # diagonals
    ]
    return any(all(board[i] == mark for i in combo) for combo in win_patterns)

def get_move(board, player):
    while True:
        try:
            move = input(f"Player {player} ({'X' if player == 1 else 'O'}), enter a move (1‑9): ")
            idx = int(move) - 1
            if idx < 0 or idx > 8:
                print("Invalid number – choose 1 through 9.")
                continue
            if board[idx] != ' ':
                print("Square already taken – choose another.")
                continue
            return idx
        except ValueError:
            print("Please enter a numeric value.")

def main():
    board = [' '] * 9
    current_player = 1  # 1 -> X, 2 -> O
    move_count = 0
    while True:
        print_board(board)
        idx = get_move(board, current_player)
        board[idx] = 'X' if current_player == 1 else 'O'
        move_count += 1
        if check_winner(board, board[idx]):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if move_count == 9:
            print_board(board)
            print("It's a draw!")
            break
        current_player = 2 if current_player == 1 else 1

if __name__ == "__main__":
    main()
