#Mohamed Kharaev 43121144. Lab Section 13

import othello
import tkinter

class GameGUI:
    def __init__(self, game: othello.GameState):
        self.game = game
        self.hori_lines_decimals = list(i/game.get_rows() for i in range(1, game.get_rows() + 1))
        self.vert_lines_decimals = list(i/game.get_cols() for i in range(1, game.get_cols() + 1))

        self._window = tkinter.Tk()

        self._status = tkinter.Canvas(master = self._window,
                                      width = 500,
                                      height = 50,
                                      background = 'white')
        
        self._status.grid(row = 0, column = 0,
                          sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._window.bind('<Configure>', self._on_window_resized)

        self._window.rowconfigure(0, weight = 1)
        self._window.rowconfigure(1, weight = 1)
        self._window.columnconfigure(0, weight = 1)
        
        self._board = tkinter.Canvas(
            master = self._window,
            height = 500,
            width = 500,
            background = '#9BF0FF')
        
        self._board.grid(row = 1, column = 0,
                         sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._board.bind('<Button-1>', self._board_pressed)

        
    def run(self) -> None:
        '''Runs the tkinter window'''
        self._window.mainloop()

    def _on_window_resized(self, event: tkinter.Event) -> None:
        '''Accomodates for the tkinter window being resized'''
        self._status.delete(tkinter.ALL)
        self._board.delete(tkinter.ALL)
        
        status_width = self._status.winfo_width()
        status_height = self._status.winfo_height()
        board_width = self._board.winfo_width()
        board_height = self._board.winfo_height()

        self._update_board()

        if self.game.check_any_move_possible():
            self._score_text = 'B: {} | W: {}'.format(self.game.get_scores()['black'], self.game.get_scores()['white'])
            self._turn_text = 'Turn: {}'.format(_piece_to_text(self.game.get_turn()))
            
            self._status.create_text(.1 * status_width,
                                     .5 * status_height,
                                     text = self._turn_text)
            self._status.create_text(.5 * status_width,
                                     .5 * status_height,
                                     text = 'FULL')
            self._status.create_text(.9 * status_width,
                                     .5 * status_height,
                                     text = self._score_text)
        else:
            self._score_text = 'B: {} | W: {}'.format(self.game.get_scores()['black'], self.game.get_scores()['white'])
            self._winner_text = 'Winner: {}'.format(_winner_str(self.game.winner()))
            
            self._status.create_text(.9 * status_width,
                                     .5 * status_height,
                                     text = self._score_text)
            self._status.create_text(.1 * status_width,
                                     .5 * status_height,
                                     text = self._winner_text)

        
        for vert_line in self.vert_lines_decimals:
            self._board.create_line(vert_line * board_width,
                                     0,
                                     vert_line * board_width,
                                     board_height)
        
        for hori_line in self.hori_lines_decimals:
            self._board.create_line(0,
                                     hori_line * board_height,
                                     board_width,
                                     hori_line * board_height)


    def _board_pressed(self, event: tkinter.Event) -> None:
        '''Registers a move that the user makes by pressing the board and makes it in the game'''
        self._status.delete(tkinter.ALL)
        self._board.delete(tkinter.ALL)
        
        status_width = self._status.winfo_width()
        status_height = self._status.winfo_height()
        board_width = self._board.winfo_width()
        board_height = self._board.winfo_height()

        
        board_click_coordinate_x = int(event.x / board_width * self.game.get_cols())
        board_click_coordinate_y = int(event.y / board_height * self.game.get_rows())
        
        try:
            self.game.make_move(board_click_coordinate_y, board_click_coordinate_x)
        except(othello.GameOverError):
            pass
        except(othello.InvalidMove):
            pass
            
        self._update_board()

        if self.game.check_any_move_possible():
            self._score_text = 'B: {} | W: {}'.format(self.game.get_scores()['black'], self.game.get_scores()['white'])
            self._turn_text = 'Turn: {}'.format(_piece_to_text(self.game.get_turn()))
            
            self._status.create_text(.1 * status_width,
                                     .5 * status_height,
                                     text = self._turn_text)
            self._status.create_text(.5 * status_width,
                                     .5 * status_height,
                                     text = 'FULL')
            self._status.create_text(.9 * status_width,
                                     .5 * status_height,
                                     text = self._score_text)
        else:
            self._score_text = 'B: {} | W: {}'.format(self.game.get_scores()['black'], self.game.get_scores()['white'])
            self._winner_text = 'Winner: {}'.format(_winner_str(self.game.winner()))
            
            self._status.create_text(.9 * status_width,
                                     .5 * status_height,
                                     text = self._score_text)
            self._status.create_text(.1 * status_width,
                                     .5 * status_height,
                                     text = self._winner_text)


        
        for vert_line in self.vert_lines_decimals:
            self._board.create_line(vert_line * board_width,
                                     0,
                                     vert_line * board_width,
                                     board_height)
        
        for hori_line in self.hori_lines_decimals:
            self._board.create_line(0,
                                     hori_line * board_height,
                                     board_width,
                                     hori_line * board_height)


    def _draw_piece_from_center(self, frac_x: float, frac_y: float, color: int) -> None:
        '''Draws a circle in the given fractional coordinates and fills it with the given color'''
        radius_x = .5/self.game.get_cols()
        radius_y = .5/self.game.get_rows()
        
        board_width = self._board.winfo_width()
        board_height = self._board.winfo_height()
        
        if color == othello.BLACK:
            piece_color = 'black'
        elif color == othello.WHITE:
            piece_color = 'white'
            
        self._board.create_oval((frac_x - radius_x) * board_width ,
                                 (frac_y - radius_y) * board_height,
                                 (frac_x + radius_x) * board_width,
                                 (frac_y + radius_y) * board_height,
                                 fill = piece_color)


    def _update_board(self) -> None:
        '''Reads the game board and draws the pieces in the GUI'''
        for row in range(self.game.get_rows()):
            for col in range(self.game.get_cols()):
                if self.game.board[row][col] != othello.NONE:                                  
                    self._draw_piece_from_center(col/self.game.get_cols() + (.5 / self.game.get_cols()),
                                                 row/self.game.get_rows() + (.5 / self.game.get_rows()),
                                                 self.game.board[row][col])
                    

class Initialize_Board_GUI:
    def __init__(self, game: othello.GameState) -> None:
        self.game = game
        self.first_turn = self.game.get_turn()
        
        self.hori_lines_decimals = list(i/game.get_rows() for i in range(1, game.get_rows() + 1))
        self.vert_lines_decimals = list(i/game.get_cols() for i in range(1, game.get_cols() + 1))

        self._i_window = tkinter.Tk()

        self._i_status = tkinter.Canvas(
            master = self._i_window,
            height = 50,
            width= 500,
            background = 'white')

        self._i_status.grid(row = 0, column = 0,
                            sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._i_board = tkinter.Canvas(
            master = self._i_window,
            height = 500,
            width = 500,
            background = '#9BF0FF')

        self._i_board.grid(row = 1, column = 0,
                           sticky = tkinter.N + tkinter.S + tkinter.W + tkinter.E)

        self._switch_button = tkinter.Button(
            master = self._i_window,
            text = 'Switch Piece',
            command = self._switch_button_on)

        self._switch_button.grid(row = 2, column = 0,
                                 sticky = tkinter.S + tkinter.E)

        self._done_button = tkinter.Button(
            master = self._i_window,
            text = 'Done',
            command = self._done_button_on)

        self._done_button.grid(row = 3, column = 0,
                               sticky = tkinter.N + tkinter.E)
        
        self._i_window.rowconfigure(0, weight = 1)
        self._i_window.rowconfigure(1, weight = 1)
        self._i_window.rowconfigure(2, weight = 1)
        self._i_window.rowconfigure(3, weight = 1)
        self._i_window.columnconfigure(0, weight = 1)

        self._i_window.bind('<Configure>', self._on_window_resized)
        self._i_board.bind('<Button-1>', self._board_pressed)

    def run(self) -> None:
        '''Runs the tkinter window'''
        self._i_window.mainloop()

    def _switch_button_on(self) -> None:
        '''Switches the piece that the user can place on the board'''
        self._i_status.delete(tkinter.ALL)
        self.game.turn = othello.opposite_turn(self.game.get_turn())
        status_width = self._i_status.winfo_width()
        status_height = self._i_status.winfo_height()
        
        self._status_text = 'Place pieces by pressing on the board. Currently placing {}'.format(_piece_to_text(self.game.get_turn()))

        self._i_status.create_text(.5 * status_width,
                                     .5 * status_height,
                                     text = self._status_text)

    def _done_button_on(self) -> None:
        '''destroys the window and sets the turn back to the intended first turn'''
        self.game.turn = self.first_turn
        self._i_window.destroy()

    def _on_window_resized(self, event: tkinter.Event) -> None:
        '''Accomodates for the tkinter window being resized'''
        self._i_status.delete(tkinter.ALL)
        self._i_board.delete(tkinter.ALL)
        
        status_width = self._i_status.winfo_width()
        status_height = self._i_status.winfo_height()
        board_width = self._i_board.winfo_width()
        board_height = self._i_board.winfo_height()

        self._update_board()

        self._status_text = 'Place pieces by pressing on the board. Currently placing {}'.format(_piece_to_text(self.game.get_turn()))

        self._i_status.create_text(.5 * status_width,
                                     .5 * status_height,
                                     text = self._status_text)    
        for vert_line in self.vert_lines_decimals:
            self._i_board.create_line(vert_line * board_width,
                                     0,
                                     vert_line * board_width,
                                     board_height)
        
        for hori_line in self.hori_lines_decimals:
            self._i_board.create_line(0,
                                     hori_line * board_height,
                                     board_width,
                                     hori_line * board_height)


    def _board_pressed(self, event: tkinter.Event) -> None:
        '''Places a piece on the board wherever the player presses the screen.
        If a piece is already there, the piece is removed.'''
        self._i_status.delete(tkinter.ALL)
        self._i_board.delete(tkinter.ALL)
        
        status_width = self._i_status.winfo_width()
        status_height = self._i_status.winfo_height()
        board_width = self._i_board.winfo_width()
        board_height = self._i_board.winfo_height()

        
        board_click_coordinate_x = int(event.x / board_width * self.game.get_cols())
        board_click_coordinate_y = int(event.y / board_height * self.game.get_rows())

        
        if self.game.board[board_click_coordinate_y][board_click_coordinate_x] == self.game.get_turn():
            self.game.board[board_click_coordinate_y][board_click_coordinate_x] = othello.NONE
        else:
            self.game.board[board_click_coordinate_y][board_click_coordinate_x] = self.game.get_turn()

        self._update_board()

        self._status_text = 'Place pieces by pressing on the board. Currently placing {}'.format(_piece_to_text(self.game.get_turn()))

        self._i_status.create_text(.5 * status_width,
                                     .5 * status_height,
                                     text = self._status_text)    
        for vert_line in self.vert_lines_decimals:
            self._i_board.create_line(vert_line * board_width,
                                     0,
                                     vert_line * board_width,
                                     board_height)
        
        for hori_line in self.hori_lines_decimals:
            self._i_board.create_line(0,
                                     hori_line * board_height,
                                     board_width,
                                     hori_line * board_height)


    def _draw_piece_from_center(self, frac_x: float, frac_y: float, color: int) -> None:
        '''Draws a circle in the given fractional coordinates and fills it with the given color'''
        radius_x = .5/self.game.get_cols()
        radius_y = .5/self.game.get_rows()
        
        board_width = self._i_board.winfo_width()
        board_height = self._i_board.winfo_height()
        
        if color == othello.BLACK:
            piece_color = 'black'
        elif color == othello.WHITE:
            piece_color = 'white'
            
        self._i_board.create_oval((frac_x - radius_x) * board_width ,
                                 (frac_y - radius_y) * board_height,
                                 (frac_x + radius_x) * board_width,
                                 (frac_y + radius_y) * board_height,
                                 fill = piece_color)


    def _update_board(self) -> None:
        '''Reads the game board and draws the pieces in the GUI'''
        for row in range(self.game.get_rows()):
            for col in range(self.game.get_cols()):
                if self.game.board[row][col] != othello.NONE:                                  
                    self._draw_piece_from_center(col/self.game.get_cols() + (.5 / self.game.get_cols()),
                                                 row/self.game.get_rows() + (.5 / self.game.get_rows()),
                                                 self.game.board[row][col])
    
        
def _piece_to_text(piece: int) -> str:
    '''Converts a piece integer to its respective string'''
    if piece == othello.WHITE:
        return 'W'
    else:
        return 'B'


def _winner_str(piece: int) -> str:
    '''returns a str that represents the winner'''
    if piece == othello.NONE:
        return 'NONE'
    else:
        return _piece_to_text(piece)
    
