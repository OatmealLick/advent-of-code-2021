import time
from heapq import heappush, heappop
from math import inf
from typing import Tuple

import numpy as np

from ala.solutions.utils import read_map, read_resized_map


class Node:
    def __init__(self, coords: Tuple[int, int], risk_f: int = +inf):
        self.coords = coords
        self.risk_f = risk_f

    def h(self, end_coords: Tuple[int, int]):
        return end_coords[0] - self.coords[0] + end_coords[1] - self.coords[1]

    def __eq__(self, other):
        return self.coords == other.coords

    def __hash__(self):
        return self.coords[0] ** self.coords[1]

    def __lt__(self, other):
        return self.risk_f < other.risk_f

    def __repr__(self):
        return f'{self.coords}, {self.risk_f}'


class LowestRiskPathFinder:
    def __init__(self, map_: np.array):
        self.map_ = map_
        self.risk_map_g = np.zeros(map_.shape) + +inf
        self.end_coords = self.map_.shape[0] - 1, self.map_.shape[1] - 1

    def find_the_lowest_risk(self):
        return self.find_the_lowest_path()

    @staticmethod
    def sum_risks(came_from, current_node):
        risk = current_node.risk_f
        while current_node in came_from.keys():
            current_node = came_from[current_node]
            risk += current_node.risk_f
        return risk

    def find_the_lowest_path(self):
        opens = []
        came_from = {}

        current_node = Node((0, 0))
        current_node.risk_f = current_node.h(self.end_coords)
        self.risk_map_g[0, 0] = 0

        heappush(opens, current_node)

        while opens:
            current_node = heappop(opens)
            c_coords = current_node.coords

            if current_node.coords == self.end_coords:
                # return self.sum_risks(came_from, current_node)
                return current_node.risk_f

            for diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                s_coords = (c_coords[0] + diff[0], c_coords[1] + diff[1])
                if s_coords[0] in range(self.map_.shape[0]) and s_coords[1] in range(self.map_.shape[1]):
                    successor = Node(s_coords)
                    s_risk = self.risk_map_g[c_coords] + self.map_[s_coords]
                    if s_risk < self.risk_map_g[s_coords]:
                        came_from[successor] = current_node
                        self.risk_map_g[s_coords] = s_risk
                        successor.risk_f = s_risk + successor.h(self.end_coords)
                        if successor not in opens:
                            heappush(opens, successor)


if __name__ == '__main__':
    input_path = '../inputs/aoc_day15.txt'
    map_ = read_map(input_path)
    map_ = read_resized_map(map_, 5)

    start = time.time()
    lrpf = LowestRiskPathFinder(map_)
    print(lrpf.find_the_lowest_risk())
    print(f'Time: {time.time() - start}')
