import board
def find_blank(dictionary):
    for coordinate, piece in dictionary.items():
        if piece == "_":
            return coordinate
        
def legal_moves(dictionary):
    legal_moves = []
    r0, c0 = find_blank(dictionary)
    for coordinate in dictionary:
        r, c = coordinate
        if (r, c) == (r0 + 1, c0) or (r, c) == (r0 - 1, c0) or (r, c) == (r0, c0 + 1) or (r, c) == (r0, c0 - 1):
            legal_moves.append((r,c))
    return legal_moves

def apply_move(dictionary, move):
    leg_moves = legal_moves(dictionary)
    if move in leg_moves:
        piece = dictionary[move]
        blank = find_blank(dictionary)
        dictionary[blank] = piece
        dictionary[move] = "_"
        return True
    else:
        print("not a legal move")
        return False
    
def is_solved(dictionary):
    length = len(dictionary)
    if length == 9:
        size = "1"
    elif length == 12:
        size = "2"
    elif length == 16:
        size = "3"
    state = board.build_solved_board(size)
    solved_dictionary = board.create_grid_dictionary(state)
    if dictionary == solved_dictionary:
        return True
    else:
        return False
    
