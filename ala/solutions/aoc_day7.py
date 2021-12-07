from math import fabs, inf
from typing import List

from tqdm import tqdm

from ala.solutions.utils import read_one_line_int


class CheapestPositionFinder:
    def __init__(self, crab_positions: List[int]):
        self.crab_positions = crab_positions

    def calc_minimum_fuel_usage(self) -> int:
        cheapest_destination = self.find_cheapest_destination()
        fuel_usage = self.calc_fuel_usage(cheapest_destination)
        return fuel_usage

    def find_cheapest_destination(self) -> int:
        cheapest_destination = 0
        minimum_fuel_usage = +inf
        for crab_pos in tqdm(range(max(self.crab_positions))):
            fuel_usage = self.calc_fuel_usage(crab_pos)
            if fuel_usage < minimum_fuel_usage:
                minimum_fuel_usage = fuel_usage
                cheapest_destination = crab_pos

        print(f'Cheapest destination: {cheapest_destination}')
        return cheapest_destination

    def calc_fuel_usage(self, destination: int) -> int:
        fuel_usage = 0
        for crab_pos in self.crab_positions:
            fuel_usage += sum(range(int(fabs(crab_pos - destination)) + 1))
        return fuel_usage


if __name__ == '__main__':
    input_path = '../inputs/aoc_day7.txt'
    crab_positions = read_one_line_int(input_path)

    cpf = CheapestPositionFinder(crab_positions)
    print(cpf.calc_minimum_fuel_usage())
