import os
import sys


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return self.x + 31 * self.y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)


def i_do_not_fancy_this_input_read_lines(input_lines):
    lines = []
    for input_line in input_lines:
        parts = input_line.split(" -> ")
        coords0 = [int(part.strip()) for part in parts[0].split(",")]
        coords1 = [int(part.strip()) for part in parts[1].split(",")]
        lines.append((Point(coords0[0], coords0[1]), Point(coords1[0], coords1[1])))
    return lines


def get_points_in_line(line):
    if line[0].x == line[1].x:
        return get_points_vertical(line)
    elif line[0].y == line[1].y:
        return get_points_horizontal(line)
    else:
        return get_points_diagonal(line)


def get_points_vertical(line):
    points = []
    smaller = min(line[0].y, line[1].y)
    higher = max(line[0].y, line[1].y)
    for i in range(smaller, higher + 1):
        points.append(Point(line[0].x, i))
    return points


def get_points_horizontal(line):
    points = []
    smaller = min(line[0].x, line[1].x)
    higher = max(line[0].x, line[1].x)
    for i in range(smaller, higher + 1):
        points.append(Point(i, line[0].y))
    return points


def get_points_diagonal(line):
    points = []
    x_offset = 1 if line[0].x < line[1].x else -1
    y_offset = 1 if line[0].y < line[1].y else -1
    current = line[0]
    end = line[1]
    points.append(current)
    while current != end:
        next_current = Point(current.x + x_offset, current.y + y_offset)
        points.append(next_current)
        current = next_current
    return points


def add_points_to_board(points, board):
    for p in points:
        current = board.get(p, 0)
        board[p] = current + 1


def count_occurrences(board):
    counter = 0
    for count in board.values():
        if count > 1:
            counter += 1
    return counter


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    board = {}
    with open(filename, "r") as f:
        input_lines = f.readlines()
    lines = i_do_not_fancy_this_input_read_lines(input_lines)
    points_in_lines = [get_points_in_line(l) for l in lines]
    for points in points_in_lines:
        add_points_to_board(points, board)
    counter = count_occurrences(board)
    print(counter)


if __name__ == "__main__":
    main()
