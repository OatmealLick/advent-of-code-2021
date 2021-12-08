def decode(v, decoded_dict):
    # print(f"Decoding: {v}, having {decoded_dict}")
    v_len = len(v)

    # these bitches we know for certain
    if v_len == 2:
        return 1
    if v_len == 3:
        return 7
    if v_len == 4:
        return 4
    if v_len == 7:
        return 8

    # now deduce the rest based on those we already know
    if v_len == 6:  # possibly 0, 6, 9
        if custom_in(decoded_dict[4], v):
            return 9
        elif custom_in(decoded_dict[1], v):
            return 0
        else:
            return 6

    if v_len == 5:  # possibly 2, 3, 5  https://www.youtube.com/watch?v=ek_ln3xecnw
        if 1 in decoded_dict and custom_in(decoded_dict[1], v):
            return 3
        else:
            if custom_diff(decoded_dict[4], v) == 1:
                return 5
            else:
                return 2


def custom_in(smaller, bigger):
    return custom_diff(smaller, bigger) == 0


def custom_diff(one, two):
    diff = 0
    for char in one:
        if char not in two:
            diff += 1
    return diff


def custom_sort_key(v):
    v_len = len(v)
    if v_len in [2, 3, 4, 8]:
        return 0
    elif v_len == 6:
        return 1
    else:
        return 2


def main():
    filename = "input.txt"
    # filename = "input-samplest-of-them-all.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        lines = [line.strip() for line in f.readlines()]

    total = 0
    for line in lines:
        parts = [part.strip() for part in line.split("|")]
        train_values = ["".join(sorted(value.strip())) for value in parts[0].split(" ")]
        test_values = ["".join(sorted(value.strip())) for value in parts[1].split(" ")]

        train_values.sort(key=custom_sort_key)

        decoded_dict = {}
        for v in train_values:
            decoded = decode(v, decoded_dict)
            decoded_dict[decoded] = v

        num = []
        print(f"For line {line} and {decoded_dict}")
        for v in test_values:
            decoded = decode(v, decoded_dict)
            num.append(str(decoded))
        num_as_num = int("".join(num))
        total += num_as_num
        print(f"Got {num_as_num}")
    print(f"Total {total}")


if __name__ == "__main__":
    main()
