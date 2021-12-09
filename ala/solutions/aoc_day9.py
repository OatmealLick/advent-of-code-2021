from itertools import product

import numpy as np

from ala.solutions.utils import read_map


class RiskFinder:
    def __init__(self, risk_map: np.ndarray):
        self.risk_map = np.pad(risk_map, 1, 'constant', constant_values=9)
        self.check_array = np.zeros(self.risk_map.shape)

    def find_risk_level(self):
        valleys_sum = 0
        x_positions, y_positions = self.risk_map.shape
        for x, y in product(range(1, x_positions), range(1, y_positions)):
            context = self.risk_map[x - 1:x + 2, y - 1:y + 2]
            if len(np.unique(context)) > 1 and np.min(context) == self.risk_map[x, y]:
                valleys_sum += self.risk_map[x, y] + 1
        return valleys_sum

    def get_basins_sizes(self):
        x_positions, y_positions = self.risk_map.shape
        basins_sizes = []
        for x, y in product(range(1, x_positions), range(1, y_positions)):
            context = self.risk_map[x - 1:x + 2, y - 1:y + 2]
            if len(np.unique(context)) > 1 and np.min(context) == self.risk_map[x, y]:
                basin_size = self._get_basin_size(x, y)
                basins_sizes.append(basin_size)

        basins_sizes.sort()
        return basins_sizes[-1]*basins_sizes[-2]*basins_sizes[-3]

    def _get_basin_size(self, x: int, y: int):
        if self.check_array[x, y]:
            return 0

        if x * y < 0:
            return 0

        if x + 1 > self.risk_map.shape[0] or y + 1 > self.risk_map.shape[1]:
            return 0

        self.check_array[x, y] = True

        if self.risk_map[x, y] == 9:
            return 0

        return 1 + self._get_basin_size(x + 1, y) \
               + self._get_basin_size(x - 1, y) \
               + self._get_basin_size(x, y + 1) \
               + self._get_basin_size(x, y - 1)


if __name__ == '__main__':
    input_path = '../inputs/aoc_day9.txt'
    risk_map = read_map(input_path)

    rf = RiskFinder(risk_map)
    print(rf.find_risk_level())
    print(rf.get_basins_sizes())
