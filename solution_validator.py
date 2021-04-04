# returns a unidimentional list with values of a 3x3 block
def get_block(board: list, block_id: int) -> list:
    block = [board[x + 3 * (block_id // 3)][y + 3 * (block_id % 3)]
             for x in range(3) for y in range(3)]

    return block


def valid_solution(board: list) -> bool:

    for line_idx, line in enumerate(board):
        if 0 in line:
            return False
        if len(set(line)) != 9:
            return False
        if len(set([board[column][line_idx] for column in range(9)])) != 9:
            return False

    for block_id in range(9):
        if len(set(get_block(board, block_id))) != 9:
            return False

    return True


# print(valid_solution([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]]))  # =>True

# print(valid_solution([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 0, 3, 4, 8],
#     [1, 0, 0, 3, 4, 2, 5, 6, 0],
#     [8, 5, 9, 7, 6, 1, 0, 2, 0],
#     [4, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 0, 1, 5, 3, 7, 2, 1, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 0, 0, 4, 8, 1, 1, 7, 9]]))  # =>False

# print(valid_solution([
#     [5, 3, 4, 6, 7, 8, 9, 1, 2],
#     [6, 7, 2, 1, 9, 5, 3, 4, 8],
#     [1, 9, 8, 3, 4, 2, 5, 6, 7],
#     [8, 5, 9, 7, 6, 1, 4, 2, 3],
#     [1, 2, 6, 8, 5, 3, 7, 9, 1],
#     [7, 1, 3, 9, 2, 4, 8, 5, 6],
#     [9, 6, 1, 5, 3, 7, 2, 8, 4],
#     [2, 8, 7, 4, 1, 9, 6, 3, 5],
#     [3, 4, 5, 2, 8, 6, 1, 7, 9]]))  # =>False
