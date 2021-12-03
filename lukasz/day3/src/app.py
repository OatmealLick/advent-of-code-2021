import os
import sys


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    gold_pieces = find_me_the_riches_son(lines.copy(), finding_most_common=True)
    silver_pieces = find_me_the_riches_son(lines.copy(), finding_most_common=False)
    gold = int("".join(gold_pieces), 2)
    silver = int("".join(silver_pieces), 2)
    print(gold * silver)


def find_me_the_riches_son(nums: list, finding_most_common: bool):
    num_length = len(nums[0])
    for i in range(num_length):
        print(nums)
        zero_starting = []
        one_starting = []
        for line in nums:
            if line[i] == "1":
                one_starting.append(line)
            else:
                zero_starting.append(line)
        if finding_most_common:
            nums = one_starting if len(one_starting) >= len(zero_starting) else zero_starting
        else:
            nums = zero_starting if len(zero_starting) <= len(one_starting) else one_starting
        if len(nums) < 2:
            break
    return nums


if __name__ == "__main__":
    main()
