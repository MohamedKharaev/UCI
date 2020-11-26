#connectfour_sockets.py
import socket
from collections import namedtuple
import sys

Connection = namedtuple('Connection', 'socket, input, output')

def connect() -> Connection:
    '''Prompts user to connect to a sevrer and returns a Connection'''
    while True:
        connect_socket = socket.socket()
        host = input("What host would you like to connect to?\n")
        port = input("What is the port number?\n")
        try:
            connect_socket.connect((host, int(port)))
            connect_input = connect_socket.makefile('r')
            connect_output = connect_socket.makefile('w')
            return Connection(connect_socket,
                              connect_input,
                              connect_output)
        except(ValueError):
            print('Port was not a number')
        except(TimeoutError):
            print('Invalid Port')
        except(socket.gaierror):
            print('Invalid Host')
        except(ConnectionRefusedError):
            print('Server actively refused connection')
        except(OverflowError):
            print('Port was not a number between 0 and 65535')


def login(current_connection: Connection) -> str:
    '''Prompts the user to login and ensures the given server is following protocol'''
    while True:
        login_name = input("What is your username? (Must be one word)\n")
        if len(login_name.split()) != 1:
            print('Invalid username')
        else:
            login_message = 'I32CFSP_HELLO ' + login_name
            _write_line(current_connection, login_message)
            return_message = _read_line(current_connection)
            if return_message == 'WELCOME ' + login_name:
                return return_message
            else:
                sys.exit()


def begin_game(current_connection: Connection) -> None:
    '''Sends the start game message to the server'''
    _write_line(current_connection, 'AI_GAME')
    print(_read_line(current_connection))


def send_move(current_connection: Connection, move: str) -> None:
    '''Sends the given move to the server'''
    _write_line(current_connection, move)
    return


def receive_ai_move(current_connection: Connection) -> str:
    '''Reades the output from the server and returns the server's move.
    If the server doesn't perform a move, a message is returned that
    represents the server message.'''
    ai_line1 = _read_line(current_connection)
    if ai_line1 == 'OKAY':
        ai_move = _read_line(current_connection)
        _read_line(current_connection)
    elif ai_line1 == 'INVALID':
        print(ai_line1)
        ai_move = 'Invalid'
        _read_line(current_connection)
    elif ai_line1 == 'WINNER_RED' or ai_line1 == 'WINNER_YELLOW':
        ai_move = 'Game is over'
    else:
        sys.exit()
    return ai_move
    
    

def _write_line(current_connection: Connection, text: str) -> None:
    '''sends a line to the server with formating'''
    current_connection.output.write(text + '\r\n')
    current_connection.output.flush()


def _read_line(current_connection: Connection) -> str:
    '''reads the last line sent from the server without the \n'''
    return current_connection.input.readline()[:-1]

