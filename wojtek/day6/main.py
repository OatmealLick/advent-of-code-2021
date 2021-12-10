def count_fishes_after_days(days):
    for i in range(days):
        # print("Day ", i, end="")
        # print([value for key, value in sorted(d.items())])
        for key, item in sorted(d.items(), reverse=True):
            if key == 0:
                d[6] = d[6] + item
                d[8] = item
            elif key > 0:
                d[key - 1] = item

    print(sum(d.values()))
if __name__ == "__main__":
    with open("input.txt") as f:
        lanternfishes = [int(n) for n in f.read().split(",")]
        d = {i: lanternfishes.count(i) for i in range(9)} #a moze queue ?
        count_fishes_after_days(256)