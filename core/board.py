from core.move_generator import get_legal_moves
from core.rules import can_castle_kingside, can_castle_queenside
from core.utils import (WHITE_KING, BLACK_KING,
                               WHITE_ROOK, BLACK_ROOK)

class Board:
    def __init__(self):
        self.board = self._create_starting_position()
        self.turn = "white"
        self.white_king_moved = False
        self.black_king_moved = False
        self.white_rook_kingside_moved = False
        self.white_rook_queenside_moved = False
        self.black_rook_kingside_moved = False
        self.black_rook_queenside_moved = False

    @property
    def castling_rights(self):
          rights = ""
          if can_castle_kingside(self, white_player=True):
               rights += "K"
          if can_castle_queenside(self, white_player=True):
               rights += "Q"
          if can_castle_kingside(self, white_player=False):
               rights += "k"
          if can_castle_queenside(self, white_player=False):
               rights += "q"
          return rights if rights else "-"
        
    def _create_starting_position(self):
         return [
            ["♜", "♞", "♝", "♛", "♚", "♝", "♞", "♜"],
            ["♟", "♟", "♟", "♟", "♟", "♟", "♟", "♟"],
            ["·", "·", "·", "·", "·", "·", "·", "·"],
            ["·", "·", "·", "·", "·", "·", "·", "·"],
            ["·", "·", "·", "·", "·", "·", "·", "·"],
            ["·", "·", "·", "·", "·", "·", "·", "·"],
            ["♙", "♙", "♙", "♙", "♙", "♙", "♙", "♙"],
            ["♖", "♘", "♗", "♕", "♔", "♗", "♘", "♖"],
        ]
    
    def display(self):
         print("  a b c d e f g h")
         print("  ---------------")

         for i, row in enumerate(self.board):
              print(8 - i, end="|")
              for piece in row:
                  print(piece, end=" ")
              print("|" + str(8 - i))
        
         print("  ---------------")
         print("  a b c d e f g h")

    
    def move_piece(self, start, end):
        start_row, start_col = start
        end_row, end_col = end
        
        piece = self.board[start_row][start_col]
        if piece == "·":
            raise ValueError("No piece at this position!")
        
        is_king = (piece == WHITE_KING or piece == BLACK_KING)
        is_castling = (
            is_king and
            start_col == 4 and
            end_row == start_row and
            abs(end_col - start_col) == 2
        )
        
        self.update_flags_for_castling(piece, start_row, start_col)
        
        self.board[end_row][end_col] = piece
        self.board[start_row][start_col] = "·"
        
        if is_castling:
            if piece == WHITE_KING and start_row == 7:
                if end_col == 6:
                    self.board[7][5] = WHITE_ROOK
                    self.board[7][7] = "·"
                    self.white_rook_kingside_moved = True
                else:
                    self.board[7][3] = WHITE_ROOK
                    self.board[7][0] = "·"
                    self.white_rook_queenside_moved = True
            elif piece == BLACK_KING and start_row == 0:
                if end_col == 6:
                    self.board[0][5] = BLACK_ROOK
                    self.board[0][7] = "·"
                    self.black_rook_kingside_moved = True
                else:
                    self.board[0][3] = BLACK_ROOK
                    self.board[0][0] = "·"
                    self.black_rook_queenside_moved = True
        
        if piece == "♙" and end_row == 0:
            self.board[end_row][end_col] = "♕"
        elif piece == "♟" and end_row == 7:
            self.board[end_row][end_col] = "♛"
        
        self.turn = "black" if self.turn == "white" else "white"


    
    def notation_to_index(self, notation):
         files = "abcdefgh"
         ranks = "12345678"

         if len(notation) != 2 or notation[0] not in files or notation[1] not in ranks:
              raise ValueError(f"Invalid notation: {notation}")
         
         col = files.index(notation[0])
         row = 8 - int(notation[1])

         return (row, col)
    
    def index_to_notation(self, row, col):
         files = "abcdefgh"
         if not (0 <= row < 8 and 0 <= col < 8):
              raise ValueError(f"Invalid index: {(row, col)}")
         
         file = files[col]
         rank = str(8 - row)

         return f"{file}{rank}"
    
    
    def move_piece_notation(self, start_notation, end_notation):
         start = self.notation_to_index(start_notation)
         end = self.notation_to_index(end_notation)

         self.move_piece(start, end)

    def get_legal_moves(self, row, col):
         return get_legal_moves(self, row, col)
    

    def update_flags_for_castling(self, piece, start_row, start_col):
         if piece == WHITE_KING:
              self.white_king_moved = True
         elif piece == BLACK_KING:
              self.black_king_moved = True
         elif piece == WHITE_ROOK:
              if start_row == 7 and start_col == 0:
                   self.white_rook_queenside_moved = True
              elif start_row == 7 and start_col == 7:
                   self.white_rook_kingside_moved = True
         elif piece == BLACK_ROOK:
              if start_row == 0 and start_col == 0:
                   self.black_rook_queenside_moved = True
              elif start_row == 0 and start_col == 7:
                   self.black_rook_kingside_moved = True


if __name__ == "__main__":
     board = Board()
     board.display()