from solution_validator import get_block, valid_solution
from time import sleep


def print_grid(board: list):
    for line in board:
        print(line, flush=True)


def map_pos(board: list, pos: tuple) -> tuple:

    # create a list with the valid values of the row specified by pos
    row = [number for number in board[pos[0]] if number]

    # create a list with the valid values of the column specified by pos
    column = [board[x][pos[1]] for x in range(len(board))]

    # create list with the valid values for the block specified by pos
    block_id = pos[0]//3 * 3 + pos[1]//3
    block = get_block(board, block_id)

    # create dictionaries with number of occurrences
    row_map = {num: num in row for num in range(1, 10)}
    column_map = {num: num in column for num in range(1, 10)}
    block_map = {num: num in block for num in range(1, 10)}

    return row_map, column_map, block_map


# returns intersection of missing values in the row, column and block dictionaries
def intersect(row: dict, column: dict, block: dict) -> list:
    return [num for num in range(1, 10) if not any(
        [row[num], column[num], block[num]])]


def find_missing(board: list) -> tuple:
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i, j)
    return None


def solve_sudoku(board: list, show_steps=False) -> bool:
    global steps
    steps += 1

    # find index of cell with value 0
    pos = find_missing(board)

    # there are no cells missing a value, solution was found
    if not pos:
        return True

    # creates dictionaries with value ocurrences
    row, column, block = map_pos(board, pos)
    # intersects all the dictionaries to get possible answers to that block
    candidates = intersect(row, column, block)

    # no possible candidates for current cell
    if not len(candidates):
        return False
    else:
        # loop over all the candidates for the current cell
        for attempt in candidates:
            board[pos[0]][pos[1]] = attempt
            # some code to allow visualization of the algorithm. Can be commented/removed
            if show_steps:
                print("\nattempting:", attempt, "at pos:", pos)
                print_grid(board)
                sleep(0.001)
            # recursive call with updated cell
            if (solve_sudoku(board, show_steps=show_steps)):
                return True

    # attemps where unsuccessful, reset cell
    board[pos[0]][pos[1]] = 0
    return False


def main(board: list):
    print("Inital board: ")
    print_grid(board)

    if(solve_sudoku(board, show_steps=False)):
        print("\nFound solution:")
        print_grid(board)
        print("\nSolution is valid:", valid_solution(board))
        print(f"Total steps taken: {steps}")

    else:
        print("\nGiven board is unsolvable")


if __name__ == '__main__':
    # testing boards
    # board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
    #          [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #          [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #          [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #          [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #          [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # board = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
    #          [5, 2, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 8, 7, 0, 0, 0, 0, 3, 1],
    #          [0, 0, 3, 0, 1, 0, 0, 8, 0],
    #          [9, 0, 0, 8, 6, 3, 0, 0, 5],
    #          [0, 5, 0, 0, 9, 0, 6, 0, 0],
    #          [1, 3, 0, 0, 0, 0, 2, 5, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 7, 4],
    #          [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    # board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # board = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 5, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0],
    #          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

    # Extra hard board --- better approach on better_console_solver.py 
    board = [[7, 0, 0, 1, 0, 8, 0, 0, 0],
             [0, 9, 0, 0, 0, 0, 0, 3, 2],
             [0, 0, 0, 0, 0, 5, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 1, 0, 0],
             [9, 6, 0, 0, 2, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 8, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 5, 0, 0, 1, 0, 0, 0],
             [3, 2, 0, 0, 0, 0, 0, 0, 6]]

    global rec_depth, steps
    rec_depth = steps = 0

    main(board)
