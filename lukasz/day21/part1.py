from collections import defaultdict, namedtuple


def get_next_roll(die):
    assert die < 101
    if die < 98:
        return 3 * die + 3, die + 3
    elif die == 98:
        return 98 + 99 + 100, 1
    elif die == 99:
        return 99 + 100 + 1, 2
    elif die == 100:
        return 100 + 1 + 2, 3

def get_single_roll(die):
    return (die % 100) + 1

def position_after_roll(start, roll):
    return ((start + roll - 1) % 10) + 1

def play_game(p1, p2, p1score, p2score, p1Turn, die):
    pass

def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        p1 = int(f.readline()[-2])
        p2 = int(f.readline()[-1])
    print(p1, p2)
    die = 1
    p1Turn = True
    print(position_after_roll(7, 5))
    print(position_after_roll(7, 6))
    p1score = 0
    p2score = 0
    count = 0
    # print("single for 99" + get_single_roll(99))
    # print("single for 100" + get_single_roll(100))
    while p1score < 1000 and p2score < 1000:
        print(f"Count {count}, die {die}, p1 {p1} with score {p1score}, p2 {p2} {p2score}")
        roll, die = get_next_roll(die)
        if p1Turn:
            p1 = position_after_roll(p1, roll)
            p1score += p1
        else:
            p2 = position_after_roll(p2, roll)
            p2score += p2
        p1Turn = not p1Turn
        count += 3
    losing = min(p1score, p2score)
    print(f"Count {count}")
    print(f"Losing {losing}")
    print(count * losing)


if __name__ == "__main__":
    main()
