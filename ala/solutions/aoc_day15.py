import time
from typing import Tuple

import numpy as np

from ala.solutions.utils import read_map


class LowestRiskPathFinder:
    def __init__(self, map: np.array):
        self.map = map
        self.risk_map = np.zeros(map.shape)

    def find_the_lowest_risk(self):
        return self.find_the_lowest_path((self.map.shape[0] - 1, self.map.shape[1] - 1))

    # def find_the_lowest_path(self, dst: Tuple[int, int]):
    #     if dst == (0, 0):
    #         return 0
    #     if dst[0] == 0:
    #         self.risk_map[dst] = sum(self.map[0, 1:dst[1] + 1])
    #     if dst[1] == 0:
    #         self.risk_map[dst] = sum(self.map[1:dst[0] + 1, 0])
    #
    #     if self.risk_map[dst] == 0:
    #         self.risk_map[dst] = min(self.find_the_lowest_path((dst[0] - 1, dst[1])),
    #                                  self.find_the_lowest_path((dst[0], dst[1] - 1))) + self.map[dst]
    #     return self.risk_map[dst]

    def find_the_lowest_path(self, dst: Tuple[int, int]):
        print(dst)
        time.sleep(0.1)
        if dst[0] < 0 or dst[1] < 0 or dst[0] + 1 > self.map.shape[0] or dst[1] + 1 > self.map.shape[1]:
            return 0

        if dst == (0, 0):
            return 0

        if dst in [(0, 1), (1, 0)]:
            self.risk_map[dst] = self.map[dst]
            return self.map[dst]

        if not self.risk_map[dst]:
            if dst[0] == 0:
                self.risk_map[dst] = min(self.find_the_lowest_path((dst[0], dst[1] - 1)),
                                         self.find_the_lowest_path((dst[0] + 1, dst[1])),
                                         self.find_the_lowest_path((dst[0], dst[1] + 1))) + self.map[dst]
            elif dst[1] == 0:
                self.risk_map[dst] = min(self.find_the_lowest_path((dst[0] - 1, dst[1])),
                                         self.find_the_lowest_path((dst[0] + 1, dst[1])),
                                         self.find_the_lowest_path((dst[0], dst[1] + 1))) + self.map[dst]

            else:
                self.risk_map[dst] = min(self.find_the_lowest_path((dst[0] - 1, dst[1])),
                                         self.find_the_lowest_path((dst[0], dst[1] - 1)),
                                         self.find_the_lowest_path((dst[0] + 1, dst[1])),
                                         self.find_the_lowest_path((dst[0], dst[1] + 1))) + self.map[dst]
        return self.risk_map[dst]


if __name__ == '__main__':
    input_path = '../inputs/test_aoc_day15.txt'
    map = read_map(input_path)

    lrpf = LowestRiskPathFinder(map)
    print(lrpf.find_the_lowest_risk())
    print()
