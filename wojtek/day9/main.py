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


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = [[int(c) for c in line] for line in f.read().splitlines()]
        risk_levels = 0
        for row, line in enumerate(lines):
            for column, height in enumerate(line):
                if check_if_low_point(lines, row, column, height):
                    risk_levels += height + 1
                    print(risk_levels, row, column, height)

        print(risk_levels)
