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


def is_vertical_or_horizontal(line):
    return line[0].x == line[1].x or line[0].y == line[1].y


def get_points_in_line(line):
    points = []
    if line[0].x == line[1].x:
        smaller = min(line[0].y, line[1].y)
        higher = max(line[0].y, line[1].y)
        for i in range(smaller, higher + 1):
            points.append(Point(line[0].x, i))
    else:
        smaller = min(line[0].x, line[1].x)
        higher = max(line[0].x, line[1].x)
        for i in range(smaller, higher + 1):
            points.append(Point(i, line[0].y))
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
    # dude, how come a filter version looks like shit in this language :(
    # lines_filtered = list(filter(lambda l: is_vertical_or_horizontal(l), lines))
    lines_filtered = [l for l in lines if is_vertical_or_horizontal(l)]
    points_in_lines = [get_points_in_line(l) for l in lines_filtered]
    for points in points_in_lines:
        add_points_to_board(points, board)
    counter = count_occurrences(board)
    print(counter)


if __name__ == "__main__":
    main()
