import os
import sys


def fuck_this_input_read_board(f):
    board = []
    for i in range(5):
        board.append([int(num.strip()) for num in f.readline().replace("  ", " ").strip().split(" ")])
    return board


def fuck_this_input_skip_line(f):
    f.readline()


def check_board_if_won(board, nums):
    for i in range(5):
        if check_if_all_items_in_nums(board[i], nums):
            return True
    for i in range(5):
        column = []
        for j in range(5):
            column.append(board[j][i])
        if check_if_all_items_in_nums(column, nums):
            return True
    return False


def check_if_all_items_in_nums(items, nums):
    return all([item in nums for item in items])


def get_all_unmarked(board, nums):
    board_nums = [item for row in board for item in row]
    return [board_num for board_num in board_nums if board_num not in nums]


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        moves = [int(move) for move in f.readline().split(",")]
        boards = []
        while f.readline() != "DUPA":  # TO HAK ALI NIE MÓJ :)
            boards.append(fuck_this_input_read_board(f))
    boards_already_won = []
    for i in range(1, len(moves)):
        sub_moves = moves[:i]
        for board_num in range(len(boards)):
            if board_num not in boards_already_won:
                board = boards[board_num]
                result = check_board_if_won(board, sub_moves)
                if result:
                    boards_already_won.append(board_num)
                    if len(boards_already_won) == len(boards):
                        unmarked = get_all_unmarked(board, sub_moves)
                        final_result = sum(unmarked) * sub_moves[-1]
                        print(f"Final result {final_result}, last num {sub_moves[-1]}")


if __name__ == "__main__":
    main()
