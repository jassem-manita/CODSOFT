from src.game import TicTacToe
from src.ai import get_ai_move

def main():
    game = TicTacToe()
    human_player = 1
    ai_player = -1
    current_player = human_player

    while True:
        game.print_board()
        if game.current_winner:
            print(f"Player {'X' if game.current_winner == 1 else 'O'} wins!")
            break
        elif not game.empty_squares():
            print("It's a tie!")
            break

        if current_player == human_player:
            while True:
                row = int(input("Enter the row (0, 1, or 2): "))
                col = int(input("Enter the column (0, 1, or 2): "))
                if game.make_move((row, col), human_player):
                    break
                else:
                    print("Invalid move. Try again.")
        else:
            ai_move = get_ai_move(game)
            game.make_move(ai_move, ai_player)
            print(f"AI moves to ({ai_move[0]}, {ai_move[1]})")

        current_player *= -1  # Switch turns

if __name__ == "__main__":
    main()
