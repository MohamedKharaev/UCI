#connectfour_server.py
import connectfour
import connectfour_functions
import connectfour_sockets


def send_and_receive_move(current_game: connectfour.GameState, ai_connection: connectfour_sockets.Connection) -> str and str:
    '''Prompts player for a move and receives the ai move. Returns both'''
    while True:
        player_move = input(connectfour_functions.board_piece(current_game.turn) + "'s turn: ")
        if connectfour_functions.check_valid_move(player_move):
            connectfour_sockets.send_move(ai_connection, player_move)
            ai_move = connectfour_sockets.receive_ai_move(ai_connection)
            return player_move, ai_move

def execute_player_and_ai_move(current_game: connectfour.GameState, player_move: str, ai_move: str) -> connectfour.GameState:
    '''executes the moves peformed by the player and ai. Handles exceptions'''
    if ai_move == 'Invalid':
        return current_game
    elif ai_move == 'Game is over':
        current_game = connectfour_functions.execute_move(current_game, player_move)
        connectfour_functions.print_board(current_game)
        return current_game
    else:
        current_game = connectfour_functions.execute_move(current_game, player_move)
        connectfour_functions.print_board(current_game)
        print(connectfour_functions.board_piece(current_game.turn) + "'s turn: " + ai_move)
        current_game = connectfour_functions.execute_move(current_game, ai_move)
        connectfour_functions.print_board(current_game)
        return current_game


def run_game(current_game: connectfour.GameState, ai_connection: connectfour_sockets.Connection) -> int:
    '''Runs a continous loop of turns until the game is over'''
    while connectfour.winner(current_game) == connectfour.NONE:
        player_move, ai_move = send_and_receive_move(current_game, ai_connection)
        current_game = execute_player_and_ai_move(current_game, player_move, ai_move)
    return connectfour.winner(current_game)


if __name__ == '__main__':
    ai_connection = connectfour_sockets.connect()
    print(connectfour_sockets.login(ai_connection))
    connectfour_sockets.begin_game(ai_connection)
    game = connectfour_functions.start_game()
    winner = run_game(game, ai_connection)
    connectfour_functions.print_winner(winner)
    ai_connection.socket.close()

