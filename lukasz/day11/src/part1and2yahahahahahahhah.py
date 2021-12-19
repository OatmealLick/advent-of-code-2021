import os
import sys


def neighbours(y, x, lines):
    neighbours = []
    height = len(lines)
    width = len(lines[0])
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i != 0 or j != 0:
                new_x = x + i
                new_y = y + j
                if within_bounds(new_x, new_y, width, height):
                    neighbours.append((new_y, new_x))
    return neighbours


def within_bounds(x, y, width, height):
    return 0 <= x < width and 0 <= y < height


def simulate_step(rows):
    flash_count = 0
    height = len(rows)
    width = len(rows[0])
    flashy = []
    for i in range(height):
        for j in range(width):
            octo = rows[i][j]
            octo = min(octo + 1, 10)
            if octo > 9 and (i, j) not in flashy:
                flashy.append((i, j))
            rows[i][j] = octo
    flash_count += len(flashy)
    for f in flashy:
        to_search = [f]
        while to_search:
            current = to_search.pop()
            for n in neighbours(current[0], current[1], rows):
                n_octo = rows[n[0]][n[1]]
                if n_octo < 10:
                    n_octo += 1
                    if n_octo == 10 and n not in to_search:
                        to_search.append(n)
                        flash_count += 1
                    rows[n[0]][n[1]] = n_octo

    for i in range(height):
        for j in range(width):
            octo = rows[i][j]
            if octo == 10:
                rows[i][j] = 0
    return rows, flash_count


def print_rows(rows):
    for row in rows:
        print(row)
    print()


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    rows = []
    for l in lines:
        col = []
        for c in l:
            col.append(int(c))
        rows.append(col)
    steps = 10000
    size = len(rows) * len(rows[0])
    for step in range(steps):
        rows, new_flashes = simulate_step(rows)
        if new_flashes == size:
            print(f"That {step + 1}")
            break


if __name__ == "__main__":
    main()
