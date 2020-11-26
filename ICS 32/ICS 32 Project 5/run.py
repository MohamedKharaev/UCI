#Mohamed Kharaev 43121144. Lab Section 13
#run.py
import settings
import othello
import othelloGUI

if __name__ == '__main__':
    settings = settings.SettingsAPP()
    settings.run()
    game = othello.GameState(settings.selected_rows,
                             settings.selected_cols,
                             settings.selected_bw,
                             settings.selected_mode)
    init_gameGUI = othelloGUI.Initialize_Board_GUI(game)
    init_gameGUI.run()
    game = init_gameGUI.game
    othelloGUI.GameGUI(game).run()
    
    
