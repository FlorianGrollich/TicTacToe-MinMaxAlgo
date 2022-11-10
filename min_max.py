from tic_tac_toe_game import TicTacToeGame, Player


def maxValue(game: TicTacToeGame):
    is_game_over = game.check_for_win()
    if is_game_over != 0:
        return is_game_over
