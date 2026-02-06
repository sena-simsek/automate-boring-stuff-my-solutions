def isValidChessBoard(board:dict):
   white_peaces = 0
   black_peaces = 0
   white_king = 0
   black_king = 0
   valid = ['P','N','B','R','Q','K']
   for position, piece in board.items():
      if piece.startswith('w') :
         white_peaces += 1
         if piece == 'wK':
            white_king += 1
      elif piece.startswith('b') :
         black_peaces += 1
         if piece == 'bK':
            black_king += 1
      else:
         return False

      if position[0] in 'abcdefgh' and position[1] in '12345678':
         if piece[1] in valid:
            pass
         else:
            return False
      else:
         return False

   all_pieces = list(board.values())
   white_pawns = all_pieces.count('wP')
   black_pawns = all_pieces.count('bP')
   if white_pawns > 8 or black_pawns > 8:
      return False

   if white_king != 1 or black_king != 1:
      return False

   if white_peaces > 16 or black_peaces > 16:
      return False

   return True




# Geçerli bir tahta
print(isValidChessBoard({'h1': 'bK', 'c6': 'wP', 'g2': 'wK'}))

# Geçersiz (2 beyaz şah var)
print(isValidChessBoard({'1h': 'bK', '6c': 'wK', '2g': 'wK'}))

# Geçersiz (Konum hatalı)
print(isValidChessBoard({'9z': 'bK', '6c': 'wK'}))
