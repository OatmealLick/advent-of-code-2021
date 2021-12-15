class Day11:

    def __init__(self, energy_levels):
        self.energy_levels = energy_levels
        self.rows_len = len(energy_levels)
        self.columns_len = len(energy_levels[0])
        self.flashes = 0
        self.cycle_flashes = 0

    def cycle(self):

        for y, row in enumerate(self.energy_levels):
            for x, level in enumerate(row):
                self.charge_octopus(y, x)
        cycle_flashes = 0
        for y, row in enumerate(self.energy_levels):
            for x, level in enumerate(row):
                if self.energy_levels[y][x] > 9:
                    self.energy_levels[y][x] = 0
                    cycle_flashes += 1
        self.flashes += cycle_flashes
        return cycle_flashes

    def part1(self, amount):
        for i in range(amount):
            self.cycle()
        print(self.flashes)

    def charge_octopus(self, row, column):
        if 0 <= row <= self.rows_len - 1 and 0 <= column <= self.columns_len - 1:
            self.energy_levels[row][column] += 1
            if self.energy_levels[row][column] == 10:
                self.discharge(column, row)

    def discharge(self, column, row):
        # energy_levels[row][column] = 0
        self.charge_octopus(row + 1, column + 1)
        self.charge_octopus(row, column + 1)
        self.charge_octopus(row - 1, column + 1)
        self.charge_octopus(row + 1, column)
        self.charge_octopus(row + 1, column - 1)
        self.charge_octopus(row, column - 1)
        self.charge_octopus(row - 1, column - 1)
        self.charge_octopus(row - 1, column)

    def part2(self):
        i = 1
        while self.cycle() != 100:
            i += 1
        print("Simultaneous flashes on:", i)


if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.read().splitlines()
        _energy_levels = [[int(n) for n in line] for line in lines]
        _energy_levels_temp = [i.copy() for i in _energy_levels]
        x = Day11(_energy_levels)
        y = Day11(_energy_levels_temp)
        x.part1(100)
        y.part2()
