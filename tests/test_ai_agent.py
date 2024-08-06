import unittest
from tictactoe import TicTacToe
from ai_agent import TicTacToeAI


class TestTicTacToeAI(unittest.TestCase):
    def test_get_move(self):
        game = TicTacToe()
        ai = TicTacToeAI('O')
        move = ai.get_move(game.board)
        self.assertIn(move, [(r, c) for r in range(3) for c in range(3)])


if __name__ == '__main__':
    unittest.main()
