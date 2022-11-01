from typing import List

board = [
    "......................",
    "......##########......",
    "......#........#......",
    "......#........#......",
    "......#........#####..",
    "....###............#..",
    "....#............###..",
    "....##############....",
]

def flood_fill(input_board: List[str], old: str, new: str, x: int, y: int) -> List[str]:
    row_len = len(input_board)
    col_len = len(input_board[0])
    found_boundary = False
    if input_board[x][y] == "#":
        return input_board

    for i in range(0, x):
        if input_board[i][y] == "#":
            found_boundary = True
            break
    if not found_boundary:
        return input_board
    found_boundary = False
    for i in range(x, row_len):
        if input_board[i][y] == "#":
            found_boundary = True
            break
    if not found_boundary:
        return input_board
    found_boundary = False
    for i in range(y, col_len):
        if input_board[x][i] == "#":
            found_boundary = True
            break
    if not found_boundary:
        return input_board
    found_boundary = False
    for i in range(0, y):
        if input_board[x][i] == "#":
            found_boundary = True
            break
    if not found_boundary:
        return input_board
    output_board = []
    for i in range(0,row_len):
        j = 0
        start = 0
        end = 0
        while(j < col_len):
            while(j < col_len and board[i][j] == "#"):
                start = j
                j = j + 1
            if start != 0:
                break
            j = j + 1
        j = j + 1
        while(j < col_len):
            if board[i][j] == "#":
                end = j
                break
            j = j + 1
        
        if start == 0 or end == 0:
            output_board.append(input_board[i])
        else:
            new_str = input_board[i][:start+1] + (end-start-1) * new + input_board[i][end:]
            output_board.append(new_str)
    return output_board


modified_board = flood_fill(input_board=board, old=".", new="~", x=5, y=12)

for a in modified_board:
    print(a)
