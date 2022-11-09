from enum import Enum


class Player(Enum):
    X = "X"
    O = "O"
    N = "#"  # nothing


class TicTacToeGame:
    def __init__(self):
        # "#" = empty
        self.game_field: list[list[Player]] = [
            [Player.N, Player.N, Player.N],
            [Player.N, Player.N, Player.N],
            [Player.N, Player.N, Player.N],
        ]
        self.round: int = 0

    #   INDEX for playing field
    #   0 | 1 | 2
    #   ---------
    #   3 | 4 | 5
    #   ---------
    #   6 | 7 | 8
    def next_move(self, index: int) -> None:
        pass
    def check_for_win(self) -> bool:
        pass
