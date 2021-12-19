def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    risks = 0
    height = len(lines)
    width = len(lines[0])
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if is_higher(row - 1, col, row, col, height, width, lines) and \
                    is_higher(row + 1, col, row, col, height, width, lines) and \
                    is_higher(row, col - 1, row, col, height, width, lines) and \
                    is_higher(row, col + 1, row, col, height, width, lines):
                num = int(lines[row][col]) + 1
                print(f"For [{row},{col}] got {num}")
                risks += num
    print(risks)


def is_higher(row_high, col_high, row_low, col_low, height, width, map):
    return not is_within_bounds(row_high, col_high, height, width) or \
           int(map[row_high][col_high]) > int(map[row_low][col_low])


def is_within_bounds(row, col, height, width):
    return 0 <= row < height and 0 <= col < width


if __name__ == "__main__":
    main()
