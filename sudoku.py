#############################################################
# FILE : sudoku.py
# WRITER : sagikel
# DESCRIPTION : Backtracking.
#############################################################

import math
import copy

# *** PART 1 *** #


def solve_sudoku(board):
    """The function return True if there is a solution to the sudoku. First
    it's check if n = 0 or the sudoku is full. After that it use another
    function to do backtracking and recursion for solving this problem."""
    n = len(board)
    if board == [[]]:  # n = 0 [[]]
        return True
    zero_cells = where_is_zero(board, n)
    if not zero_cells:  # full sudoku or n = 0 []
        return True
    n_square_root = int(math.sqrt(n))
    all_cells = squares_to_list(n_square_root)
    answer = solve_sudoku_helper(board, n, zero_cells[0], zero_cells, all_cells)
    return answer


def where_is_zero(board, n):
    """The function return list of all the places(list of tuples) where we can
    find zero in the sudoku."""
    result = []
    for row in range(n):
        for column in range(n):
            if board[row][column] == 0:
                result.append((row, column))
    return result


def squares_to_list(n):
    """The function return list of lists that have tuples of places for any
    square in the sudoku."""
    list_of_squares = []
    range_list = [0]
    range_list += range(n, n * n, n)
    for a in range_list:
        for b in range_list:
            new_list = []
            for c in range(0, n):
                for d in range(0, n):
                    new_list.append((a+c, b+d))
            list_of_squares.append(new_list)
    return list_of_squares


def solve_sudoku_helper(board, n, cell, zero_cells, all_cells,
                        counter=0, possible_number=10):
    """This part doing the backtracking. At the start it's doing checks and if
    it end well it will add the possible_number and continue to the next zero
    cell. If we find solution it will return True. If not - False. """
    for num in range(n):  # row check
        if board[cell[0]][num] == possible_number:
            return False
    for num in range(n):   # column check
        if board[num][cell[1]] == possible_number:
            return False
    if not square_check(board, cell, all_cells,
                        possible_number):  # square check
        return False
    if len(zero_cells) == counter:  # len check
        board[cell[0]][cell[1]] = possible_number
        return True
    if counter:
        board[cell[0]][cell[1]] = possible_number
    for number in range(1, n+1):
        if not solve_sudoku_helper(board, n, zero_cells[counter], zero_cells,
                                   all_cells, counter+1, number):
            continue
        else:
            return True
    board[cell[0]][cell[1]] = 0  # return the 0 if the process filed.
    return False


def square_check(board, cell, all_cells, possible_number):
    """The function return False if it find a possible_number in the square
    that match to the cell in the arguments. If not, it will return True as the
    test succeed."""
    for i in all_cells:
        if cell in i:
            for g in i:
                if board[g[0]][g[1]] == possible_number:
                    return False
    return True


# *** PART 2 *** #


def print_k_subsets(n, k):
    """Prints all subgroups that are at size k for the group {0, ..., 1-n}."""
    if k <= n:
        print_k_subsets_helper(n, k, [], 0)


def print_k_subsets_helper(n, k, possible_list, index):
    """The function uses backtracking and if it reaches the limit of k, it
    prints the possible list."""
    if len(possible_list) == k:
        print(possible_list)
        return
    if n == index:
        return
    possible_list.append(index)
    print_k_subsets_helper(n, k, possible_list, index + 1)
    possible_list.pop()
    print_k_subsets_helper(n, k, possible_list, index+1)


def fill_k_subsets(n, k, lst):
    """Insert to the lst all subgroups that are at size k for the
    group {0, ..., 1-n}."""
    if k <= n:
        fill_k_subsets_helper(n, k, lst, [], 0)


def fill_k_subsets_helper(n, k, lst, possible_list, index):
    """The function uses backtracking and if it reaches the limit of k, it
    append a deep copy of the possible list."""
    if len(possible_list) == k:
        lst.append(copy.deepcopy(possible_list))
        return
    if n == index:
        return
    possible_list.append(index)
    fill_k_subsets_helper(n, k, lst, possible_list, index + 1)
    possible_list.pop()
    fill_k_subsets_helper(n, k, lst, possible_list, index + 1)


def return_k_subsets(n, k):
    """Returns a list of lists. Each list will have exactly k different organs
    from the group {0, ..., 1-n}."""
    all_possible_list = return_k_subsets_helper(n, k)
    correct_list = copy.deepcopy(all_possible_list)
    for i in all_possible_list:
        for j in range(0, k-1):
            if i[j] >= i[j+1]:
                correct_list.remove(i)
                break
    return correct_list


def return_k_subsets_helper(n, k, index=0):
    """The function returns all the existing options of a K-length list without
    the order of appearance of the numbers in n"""
    list_of_lists = []
    if k == index:
        return [[]]
    for j in range(n):
        one_option_list = return_k_subsets_helper(n, k, index + 1)
        for lst in one_option_list:
            lst.append(j)
        list_of_lists += one_option_list
    return list_of_lists

