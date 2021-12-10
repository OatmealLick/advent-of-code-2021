import os
import sys


def simulate_day(lanternfish):
    new_lanternfish = []
    for fish in lanternfish:
        new_fish = fish - 1
        if new_fish >= 0:
            new_lanternfish.append(new_fish)
        else:
            new_lanternfish.append(6)
            new_lanternfish.append(8)
    return new_lanternfish


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        # to sie nazywa input
        fish = [int(timer) for timer in f.readline().split(",")]
    days = 80
    for i in range(days):
        fish = simulate_day(fish)
    print(len(fish))


if __name__ == "__main__":
    main()
