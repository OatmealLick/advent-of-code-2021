from typing import List, Tuple

import numpy as np

from ala.solutions.utils import read_lines_coords


class LinesFinder:
    def __init__(self, points: List[Tuple[Tuple[int, int], Tuple[int, int]]]):
        self.points = points

    def find_intersection_points(self):
        x_max, y_max = self.find_frames()
        diagram = np.zeros((x_max, y_max))

        for start, end in self.points:
            start_x, start_y = start
            end_x, end_y = end

            if start_x == end_x:
                y = sorted([start_y, end_y])
                start_y, end_y = y
                for y in range(start_y, end_y + 1):
                    diagram[start_x, y] += 1

            elif start_y == end_y:
                x = sorted([start_x, end_x])
                start_x, end_x = x
                for x in range(start_x, end_x + 1):
                    diagram[x, start_y] += 1

            else:
                if start_x > end_x:
                    range_x = range(start_x, end_x - 1, -1)
                else:
                    range_x = range(start_x, end_x + 1)

                if start_y > end_y:
                    range_y = range(start_y, end_y - 1, -1)
                else:
                    range_y = range(start_y, end_y + 1)

                for x, y in zip(range_x, range_y):
                    diagram[x, y] += 1

        diagram = np.where(diagram > 1)

        return len(diagram[0])

    def find_intersection_points_ver_hor(self):
        x_max, y_max = self.find_frames()
        diagram = np.zeros((x_max, y_max))

        for start, end in self.points:
            start_x, start_y = start
            end_x, end_y = end

            if start_x == end_x:
                y = sorted([start_y, end_y])
                start_y, end_y = y
                for y in range(start_y, end_y + 1):
                    diagram[start_x, y] += 1

            elif start_y == end_y:
                x = sorted([start_x, end_x])
                start_x, end_x = x
                for x in range(start_x, end_x + 1):
                    diagram[x, start_y] += 1

        diagram = np.where(diagram > 1)

        return len(diagram[0])

    def find_frames(self):
        x_max, y_max = 0, 0
        for start, end in self.points:
            x_max = max(x_max, start[0], end[0])
            y_max = max(y_max, start[1], end[1])
        return x_max + 1, y_max + 1


if __name__ == '__main__':
    input_path = '../inputs/aoc_day5.txt'
    lines_coords = read_lines_coords(input_path)

    lf = LinesFinder(lines_coords)
    print(lf.find_intersection_points())
