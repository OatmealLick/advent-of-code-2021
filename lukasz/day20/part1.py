from collections import defaultdict, namedtuple

Pair = namedtuple('Pair', ['y', 'x'])


def neighbours_as_binary(pair, board, step, image_start, image_end):
    if pair.y < image_start - 2 or pair.y > image_end + 2 or pair.x < image_start - 2 or pair.x > image_end + 2:
        if step % 2 == 0:
            return "000000000"
        else:
            return "111111111"

    ns = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if Pair(pair.y + i, pair.x + j) in board:
                ns.append("1")
            else:
                ns.append("0")

    return "".join(ns)


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    # 5349
    with open(filename, "r") as f:
        line = f.readline().strip()
        f.readline()
        lines = [l.strip() for l in f.readlines()]

    size = len(lines[0])
    print(f"Line len {len(line)}")
    values_dict = {}
    for i, c in enumerate(list(line)):
        if c == '#':
            values_dict[i] = 1

    board = {}
    for row, line in enumerate(list(lines)):
        for col, char in enumerate(list(line)):
            if char == '#':
                board[Pair(row, col)] = 1

    # print(values_dict)
    # print(board)
    # print(f"Size {size}")
    image_start = 0
    image_end = size
    # offset = 10
    board_first = -60
    board_last = size + 60
    steps = 50
    # print_board(board, board_first, board_last)
    for s in range(steps):
        new_board = {}
        print(f"Step {s}")
        for row in range(board_first, board_last):
            for col in range(board_first, board_last):
                p = Pair(row, col)
                binary = neighbours_as_binary(p, board, s, image_start, image_end)
                int1 = int(binary, 2)
                # print(f"For p {p} bin is {binary} and num {int1}")
                if int1 in values_dict:
                    # print(f"Lighting {p} with bin {binary}")
                    new_board[p] = 1
        board = new_board
        # board = {k: v for k, v in board.items() if k.x != board_first and k.y != board_first}
        image_start -= 1
        image_end += 1
        # print_board(board, board_first, board_last)

    print(len(board.keys()))


def print_board(board, start, end):
    for row in range(start, end):
        line = []
        for col in range(start, end):
            if Pair(row, col) in board:
                line.append('#')
            else:
                line.append('.')
        print("".join(line))


if __name__ == "__main__":
    main()
