import tkinter

BLACK = 2
WHITE = 1

class SettingsAPP:
    def __init__(self):
        self._s_window = tkinter.Tk()
        
        tkinter.Label(self._s_window, text = 'Rows').grid(row = 0)
        tkinter.Label(self._s_window, text = 'Cols').grid(row = 0, column = 1)
        tkinter.Label(self._s_window, text = 'Black or White').grid(row = 0, column = 2)
        tkinter.Label(self._s_window, text = 'Mode').grid(row = 0, column = 3)
        
        

        self._row_box = tkinter.Listbox(
            exportselection = 0,
            master = self._s_window,
            height = 7,
            selectmode = tkinter.SINGLE)
        self._row_box.insert(1, 4)
        self._row_box.insert(2, 6)
        self._row_box.insert(3, 8)
        self._row_box.insert(4, 10)
        self._row_box.insert(5, 12)
        self._row_box.insert(6, 14)
        self._row_box.insert(7, 16)

        self._row_box.grid(
            row = 1, column = 0)

        self._col_box = tkinter.Listbox(
            exportselection = 0,
            master = self._s_window,
            height = 7,
            selectmode = tkinter.SINGLE)
        self._col_box.insert(1, 4)
        self._col_box.insert(2, 6)
        self._col_box.insert(3, 8)
        self._col_box.insert(4, 10)
        self._col_box.insert(5, 12)
        self._col_box.insert(6, 14)
        self._col_box.insert(7, 16)

        self._col_box.grid(
            row = 1, column = 1)

        self._bw_box = tkinter.Listbox(
            exportselection = 0,
            master = self._s_window,
            height = 7,
            selectmode = tkinter.SINGLE)
        self._bw_box.insert(1, 'B')
        self._bw_box.insert(2, 'W')

        self._bw_box.grid(
            row = 1, column = 2)

        self._mode_box = tkinter.Listbox(
            exportselection = 0,
            master = self._s_window,
            height = 7,
            selectmode = tkinter.SINGLE)
        self._mode_box.insert(1, '>')
        self._mode_box.insert(2, '<')

        self._mode_box.grid(
            row = 1, column = 3)

        # Incase the user closes the window without selecting options, a default 4x4 board
        # is made where the first player is white and the mode is >
        self.selected_rows = 4
        self.selected_cols = 4
        self.selected_bw = 1
        self.selected_mode = '>'

        self._submit_button = tkinter.Button(
            master = self._s_window,
            text = 'Run Othello',
            command = self._submit_pressed)

        self._submit_button.grid(
            row = 1, column = 4)


        
    def run(self) -> None:
        '''Runs the tkinter window'''
        self._s_window.mainloop()

    def _submit_pressed(self) -> None:
        '''Saves all the values that were selected in the listboxes'''
        try:
            self.selected_rows = self._row_box.get(self._row_box.curselection()[0])
        except(IndexError):
            pass
        try:
            self.selected_cols = self._col_box.get(self._col_box.curselection()[0])
        except(IndexError):
            pass
        try:
            self.selected_bw = _piece_to_int(self._bw_box.get(self._bw_box.curselection()[0]))
        except(IndexError):
            pass
        try:
            self.selected_mode = self._mode_box.get(self._mode_box.curselection()[0])
        except(IndexError):
            pass
        
        self._s_window.destroy()
        

def _piece_to_int(piece: str) -> int:
    '''Converts a piece string to its respective integer'''
    if piece == 'B':
        return BLACK
    else:
        return WHITE

    
