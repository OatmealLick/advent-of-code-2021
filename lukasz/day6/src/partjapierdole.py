import os
import sys
from collections import defaultdict

PARENT_FISH_INITIAL_LIFE = 6
CHILD_FISH_INITIAL_LIFE = 8


def simulate_day(fish):
    new_fish = defaultdict(lambda: 0)
    for key in fish.keys():
        fish_value = fish[key]
        if key > 0:
            new_fish[key - 1] += fish_value
        else:
            new_fish[8] += fish_value
            new_fish[6] += fish_value
    return new_fish


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        fish_list = [int(timer) for timer in f.readline().split(",")]

    fish_dict = defaultdict(lambda: 0)
    days = 256
    for fish in fish_list:
        fish_dict[fish] += 1
    print(fish_dict)
    for _ in range(days):
        fish_dict = simulate_day(fish_dict)
        print(fish_dict)
    total = sum(fish_dict.values())
    print(total)


if __name__ == "__main__":
    main()
