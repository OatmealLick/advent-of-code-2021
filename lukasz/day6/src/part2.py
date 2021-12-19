import os
import sys

PARENT_FISH_INITIAL_LIFE = 6
CHILD_FISH_INITIAL_LIFE = 8


class DayFish:
    def __init__(self, day, fish):
        self.day = day
        self.fish = fish

    def __eq__(self, o: object) -> bool:
        return self.day == o.day and self.fish == o.fish

    def __str__(self) -> str:
        return f"(day: {self.day}, fish: {self.fish})"

    def __repr__(self) -> str:
        return str(self)

    def __hash__(self) -> int:
        return self.day * 31 + self.fish


def simulate_days(day: int, fish: int, cache: dict):
    for d in range(1, day):
        for f in range(fish):
            day_fish = DayFish(d, f)
            print(f"DF: {day_fish}")
            if day_fish not in cache:
                new_f = simulate_day(cache.get(DayFish(d - 1, f), [1]))
                cache[DayFish(d, f)] = new_f
    return cache

def simulate_day(initial_fish):
    new_fish = []
    for fish in initial_fish:
        if fish - 1 >= 0:
            new_fish.append(fish - 1)
        else:
            new_fish.append(PARENT_FISH_INITIAL_LIFE)
            new_fish.append(CHILD_FISH_INITIAL_LIFE)
    return new_fish

def main():
    # filename = "input.txt"
    filename = "input-sample.txt"
    with open(filename, "r") as f:
        fish = [int(timer) for timer in f.readline().split(",")]

    days = 256
    cache = {}

    cache = simulate_days(days, CHILD_FISH_INITIAL_LIFE, cache)
    print(cache)


if __name__ == "__main__":
    main()
