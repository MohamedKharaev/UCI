#connectfour_console.py
import connectfour
import connectfour_functions

def make_player_move(current_game: connectfour.GameState) -> connectfour.GameState:
    '''Calls on player to make a move and returns the new GameState'''
    while True:
        player_move = input(connectfour_functions.board_piece(current_game.turn) + "'s turn: ")
        if connectfour_functions.check_valid_move(player_move):
            return connectfour_functions.execute_move(current_game, player_move)


def run_game(current_game: connectfour.GameState) -> int:
    '''Runs a continous loop of turns until the game is over'''
    while connectfour.winner(current_game) == connectfour.NONE:
        current_game = make_player_move(current_game)
        connectfour_functions.print_board(current_game)
    return connectfour.winner(current_game)


if __name__ == '__main__':
    game = connectfour_functions.start_game()
    winner = run_game(game)
    connectfour_functions.print_winner(winner)


