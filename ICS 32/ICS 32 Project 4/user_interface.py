#Mohamed Kharaev 43121144. Lab Section 13
#user_interface.py
import othello
from collections import namedtuple

Settings = namedtuple('Settings', ['rows', 'cols', 'turn', 'mode'])

        
def input_game_settings() -> Settings:
    '''Requests user input for settings of the game and returns them as a Settings namedtuple'''
    rows = int(input())
    cols = int(input())
    turn = _convert_str_to_piece(input())
    mode = input()
    return Settings(rows, cols, turn, mode)


def initialize_board(game: othello.GameState) -> othello.GameState:
    '''User is able to initialize the game board with input'''
    for row in range(game.get_rows()):
        pieces = input()
        for i in range(game.get_cols()):
            game.board[row][i] = _convert_str_to_piece(pieces[i * 2])
    return game


def _convert_str_to_piece(piece: str) -> int:
    '''converts the string equivalent of a game piece to its piece value'''
    if piece == 'B':
        return othello.BLACK
    elif piece == 'W':
        return othello.WHITE
    else:
        return othello.NONE


def _piece_to_text(piece: int) -> str:
    '''converts a game piece to its string equivalent'''
    if piece == othello.BLACK:
        return 'B'
    elif piece == othello.WHITE:
        return 'W'
    else:
        return '.'


def _print_board(game: othello.GameState) -> None:
    '''Prints the GameState's board to the console'''
    print('B: {} W: {}'.format(game.get_scores()['black'], game.get_scores()['white']))
    for row in game.get_board():
        for piece in row:
            if piece == othello.NONE:
                print('.', end = ' ')
            elif piece == othello.BLACK:
                print('B', end = ' ')
            else:
                print('W', end = ' ')
        print()
    if game.check_any_move_possible():
        print('TURN: {}'.format(_piece_to_text(game.get_turn())))
    else:
        print('WINNER: {}'.format(_winner_str(game.winner())))


def _input_move(game: othello.GameState) -> int:
    '''User inputs their move (format: row col) and each of those is returned'''
    move = input()
    row, col = [(int(i) - 1) for i in move.split()]
    return row, col


def _winner_str(piece: int) -> str:
    '''returns a str that represents the winner'''
    if piece == othello.NONE:
        return 'NONE'
    else:
        return _piece_to_text(piece)


if __name__ == '__main__':
    print('FULL')
    settings = input_game_settings()
    game = othello.GameState(settings.rows, settings.cols, settings.turn, settings.mode)
    game = initialize_board(game)
    _print_board(game)
    while game.check_any_move_possible():
        row, col = _input_move(game)
        previous_board = othello.copy_game_board(game.get_board())
        try:
            game.make_move(row, col)
        except(othello.InvalidMove):
            pass
        if previous_board == game.get_board():
            print('INVALID')
        else:
            print('VALID')
            if game.check_any_move_possible():
                _print_board(game)
            else:
                pass
    _print_board(game)
    
        
