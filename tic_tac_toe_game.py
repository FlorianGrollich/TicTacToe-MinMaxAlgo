from enum import Enum


class FieldState(Enum):
    X = "X"
    O = "O"
    N = "#"  # nothing --> empty field

    #   INDEX for playing field
    #   0 | 1 | 2
    #   ---------
    #   3 | 4 | 5
    #   ---------
    #   6 | 7 | 8


game_field: list[FieldState] = [

    FieldState.N, FieldState.N, FieldState.N,
    FieldState.N, FieldState.N, FieldState.N,
    FieldState.N, FieldState.N, FieldState.N]

round: int = 1


def print_game_field():
    print(f"""
    {game_field[0].value} | {game_field[1].value} | {game_field[2].value}
    ---------
    {game_field[3].value} | {game_field[4].value} | {game_field[5].value}
    --------- 
    {game_field[6].value} | {game_field[7].value} | {game_field[8].value}
    """)


def next_move(index: int) -> list[FieldState]:
    next_player = FieldState.X if round % 2 == 0 else FieldState.O

    if game_field[index] == FieldState.N:
        field = game_field.copy()
        field[index] = next_player
        return field
    else:
        raise Exception("There is already a player on that field")


def get_possible_moves() -> list[int]:
    result = []
    for i, field in enumerate(game_field):
        if field == FieldState.N:
            result.append(i)
    return result


def check_for_win(board) -> int:
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
        is_win = len({board[pos[0]], board[pos[1]], board[pos[2]]}) == 1
        if is_win:
            if board[pos[0]] == FieldState.X:
                return 1
            elif board[pos[0]] == FieldState.O:
                return -1
    return 0


def calculate_score(move: int):
    new_board = next_move(move)
    is_win = check_for_win(new_board)
    if is_win != 0:
        return is_win
