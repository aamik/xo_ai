class TicTacToeAI:
    def __init__(self, player):
        self.player = player
        # Set the opponent player
        self.opponent = 'X' if player == 'O' else 'O'

    def get_move(self, board):
        # Initialize the best score to negative infinity
        best_score = float('-inf')
        # Initialize the best move to None
        best_move = None

        # Iterate over all cells in the board
        for row in range(3):
            for col in range(3):
                # Check if the cell is empty
                if board[row][col] == ' ':
                    # Make a move for the player
                    board[row][col] = self.player
                    # Evaluate the move using minimax algorithm
                    score = self.minimax(board, 0, False)
                    # Undo the move
                    board[row][col] = ' '
                    # Update the best score and best move if the current score is better
                    if score > best_score:
                        best_score = score
                        best_move = (row, col)

        return best_move

    def minimax(self, board, depth, is_maximizing):
        if self.check_winner(board, self.player):
            return 1
        elif self.check_winner(board, self.opponent):
            return -1
        # Check if the game is a draw
        elif self.check_draw(board):
            return 0

        if is_maximizing:
            best_score = float('-inf')
            # Iterate over all cells in the board
            for row in range(3):
                for col in range(3):
                    # Check if the cell is empty
                    if board[row][col] == ' ':
                        # Make a move for the player
                        board[row][col] = self.player
                        # Recursively call minimax for the opponent's move
                        score = self.minimax(board, depth + 1, False)
                        # Undo the move
                        board[row][col] = ' '
                        best_score = max(best_score, score)
            return best_score
        else:
            best_score = float('inf')
            # Iterate over all cells in the board
            for row in range(3):
                for col in range(3):
                    # Check if the cell is empty
                    if board[row][col] == ' ':
                        # Make a move for the opponent
                        board[row][col] = self.opponent
                        # Recursively call minimax for the player's move
                        score = self.minimax(board, depth + 1, True)
                        # Undo the move
                        board[row][col] = ' '
                        best_score = min(best_score, score)
            return best_score

    def check_winner(self, board, player):
        # Check rows for a win
        for row in board:
            if row[0] == row[1] == row[2] == player:
                return True
        # Check columns for a win
        for col in range(3):
            if board[0][col] == board[1][col] == board[2][col] == player:
                return True
        # Check diagonals for a win
        if board[0][0] == board[1][1] == board[2][2] == player:
            return True
        if board[0][2] == board[1][1] == board[2][0] == player:
            return True
        return False

    def check_draw(self, board):
        # Check if there are any empty cells left
        for row in board:
            if ' ' in row:
                return False
        return True
    

 
