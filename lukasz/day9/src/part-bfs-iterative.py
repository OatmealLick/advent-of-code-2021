def is_higher(row_high, col_high, row_low, col_low, height, width, map):
    return not is_within_bounds(row_high, col_high, height, width) or \
           int(map[row_high][col_high]) > int(map[row_low][col_low])


def is_proper_neighbour(row, col, height, width, parent_row, parent_col, lines):
    return is_within_bounds(row, col, height, width) and \
           int(lines[row][col]) != 9 and \
           int(lines[row][col]) > int(lines[parent_row][parent_col])


def is_within_bounds(row, col, height, width):
    return 0 <= row < height and 0 <= col < width


def find_basin(row, col, height, width, lines):
    basin = [(row, col)]
    visited = []

    while basin:
        current = basin.pop()
        visited.append(current)
        row = current[0]
        col = current[1]
        for n in [(row - 1, col), (row + 1, col), (row, col - 1), (row, col + 1)]:
            if is_proper_neighbour(n[0], n[1], height, width, row, col, lines):
                if n not in visited:
                    basin.append(n)
    # TODO fix this
    # ye, ye definitely, gonna do that. Soon™
    return set(visited)


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    basin_sizes = []
    height = len(lines)
    width = len(lines[0])
    for row in range(len(lines)):
        for col in range(len(lines[row])):
            if is_higher(row - 1, col, row, col, height, width, lines) and \
                    is_higher(row + 1, col, row, col, height, width, lines) and \
                    is_higher(row, col - 1, row, col, height, width, lines) and \
                    is_higher(row, col + 1, row, col, height, width, lines):
                basin = find_basin(row, col, height, width, lines)
                if len(basin_sizes) >= 3:
                    lowest = min(basin_sizes)
                    if len(basin) > lowest:
                        basin_sizes.remove(lowest)
                        basin_sizes.append(len(basin))
                else:
                    basin_sizes.append(len(basin))

                print(f"For [{row},{col}] len {len(basin)}, set len {len(set(basin))} got {basin}")
    print(basin_sizes)
    print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])


if __name__ == "__main__":
    main()
