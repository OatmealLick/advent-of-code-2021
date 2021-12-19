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
    for d in range(0, day + 1, 8):
        for f in range(fish):
            day_fish = DayFish(d, f)
            print(day_fish)
            if day_fish not in cache:
                new_f = simulate_8_days(cache.get(DayFish(d - 8, f), [f]))
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

def simulate_8_days(initial_fish, days=8):
    new_fish = []
    for fish in initial_fish:
        if fish - days >= 0:
            new_fish.append(fish - days)
        else:
            leftover = fish - days + 1
            if abs(leftover) > PARENT_FISH_INITIAL_LIFE:
                new_fish.append(PARENT_FISH_INITIAL_LIFE)
                new_fish.append(CHILD_FISH_INITIAL_LIFE)
            else:
                new_fish.append(PARENT_FISH_INITIAL_LIFE + leftover)
            new_fish.append(CHILD_FISH_INITIAL_LIFE + leftover)
    return new_fish

def main():
    # filename = "input.txt"
    filename = "input-sample.txt"
    with open(filename, "r") as f:
        fish = [int(timer) for timer in f.readline().split(",")]

    days = 80
    cache = {}

    cache = simulate_days(days, CHILD_FISH_INITIAL_LIFE, cache)
    total = 0
    for f in fish:
        i = len(cache[DayFish(days, f)])
        print(i)
        total += i
    print(total)


if __name__ == "__main__":
    main()
