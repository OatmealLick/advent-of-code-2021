from typing import List

from ala.solutions.utils import read_str_input


class PowerMeter:
    def __init__(self, measurements: List[str]):
        self.measurements = [measurement.replace('\n', '') for measurement in measurements]

    def get_power(self):
        zeros, ones = self.get_zeros_and_ones(self.measurements)
        gamma, epsilon = self.get_gamma_and_epsilon(self.measurements, zeros, ones)
        return gamma * epsilon

    def get_zeros_and_ones(self, measurements):
        zeros = [0] * len(measurements[0])
        ones = [0] * len(measurements[0])

        for measurement in measurements:
            for index in range(len(measurements[0])):
                if measurement[index] == '0':
                    zeros[index] += 1
                else:
                    ones[index] += 1

        return zeros, ones

    def get_gamma_and_epsilon(self, measurements, zeros, ones):
        gamma = ''
        delta = ''
        for index in range(len(measurements[0])):
            if zeros[index] > ones[index]:
                gamma += '0'
                delta += '1'
            else:
                gamma += '1'
                delta += '0'

        gamma = int(gamma, 2)
        delta = int(delta, 2)

        return gamma, delta

    def get_life_support_rating(self):
        oxygen_generator_rating = self.measurements
        CO2_scrubber_rating = self.measurements

        zeros_o, ones_o = self.get_zeros_and_ones(self.measurements)
        zeros_c, ones_c = self.get_zeros_and_ones(self.measurements)

        for index in range(len(self.measurements[0])):
            bit_criteria = '1' if ones_o[index] >= zeros_o[index] else '0'
            if len(oxygen_generator_rating) > 1:
                oxygen_generator_rating = [ogr for ogr in oxygen_generator_rating if ogr[index] == bit_criteria]
                zeros_o, ones_o = self.get_zeros_and_ones(oxygen_generator_rating)

            bit_criteria = '1' if ones_c[index] >= zeros_c[index] else '0'
            if len(CO2_scrubber_rating) > 1:
                CO2_scrubber_rating = [csr for csr in CO2_scrubber_rating if csr[index] != bit_criteria]
                zeros_c, ones_c = self.get_zeros_and_ones(CO2_scrubber_rating)

        return int(oxygen_generator_rating[0], 2) * int(CO2_scrubber_rating[0], 2)


if __name__ == '__main__':
    input_path = '../inputs/aoc_day3.txt'
    instructions = read_str_input(input_path)

    position_finder = PowerMeter(instructions)
    print(position_finder.get_power())
    print(position_finder.get_life_support_rating())
