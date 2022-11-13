import copy
from enum import Enum
from typing import Optional


class FieldState(Enum):
    X = "X"
    O = "O"


EMPTY = None
boardType = list[list[Optional[FieldState]]]


def print_board(board: boardType):
    print(f"""
    {'#' if board[0][0] is None else board[0][0].value} | {'#' if board[0][1] is None else board[0][1].value} | {'#' if board[0][2] is None else board[0][2].value}
    --------- 
    {'#' if board[1][0] is None else board[1][0].value} | {'#' if board[1][1] is None else board[1][1].value} | {'#' if board[1][2] is None else board[1][2].value}
    ---------
    {'#' if board[2][0] is None else board[2][0].value} | {'#' if board[2][1] is None else board[2][1].value} | {'#' if board[2][2] is None else board[2][2].value}
    
    """)


def get_init_board():
    return [[FieldState.X, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def next_player(board):
    x = 0
    o = 0
    for row in board:
        x += row.count(FieldState.X)
        o += row.count(FieldState.O)
    return FieldState.X if x == o else FieldState.O


def possible_moves(board):
    moves = set()

    for i_row, row in enumerate(board):
        for i_col, col in enumerate(row):
            if col == EMPTY:
                moves.add((i_row, i_col))
    return moves


def do_move(board, move):
    r = copy.deepcopy(board)
    r[move[0]][move[1]] = next_player(board)
    return r


def check_for_winner(board):
    posibilities = [
        [[0, 0], [1, 0], [2, 0]],
        [[0, 1], [1, 1], [2, 1]],
        [[0, 2], [1, 2], [2, 2]],
        [[0, 0], [0, 1], [0, 2]],
        [[1, 0], [1, 1], [1, 2]],
        [[2, 0], [2, 1], [2, 2]],
        [[0, 0], [1, 1], [2, 2]],
        [[2, 0], [1, 1], [0, 2]]]

    for pos in posibilities:
        r = []
        for cord in pos:
            field = board[cord[1]][cord[0]]
            if field == EMPTY:
                break
            else:
                r.append(field)
        if r.count(FieldState.X) == 3 or r.count(FieldState.O) == 3:
            return r[0]
    return None


def check_game_over(board):
    if check_for_winner(board) is not None or (
            not any(EMPTY in sublist for sublist in board) and check_for_winner(board) is None):
        return True
    else:
        return False


def get_finished_game_value(board):
    if check_for_winner(board) == FieldState.X:
        return 1
    elif check_for_winner(board) == FieldState.O:
        return -1
    else:
        return 0


def minimax(board):
    if check_game_over(board):
        return None
    else:
        if next_player(board) == FieldState.X:
            value, move = max_value(board)
            return move
        else:
            value, move = min_value(board)
            return move


def max_value(board):
    if check_game_over(board):
        return get_finished_game_value(board), None

    v = float('-inf')
    move = None
    for pos_move in possible_moves(board):
        value, m = min_value(do_move(board, pos_move))
        if value < v:
            v = value
            move = pos_move
            if v == -1:
                return v, move

    return v, move


def min_value(board):
    if check_game_over(board):
        return get_finished_game_value(board), None

    v = float('inf')
    move = None
    for pos_move in possible_moves(board):
        value, m = max_value(do_move(board, pos_move))
        if value < v:
            v = value
            move = pos_move
            if v == -1:
                return v, move

    return v, move
