from itertools import product

import numpy as np

from ala.solutions.utils import read_map


class OctopusesEnergyController:
    def __init__(self, octopuses: np.ndarray):
        self.octopuses = octopuses
        self.flashed_octopuses = np.zeros(self.octopuses.shape)
        self.flashes = 0

    def find_first_big_flash(self) -> int:
        step = 1
        while 1:
            self.update_octopuses(product(range(self.octopuses.shape[0]), range(self.octopuses.shape[1])))
            if np.sum(self.flashed_octopuses) == np.sum(np.ones(self.octopuses.shape)):
                return step
            self.flashed_octopuses = np.zeros(self.octopuses.shape)
            step += 1

    def calc_flashes(self, steps_number: int) -> int:
        for _ in range(steps_number):
            self.update_octopuses(product(range(self.octopuses.shape[0]), range(self.octopuses.shape[1])))
            self.flashed_octopuses = np.zeros(self.octopuses.shape)
        return self.flashes

    def update_octopuses(self, coords_to_update):
        for x, y in coords_to_update:
            if x in range(self.octopuses.shape[0]) and y in range(self.octopuses.shape[1]):
                if self.octopuses[x, y] < 9:
                    if not self.flashed_octopuses[x, y]:
                        self.octopuses[x, y] += 1
                else:
                    self.flash(x, y)

    def flash(self, x, y):
        if x in range(self.octopuses.shape[0]) and y in range(self.octopuses.shape[1]):
            pass

        if self.flashed_octopuses[x, y]:
            pass

        self.octopuses[x, y] = 0
        self.flashed_octopuses[x, y] = True
        self.flashes += 1

        coords_to_update = product(range(x - 1, x + 2), range(y - 1, y + 2))
        self.update_octopuses(coords_to_update)


if __name__ == '__main__':
    input_path = '../inputs/aoc_day11.txt'
    octopuses = read_map(input_path)

    oec = OctopusesEnergyController(octopuses)
    # print(oec.calc_flashes(100))
    print(oec.find_first_big_flash())
