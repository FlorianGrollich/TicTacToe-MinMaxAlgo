from tic_tac_toe_game import *

board = get_init_board()

print("""
Indexes for Board:
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
""")

index_to_move = {
    0: (0, 0),
    1: (0, 1),
    2: (0, 2),
    3: (1, 0),
    4: (1, 1),
    5: (1, 2),
    6: (2, 0),
    7: (2, 1),
    8: (2, 2),
}

for i in range(9):
    index = int(input("Where do you wanna place your X?(0-9)\n"))
    board = do_move(board, index_to_move[index])
    if check_game_over(board):
        break
    print("computer thinks...")
    move = minimax(board)
    board = do_move(board, move)
    print_board(board)
    if check_game_over(board):
        break

print_board(board)
