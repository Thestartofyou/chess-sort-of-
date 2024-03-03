class ChessBoard:
    def __init__(self):
        self.board = [
            ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
            ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
            ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        ]
        self.current_turn = 'W'
        self.castling_rights = {'W': {'king_side': True, 'queen_side': True},
                                 'B': {'king_side': True, 'queen_side': True}}
        self.en_passant_target = None

    def print_board(self):
        for row in self.board:
            print(' '.join(row))

    def is_valid_move(self, start_pos, end_pos):
        # Implement logic to check if the move is valid
        return True

    def make_move(self, start_pos, end_pos):
        if self.is_valid_move(start_pos, end_pos):
            # Implement logic to make the move
            piece = self.board[start_pos[0]][start_pos[1]]
            self.board[start_pos[0]][start_pos[1]] = ' '
            self.board[end_pos[0]][end_pos[1]] = piece
            return True
        else:
            return False

    def is_checkmate(self):
        # Placeholder for checkmate logic
        return False

    def is_stalemate(self):
        # Placeholder for stalemate logic
        return False

    def is_draw(self):
        # Placeholder for draw logic
        return False

    def switch_turn(self):
        self.current_turn = 'B' if self.current_turn == 'W' else 'W'

    def get_king_position(self, color):
        for i in range(8):
            for j in range(8):
                if self.board[i][j] == 'K' and color == 'W':
                    return i, j
                elif self.board[i][j] == 'k' and color == 'B':
                    return i, j
        return None

    def is_in_check(self, color):
        king_pos = self.get_king_position(color)
        if king_pos is None:
            return False

        # Check for attacks on the king
        for i in range(8):
            for j in range(8):
                if self.board[i][j].lower() == color.lower() and self.is_valid_move((i, j), king_pos):
                    return True
        return False

    def move_piece(self, start_pos, end_pos):
        if self.is_valid_move(start_pos, end_pos):
            piece = self.board[start_pos[0]][start_pos[1]]
            self.board[end_pos[0]][end_pos[1]] = piece
            self.board[start_pos[0]][start_pos[1]] = ' '
            return True
        return False

    def pawn_promotion(self, end_pos):
        # Check if a pawn has reached the opposite end of the board
        if end_pos[0] == 0 or end_pos[0] == 7:
            piece = input("Pawn promotion! Choose a piece (Q, R, B, N): ")
            while piece not in ['Q', 'R', 'B', 'N']:
                piece = input("Invalid choice! Choose a piece (Q, R, B, N): ")
            self.board[end_pos[0]][end_pos[1]] = piece

    def make_move(self, start_pos, end_pos):
        if self.is_valid_move(start_pos, end_pos):
            start_piece = self.board[start_pos[0]][start_pos[1]]
            end_piece = self.board[end_pos[0]][end_pos[1]]

            # Pawn promotion
            if start_piece == 'P' and end_pos[0] == 0:
                self.pawn_promotion(end_pos)

            # En passant
            if start_piece == 'P' and end_pos == self.en_passant_target:
                self.board[start_pos[0]][end_pos[1]] = ' '
            
            # Move the piece
            self.board[end_pos[0]][end_pos[1]] = start_piece
            self.board[start_pos[0]][start_pos[1]] = ' '

            # Update en passant target if applicable
            if start_piece == 'P' and abs(start_pos[0] - end_pos[0]) == 2:
                self.en_passant_target = ((start_pos[0] + end_pos[0]) // 2, start_pos[1])
            else:
                self.en_passant_target = None

            # Castling
            if start_piece in ['K', 'k'] and abs(start_pos[1] - end_pos[1]) == 2:
                if end_pos[1] > start_pos[1]:  # King side
                    self.board[end_pos[0]][end_pos[1] - 1] = self.board[end_pos[0]][end_pos[1] + 1]
                    self.board[end_pos[0]][end_pos[1] + 1] = ' '
                else:  # Queen side
                    self.board[end_pos[0]][end_pos[1] + 1] = self.board[end_pos[0]][end_pos[1] - 2]
                    self.board[end_pos[0]][end_pos[1] - 2] = ' '

            return True

        return False

# Example usage
board = ChessBoard()
board.print_board()

# Game loop
while not board.is_checkmate() and not board.is_stalemate() and not board.is_draw():
    start_pos = tuple(map(int, input("Enter start position (e.g., '2 4'): ").split()))
    end_pos = tuple(map(int, input("Enter end position (e.g., '3 4'): ").split()))

    if board.make_move(start_pos, end_pos):
        board.switch_turn()
        board.print_board()
    else:
        print("Invalid move. Try again.")

# Print game result
if board.is_checkmate():
    print("Checkmate! Player", board.current_turn, "wins!")
elif board.is_stalemate():
    print("Stalemate! The game is drawn.")
elif board.is_draw():
    print("Draw by agreement or insufficient material.")

