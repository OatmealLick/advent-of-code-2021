
def part1(levels):
    for row in levels:
        for level in row:

    pass
def part2(lines):
    pass

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.read().splitlines()
        energy_levels = [[n for n in line] for line in lines]
        part1(energy_levels)
        part2(lines)



