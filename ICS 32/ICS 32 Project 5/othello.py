#Mohamed Kharaev 43121144. Lab Section 13
#othello.py

NONE = 0
WHITE = 1
BLACK = 2


class GameOverError(Exception):
    '''Raised whenever an attempt is made to make a move after the
    game is already over'''
    pass

class InvalidMove(Exception):
    '''Raised whenever an attempt is made to make a move that is not valid'''
    pass


class GameState:
    '''GameState represents an othello game'''
    def __init__(self, rows: int, cols: int, turn: int, mode: str) -> None:
        self.rows = rows
        self.cols = cols
        self.board = _new_game_board(rows, cols)
        self.turn = turn
        self.mode = mode


    def get_rows(self) -> int:
        '''returns the amount of rows in the gameboard'''
        return self.rows

    def get_cols(self) -> int:
        '''returns the amount of cols in the gameboard'''
        return self.cols

    def get_turn(self) -> int:
        '''returns the current turn in the gamestate'''
        return self.turn

    def get_board(self) -> int:
        '''returns the gameboard'''
        return self.board

        
    def get_scores(self) -> [int, int]:
        '''creates a dictionary containing the amount of black and white pieces on the board. returns the dictionary'''
        scores = {'black': 0, 'white': 0}
        for row in self.board:
            for piece in row:
                if piece == BLACK:
                    scores['black'] += 1
                elif piece == WHITE:
                    scores['white'] += 1
        return scores


    def winner(self) -> int:
        '''Returns the winner of the GameState based on the game mdoe'''
        white_score = self.get_scores()['white']
        black_score = self.get_scores()['black']
        if self.mode == '>':
            if white_score > black_score:
                return WHITE
            elif black_score > white_score:
                return BLACK
            else:
                return NONE
        if self.mode == '<':
            if white_score > black_score:
                return BLACK
            elif black_score > white_score:
                return WHITE
            else:
                return NONE


    def check_move_possible(self, row: int, col: int) -> bool:
        '''checks the game board to see if a move is possible. if one is,
        True is returned. Otherwise the function returns False'''

        try:
            if self.board[row][col] != NONE:
                return False
        except(IndexError):
            return False

        for dir_row in range(-1, 2):
            for dir_col in range(-1, 2):
                try:
                    if (row + dir_row) >= 0 and (col + dir_col) >= 0:
                        if self.board[row + dir_row][col + dir_col] == opposite_turn(self.turn):
                            for i in range(2, max(self.rows, self.cols)):
                                if (row + (dir_row * i)) >= 0 and (col + (dir_col * i)) >= 0:
                                    piece = self.board[row + (dir_row * i)][col + (dir_col * i)]
                                    if piece == NONE:
                                        break
                                    if piece == self.turn:
                                        return True
                except(IndexError):
                    pass
        return False


    def check_any_move_possible(self) -> bool:
        '''Checks if there is any possible move for the current player'''
        
        for row in range(self.rows):
            for col in range(self.cols):
                if self.check_move_possible(row, col):
                    return True
        return False
    
                     
    def make_move(self, row: int, col: int) -> [[int]]:
        '''Executes a move'''

        if row not in list(range(self.get_rows())) or col not in list(range(self.get_cols())):
            raise InvalidMove()

        _require_game_not_over(self)
        
        original_board = copy_game_board(self.board)
        if self.check_move_possible(row, col):
            for dir_row in range(-1, 2):
                for dir_col in range(-1, 2):
                    temp_list = list()
                    try:
                        if (row + dir_row) >= 0 and (col + dir_col) >= 0:
                            if self.board[row + dir_row][col + dir_col] == opposite_turn(self.turn):
                                for i in range(1, max(self.rows, self.cols)):
                                    if (row + (dir_row * i)) >= 0 and (col + (dir_col * i)) >= 0:
                                        piece = self.board[row + (dir_row * i)][col + (dir_col * i)]
                                        if piece == opposite_turn(self.turn):
                                            temp_list.append(piece)
                                        elif piece == self.turn:
                                            temp_list.append(piece)
                                            break
                                        else:
                                            break
                    except(IndexError):
                        pass
                    if len(temp_list) > 0:
                        if temp_list[-1] == self.turn:
                            for i in range(1, len(temp_list)):
                                self.board[row + (dir_row * i)][col + (dir_col * i)] = opposite_turn(temp_list[i - 1])
                                
                        
            self.board[row][col] = self.turn
            self.turn = opposite_turn(self.turn)
            if self.check_any_move_possible():
                pass
            else:
                self.turn = opposite_turn(self.turn)
                if _is_board_full(self.board):
                   pass

        
def _is_board_full(board: [[int]]) -> bool:
    '''Checks if there are any empty spots on a gameboard (list of list of ints))'''
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == NONE:
                return False
    return True

def _new_game_board(rows: int, cols: int) -> [[int]]:
    '''
    Creates a new game board.  Initially, a game board has the size
    rows x cols and is comprised only of integers with the
    value NONE
    '''
    board = []
    
    for row in range(rows):
        board.append([])
        for col in range(cols):
            board[-1].append(NONE)

    return board


def copy_game_board(board: [[int]]) -> [[int]]:
    '''Copies the given game board'''
    board_copy = []

    for col in range(len(board)):
        board_copy.append([])
        for row in range(len(board[0])):
            board_copy[-1].append(board[col][row])

    return board_copy


def opposite_turn(turn: int) -> int:
    '''Given the player whose turn it is now, returns the opposite player'''
    if turn == WHITE:
        return BLACK
    else:
        return WHITE


def _require_game_not_over(game: GameState) -> None:
    '''Raises a GameOverError if the game can't have any more moves executed'''
    if not game.check_any_move_possible():
        raise GameOverError()
    

