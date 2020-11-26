#connectfour_functions.py
import connectfour


def print_board(current_gamestate: connectfour.GameState) -> None:
    '''Prints the current state of the Game'''
    board = current_gamestate.board
    for column_number in range(1, connectfour.BOARD_COLUMNS + 1):
        print(column_number, end = '  ')
    print()
    for row in range(connectfour.BOARD_ROWS):
        for column in range(connectfour.BOARD_COLUMNS):
            print(board_piece(board[column][row]), end = '  ')
        print()
            

def board_piece(piece_id: int) -> str:
    '''returns a letter representing the board piece it is given'''
    if piece_id == connectfour.NONE:
        return '.'
    elif piece_id == connectfour.RED:
        return 'R'
    elif piece_id == connectfour.YELLOW:
        return 'Y'
    else:
        return piece_id
        

def check_valid_move(move: str) -> bool:
    '''Checks if the given moce follows the game's protocol'''
    move = move.split()
    if len(move) == 2:
        if move[0] == 'DROP' or move[0] == 'POP':
            try:
                type(int(move[1]))
            except:
                pass
            else:
                return True
    print('Invalid Move')
    return False


def execute_move(current_gamestate: connectfour.GameState, move: str) -> connectfour.GameState:
    '''returns a GameState in which the given move has been performed'''
    command, column = move.split()
    column = int(column) - 1

    if command == 'DROP':
        try:
            return connectfour.drop(current_gamestate, column)
        except(ValueError):
            print('Column doesn\'t exist. Try again')
        except(connectfour.InvalidMoveError):
            print('That column is full. Try again')
        except(connectfour.GameOverError):
            pass
    else:
        try:
            return connectfour.pop(current_gamestate, column)
        except(ValueError):
            print('Column doesn\'t exist. Try again')
        except(connectfour.InvalidMoveError):
            print('You can\'t pop a piece from there. Try again')
        except(connectfour.GameOverError):
            pass
    return current_gamestate

 
def start_game() -> connectfour.GameState:
    '''Initiates a new game'''
    new_game = connectfour.new_game()
    print('Take your turn by typing DROP or POP followed by the column number (EX: DROP 1)')
    print_board(new_game)
    return new_game


def print_winner(winner: int) -> None:
    '''Prints a winner banner depending on which player won'''
    if winner == connectfour.RED:
        print('Red Wins!')
    elif winner == connectfour.YELLOW:
        print('Yellow Wins!')
    else:
        print(winner)
