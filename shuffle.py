import board
import movement_logic
import random
def shuffle(size):
    state = board.build_solved_board(size)
    dictionary = board.create_grid_dictionary(state)
    legal_moves = movement_logic.legal_moves(dictionary)
    for i in range(200):
        blank = movement_logic.find_blank(dictionary)
        move = random.choice(legal_moves)
        movement_logic.apply_move(dictionary, move)
        legal_moves = movement_logic.legal_moves(dictionary) 
        legal_moves.remove(blank)
    return dictionary     
