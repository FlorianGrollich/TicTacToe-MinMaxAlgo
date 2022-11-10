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
        self._game_field: list[FieldState] = [
            FieldState.N, FieldState.N, FieldState.N,
            FieldState.N, FieldState.N, FieldState.N,
            FieldState.N, FieldState.N, FieldState.N]

        self.round: int = 1

    def print_game_field(self):
        print(f"""
        {self._game_field[0].value} | {self._game_field[1].value} | {self._game_field[2].value}
        ---------
        {self._game_field[3].value} | {self._game_field[4].value} | {self._game_field[5].value}
        --------- 
        {self._game_field[6].value} | {self._game_field[7].value} | {self._game_field[8].value}
        """)

    def next_move(self, index: int) -> list[FieldState]:
        next_player = FieldState.X if self.round % 2 == 0 else FieldState.O

        if self._game_field[index] == FieldState.N:
            field = self._game_field.copy()
            field[index] = next_player
            return field
        else:
            raise Exception("There is already a player on that field")

    def make_next_move(self, move: int):
        self._game_field = self.next_move(move)
        self.round += 1

    def get_possible_moves(self) -> list[int]:
        result = []
        for i, field in enumerate(self._game_field):
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
            is_win = len({self._game_field[pos[0]], self._game_field[pos[1]], self._game_field[pos[2]]}) == 1
            if is_win:
                if self._game_field[pos[0]] == FieldState.X:
                    return 1
                elif self._game_field[pos[0]] == FieldState.O:
                    return -1
        return 0
