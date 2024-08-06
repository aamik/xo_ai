class TicTacToeAI:
    def __init__(self, player):
        self.player = player
        self.opponent = 'X' if player == 'O' else 'O'

    def get_move(self, board):
        best_score = float('-inf')
        best_move = None

        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = self.player
                    score = self.minimax(board, 0, False)
                    board[row][col] = ' '
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(board, self.player):
            return 1
        elif self.check_winner(board, self.opponent):
            return -1
        elif self.check_draw(board):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = self.player
                        score = self.minimax(board, depth + 1, False)
                        board[row][col] = ' '
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if board[row][col] == ' ':
                        board[row][col] = self.opponent
                        score = self.minimax(board, depth + 1, True)
                        board[row][col] = ' '
                        best_score = min(best_score, score)
            return best_score

    def check_winner(self, board, player):
        for row in board:
            if row[0] == row[1] == row[2] == player:
                return True
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == player:
                return True
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    def check_draw(self, board):
        for row in board:
            if ' ' in row:
                return False
        return True
