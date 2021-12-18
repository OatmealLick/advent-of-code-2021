from heapq import heappush, heappop
from typing import Tuple

import numpy as np

from ala.solutions.utils import read_map, read_resized_map


class Node:
    def __init__(self, coords: Tuple[int, int], risk_f: int):
        self.coords = coords
        self.risk_f = risk_f

    def __eq__(self, other):
        return self.coords == other.coords

    def __lt__(self, other):
        return self.risk_f < other.risk_f

    def __repr__(self):
        return f'{self.coords}, {self.risk_f}'


class LowestRiskPathFinder:
    def __init__(self, map_: np.array):
        self.map_ = map_
        self.risk_map_g = np.zeros(map_.shape)
        self.risk_map_h = np.zeros(map_.shape)
        self.build_risk_map_h((0, 0), (self.map_.shape[0] - 1, self.map_.shape[1] - 1))

    def find_the_lowest_risk(self):
        return self.find_the_lowest_path()

    def build_risk_map_h(self, src: Tuple[int, int], dst: Tuple[int, int]):
        if dst == src:
            return 0
        if dst[0] == 0:
            self.risk_map_h[dst] = sum(self.map_[src[0], 1:dst[1] + 1])
        if dst[1] == 0:
            self.risk_map_h[dst] = sum(self.map_[1:dst[0] + 1, src[1]])

        if self.risk_map_h[dst] == 0:
            self.risk_map_h[dst] = min(self.build_risk_map_h(src, (dst[0] - 1, dst[1])),
                                       self.build_risk_map_h(src, (dst[0], dst[1] - 1))) + self.map_[dst]
        return self.risk_map_h[dst]

    def find_the_lowest_path(self):
        opens = []
        closes = []

        current_node = Node((0, 0), 0)
        heappush(opens, current_node)

        while opens:
            current_node = heappop(opens)
            c_coords = current_node.coords

            if c_coords == (self.map_.shape[0] - 1, self.map_.shape[1] - 1):
                return self.risk_map_g[c_coords]

            for diff in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                s_coords = (c_coords[0] + diff[0], c_coords[1] + diff[1])
                if s_coords[0] in range(self.map_.shape[0]) and s_coords[1] in range(self.map_.shape[1]):
                    successor = Node(s_coords, 0)
                    if successor not in closes and successor not in opens:
                        successor.risk_f = self.risk_map_g[c_coords] + self.risk_map_h[s_coords]
                        self.risk_map_g[s_coords] = self.risk_map_g[c_coords] + self.map_[s_coords]
                        heappush(opens, successor)
                    else:
                        if self.risk_map_g[s_coords] > self.risk_map_g[c_coords] + self.map_[s_coords]:
                            self.risk_map_g[s_coords] = self.risk_map_g[c_coords] + self.map_[s_coords]

                            if successor in closes:
                                successor = [succ for succ in closes if succ == successor][0]
                                closes.remove(successor)
                                heappush(opens, successor)

            closes.append(current_node)


if __name__ == '__main__':
    input_path = '../inputs/aoc_day15.txt'
    map_ = read_map(input_path)
    map_ = read_resized_map(map_, 5)

    lrpf = LowestRiskPathFinder(map_)
    print(lrpf.find_the_lowest_risk())
