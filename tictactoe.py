class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)]
                      for _ in range(3)]  # Initialize 3x3 board
        self.current_player = 'X'  # Set starting player

    def display_board(self):
        for row in self.board:
            print('|'.join(row))  # Print board row
            print('-' * 5)  # Print row separator

    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player  # Place player's move
            return True
        return False  # Invalid move

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':  # Check rows
                return True

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':  # Check columns
                return True

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':  # Check diagonal
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':  # Check anti-diagonal
            return True

        return False  # No winner

    def check_draw(self):
        for row in self.board:
            if ' ' in row:  # Check for empty spaces
                return False
        return True  # Draw if no empty spaces

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'  # Switch player
