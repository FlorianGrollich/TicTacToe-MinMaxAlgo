from enum import Enum


class Player(Enum):
    X = "X"
    O = "O"
    N = "#"  # nothing --> empty field


class TicTacToeGame:
    def __init__(self):
        #   INDEX for playing field
        #   0 | 1 | 2
        #   ---------
        #   3 | 4 | 5
        #   ---------
        #   6 | 7 | 8
        self.game_field: list[Player] = [
            Player.N, Player.N, Player.N,
            Player.N, Player.N, Player.N,
            Player.N, Player.N, Player.N]

        self.round: int = 1



    def next_move(self, index: int) -> None:
        next_player = Player.X if self.round % 2 == 0 else Player.O

        if self.game_field[index] == Player.N:
            self.game_field[index] = next_player
            self.round += 1
        else:
            raise Exception("There is already a player on that field")

    def check_for_win(self) -> bool:
        win_possibilities: list[list[int]] = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [0, 3, 6],
            [1, 4, 7],
            [2, 5, 8],
            [0, 4, 8],
            [2, 4, 6],
        ]
        for pos in win_possibilities:
            is_win = len({self.game_field[pos[0]], self.game_field[pos[1]], self.game_field[pos[2]]}) == 1
            if is_win:
                return True
        return False
