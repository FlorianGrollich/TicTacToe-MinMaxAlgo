from enum import Enum


class FieldState(Enum):
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
        self.game_field: list[FieldState] = [
            FieldState.N, FieldState.N, FieldState.N,
            FieldState.N, FieldState.N, FieldState.N,
            FieldState.N, FieldState.N, FieldState.N]

        self.round: int = 1

    def print_game_field(self):
        print(f"""
        {self.game_field[0].value} | {self.game_field[1].value} | {self.game_field[2].value}
        ---------
        {self.game_field[3].value} | {self.game_field[4].value} | {self.game_field[5].value}
        --------- 
        {self.game_field[6].value} | {self.game_field[7].value} | {self.game_field[8].value}
        """)

    def next_move(self, index: int) -> None:
        next_player = FieldState.X if self.round % 2 == 0 else FieldState.O

        if self.game_field[index] == FieldState.N:
            self.game_field[index] = next_player
            self.round += 1
        else:
            raise Exception("There is already a player on that field")

    def get_possible_moves(self) -> list[int]:
        result = []
        for i, field in enumerate(self.game_field):
            if field == FieldState.N:
                result.append(i)
        return result

    def check_for_win(self) -> int:
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
                if self.game_field[pos[0]] == FieldState.X:
                    return 1
                elif self.game_field[pos[0]] == FieldState.O:
                    return -1
        return 0


