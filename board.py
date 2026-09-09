def choose_size():
    print("1) 3x3")
    print("2) 3x4")
    print("3) 4x4")
    size = input("Pick an option: ")
    return size

def build_solved_board(size):
    if size == "1":
        State = [1,2,3,4,5,6,7,8,"_"]
    elif size == "2":
        State = [1,2,3,4,5,6,7,8,9,10,11,"_"]
    elif size == "3":
        State = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,"_"]
    return State

def create_solved_board():
    size = choose_size()
    return build_solved_board(size)

def num_of_columns(State):
    number_of_columns = 'Nill'
    if len(State) == 9:
        number_of_columns = 3
    elif len(State) == 12:
        number_of_columns = 4
    elif len(State) == 16:
        number_of_columns = 4
    return number_of_columns

def num_of_rows(State):
    number_of_columns = num_of_columns(State)
    number_of_rows = len(State)//number_of_columns
    return number_of_rows
        
def coordinates(State,index):
    number_of_columns = num_of_columns(State)
    row = index//number_of_columns
    col = index%number_of_columns
    return (row,col)

def create_grid_dictionary(State):
    dictionary = dict()
    for index, piece in enumerate(State):
        dictionary[coordinates(State,index)] = piece
    return dictionary
        
def print_grid(State):
    number_of_columns = num_of_columns(State)
    for index, piece in enumerate(State):
        if (index + 1) % number_of_columns == 0:
            print(piece)
        else:
            print(piece, end = " ")