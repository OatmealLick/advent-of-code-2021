import math


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        line = f.read()
    raw_binary = bin(int(line, 16))
    binary = raw_binary[2:].zfill(len(line * 4))
    current = 0
    print(f"len {len(binary)} binary {binary}")
    output, _ = analyze_packet(binary, current)
    print(f"Output {output}")


def analyze_packet(binary, start):
    current = start
    print(f"Starting from {current}, {binary[current:]}")
    version = int(binary[current:current + 3], 2)
    type_id = int(binary[current + 3:current + 6], 2)
    current += 6
    print(f"Analyzing version {version}, type_id {type_id}")
    if type_id == 4:
        number = ""
        while True:
            is_is_last = binary[current] == '0'
            current += 1
            part = binary[current:current + 4]
            number += part
            current += 4
            if is_is_last:
                break
        number_decimal = int(number, 2)
        print(f"Literal num {number_decimal}")
        return number_decimal, current - start
    elif type_id == 0:  # sum
        current, results = read_results(binary, current)
        return sum(results), current - start
    elif type_id == 1:  # product
        current, results = read_results(binary, current)
        return math.prod(results), current - start
    elif type_id == 2:  # min
        current, results = read_results(binary, current)
        return min(results), current - start
    elif type_id == 3:  # max
        current, results = read_results(binary, current)
        return max(results), current - start
    elif type_id == 5:  # greater than
        current, results = read_results(binary, current)
        return 1 if results[0] > results[1] else 0, current - start
    elif type_id == 6:  # lower than
        current, results = read_results(binary, current)
        return 1 if results[0] < results[1] else 0, current - start
    elif type_id == 7:  # equal
        current, results = read_results(binary, current)
        return 1 if results[0] == results[1] else 0, current - start
    else:
        raise Exception("nononono")


def read_results(binary, current):
    length_type_id = binary[current]
    current += 1
    results = []
    if length_type_id == '0':
        total_bits = int(binary[current:current + 15], 2)
        current += 15
        subpackets_bits = 0
        while subpackets_bits < total_bits:
            result, length = analyze_packet(binary, current)
            results.append(result)
            subpackets_bits += length
            current += length
    elif length_type_id == '1':
        subpackets = int(binary[current:current + 11], 2)
        current += 11
        for _ in range(subpackets):
            result, length = analyze_packet(binary, current)
            results.append(result)
            current += length
    else:
        raise Exception("lel")
    return current, results


if __name__ == "__main__":
    main()
