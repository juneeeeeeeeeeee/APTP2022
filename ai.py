import main
import numpy as np
def ai_move(board, searches_per_move, search_length):
  first_moves=[move_down, move_left, move_right, move_up]
  scores=np.zeros(4) # 점수 저장하는 배열
  for first_index in range(4):
    first_move=first_moves[first_index]
    first_board, first_valid, first_score=first_move(board)