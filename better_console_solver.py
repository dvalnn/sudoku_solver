from time import sleep
from math import sqrt
from collections import namedtuple
import argparse
import solution_validator as sl


class Sudoku:
    def __init__(self, grid):
        # steps counter
        self.steps = 0
        # size of the game board
        self.square_size = 9
        # size of a subdivision in the board
        self.block_size = int(sqrt(self.square_size))
        # initialize the board as a 2d array of 0
        self.board = [[0 for row in range(self.square_size)] for col in range(self.square_size)]
        self.count_missing = self.square_size ** 2
        # initialize the lists of empty sets for each row, col and block of the map
        self.row_has_num = [set() for row in range(self.square_size)]
        self.column_has_num = [set() for col in range(self.square_size)]
        self.block_has_num = [[set() for col in range(self.block_size)] for row in range(self.block_size)]

        # initialize a namedtuple to pass to pos arguments
        Pos = namedtuple("Pos", ["row", "col"])

        # loop over given grid initializing the game board and checking if its valid
        for row in range(self.square_size):
            for col in range(self.square_size):
                if self.check(grid[row][col], Pos(row, col)):
                    self.place(grid[row][col], Pos(row, col))
                else:
                    raise ValueError(f"Invalid board at position{Pos(row, col)}")

    def check(self, value, Pos):
        return not any(
            [
                value in self.row_has_num[Pos.row],
                value in self.column_has_num[Pos.col],
                value in self.block_has_num[Pos.row // self.block_size][Pos.col // self.block_size],
            ]
        )

    def place(self, value, Pos):
        self.board[Pos.row][Pos.col] = value
        if value:
            self.count_missing -= 1
            self.row_has_num[Pos.row].add(value)
            self.column_has_num[Pos.col].add(value)
            self.block_has_num[Pos.row // self.block_size][Pos.col // self.block_size].add(value)

    def remove(self, Pos):
        if self.board[Pos.row][Pos.col]:
            self.row_has_num[Pos.row].remove(self.board[Pos.row][Pos.col])
            self.column_has_num[Pos.col].remove(self.board[Pos.row][Pos.col])
            self.block_has_num[Pos.row // self.block_size][Pos.col // self.block_size].remove(
                self.board[Pos.row][Pos.col]
            )
            self.board[Pos.row][Pos.col] = 0
            self.count_missing += 1
        else:
            raise ValueError(f"Removing nonexistent value at {Pos}")

    def solve(self):
        #every time solve is called counts a step
        self.steps += 1
        #no missing values in the board, 
        if not self.count_missing:
            return True
        #init namedtuple Pos
        Pos = namedtuple("Pos", ["row", "col"])

        min_pos = Pos(0, 0)
        #creates a set with all possible numeric choices for a cell
        possibilities = set(range(1, self.square_size + 1))
        min_candidates = possibilities.copy()

        #iterate over the board looking for empy squares
        for row in range(self.square_size):
            for col in range(self.square_size):
                #if the cell value is not 0, skip it
                if self.board[row][col]:
                    continue
                #calculates possible candidates for given cell by checking the union of the sets for the row, column and block
                #and then subtracting it to the set of all possible choices
                candidates = self.row_has_num[row].union(self.column_has_num[col])
                candidates = candidates.union(self.block_has_num[row // self.block_size][col // self.block_size])
                candidates = possibilities.difference(candidates)
                
                if len(candidates) < len(min_candidates):
                    min_candidates = candidates.copy()
                    min_pos = Pos(row, col)

        #iterate over candidate numbers for min_pos
        for attempt in min_candidates:
            self.place(attempt, min_pos)
            if self.solve():
                return True
            else:
                self.remove(min_pos)

        return False

    def get_steps(self):
        return self.steps

    def __repr__(self):
        return "[" + "\n".join(str(self.board[i]) for i in range(self.square_size)) + "]"


def main(board: list):

    sudoku = Sudoku(board)

    print("Inital board: ")
    print(sudoku)

    if sudoku.solve():
        print("\nSolution found: ")
        print(sudoku)
        print(f"\nSteps taken: {sudoku.get_steps()}")
    else:
        print("\nBoard is unsolvable.")


if __name__ == "__main__":

    # testing boards
    board1 = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]

    board2 = [
        [3, 0, 6, 5, 0, 8, 4, 0, 0],
        [5, 2, 0, 0, 0, 0, 0, 0, 0],
        [0, 8, 7, 0, 0, 0, 0, 3, 1],
        [0, 0, 3, 0, 1, 0, 0, 8, 0],
        [9, 0, 0, 8, 6, 3, 0, 0, 5],
        [0, 5, 0, 0, 9, 0, 6, 0, 0],
        [1, 3, 0, 0, 0, 0, 2, 5, 0],
        [0, 0, 0, 0, 0, 0, 0, 7, 4],
        [0, 0, 5, 2, 0, 6, 3, 0, 0],
    ]

    board3 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
    ]

    board4 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 4, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0, 0],
    ]

    board5 = [
        [7, 0, 0, 1, 0, 8, 0, 0, 0],
        [0, 9, 0, 0, 0, 0, 0, 3, 2],
        [0, 0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0],
        [9, 6, 0, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 1, 0, 0, 0],
        [3, 2, 0, 0, 0, 0, 0, 0, 6],
    ]

    GAME_BOARDS = {1: board1, 2: board2, 3: board3, 4: board4, 5: board5}

    ap = argparse.ArgumentParser()
    ap.add_argument(
        "-s",
        "--showSteps",
        type=bool,
        required=False,
        default=False,
        help="add delay and print out each step taken to solve the board --NOT IMPLEMENTED--",
    )
    ap.add_argument(
        "-b",
        "--board",
        type=int,
        required=False,
        default=5,
        help=f"select which board to solve from the available {len(GAME_BOARDS)} boards",
    )
    args = vars(ap.parse_args())

    global rec_depth, steps
    rec_depth = steps = 0

    main(GAME_BOARDS[args["board"]])