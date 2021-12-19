from collections import defaultdict


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        # to sie nazywa input
        crab_positions = [int(pos) for pos in f.readline().split(",")]
    crabs = defaultdict(lambda: 0)
    for pos in crab_positions:
        crabs[pos] += 1
    crab_middles = defaultdict(lambda: 0)
    max_crab_pos = max(crabs.keys())
    min_crab_pos = min(crabs.keys())
    for pos in range(min_crab_pos, max_crab_pos + 1):
        for crab_pos, crab_count in crabs.items():
            crab_middles[pos] += abs(crab_pos - pos) * crab_count

    print(crab_middles)
    list_crab_middles = [(k,v) for k, v in crab_middles.items()]
    list_crab_middles.sort(key=lambda c: c[1])
    print(list_crab_middles)
    print(list_crab_middles[0][1])

if __name__ == "__main__":
    main()
