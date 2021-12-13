import math


def check_if_low_point(heighmap, row, column, height):
    rows = len(heighmap)
    columns = len(heighmap[0])

    if column != 0 and height >= heighmap[row][column - 1]:
        return 0
    if row != 0 and height >= heighmap[row - 1][column]:
        return 0
    if column != columns - 1 and height >= heighmap[row][column + 1]:
        return 0
    if row != rows - 1 and height >= heighmap[row + 1][column]:
        return 0
    return 1


def calculate_basin(heighmap, row, column, height):
    rows = len(heighmap)
    columns = len(heighmap[0])
    basin_map = [[0 for i in range(columns)] for x in range(rows)]
    basin = 0

    return next_basin_point(basin, basin_map, column, columns, heighmap, row, rows)


def next_basin_point(basin, basin_map, column, columns, heighmap, row, rows):
    basin_map[row][column] = 1
    basin += 1
    if column != 0 and heighmap[row][column - 1] != 9 and basin_map[row][column - 1] != 1:  # left
        basin = next_basin_point(basin, basin_map, column - 1, columns, heighmap, row, rows)

    if row != 0 and heighmap[row - 1][column] != 9 and basin_map[row - 1][column] != 1:  # up
        basin = next_basin_point(basin, basin_map, column, columns, heighmap, row - 1, rows)

    if column != columns - 1 and heighmap[row][column + 1] != 9 and basin_map[row][column + 1] != 1:  # right
        basin = next_basin_point(basin, basin_map, column + 1, columns, heighmap, row, rows)

    if row != rows - 1 and heighmap[row + 1][column] != 9 and basin_map[row + 1][column] != 1:  # down
        basin = next_basin_point(basin, basin_map, column, columns, heighmap, row + 1, rows)

    return basin


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = [[int(c) for c in line] for line in f.read().splitlines()]
        risk_levels = 0
        basins = []
        for row, line in enumerate(lines):
            for column, height in enumerate(line):
                if check_if_low_point(lines, row, column, height):
                    risk_levels += height + 1
                    basins.append(calculate_basin(lines, row, column, height))

        # print(risk_levels)
        print(math.prod(sorted(basins)[-3:]))
