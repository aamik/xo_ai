import unittest
from tictactoe import TicTacToe


class TestTicTacToe(unittest.TestCase):
    def test_initial_board(self):
        game = TicTacToe()
        self.assertEqual(
            game.board, [[' ' for _ in range(3)] for _ in range(3)])

    def test_make_move(self):
        game = TicTacToe()
        self.assertTrue(game.make_move(0, 0))
        self.assertEqual(game.board[0][0], 'X')

    def test_check_winner(self):
        game = TicTacToe()
        game.board = [['X', 'X', 'X'], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.assertTrue(game.check_winner())

    def test_check_draw(self):
        game = TicTacToe()
        game.board = [['X', 'O', 'X'], ['X', 'O', 'O'], ['O', 'X', 'X']]
        self.assertTrue(game.check_draw())


if __name__ == '__main__':
    unittest.main()
