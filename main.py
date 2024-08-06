from tictactoe import TicTacToe
from ai import TicTacToeAI


def main():
    game = TicTacToe()
    ai = TicTacToeAI('O')

    while True:
        game.display_board()
        if game.current_player == 'X':
            row, col = map(int, input(
                "Enter row and column (0, 1, or 2): ").split())
        else:
            row, col = ai.get_move(game.board)

        if game.make_move(row, col):
            if game.check_winner():
                game.display_board()
                print(f"Player {game.current_player} wins!")
                break
            elif game.check_draw():
                game.display_board()
                print("It's a draw!")
                break
            game.switch_player()
        else:
            print("Invalid move. Try again.")


if __name__ == "__main__":
    main()
