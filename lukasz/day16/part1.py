def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        line = f.read()
    print(f"hex {line}")
    raw_binary = bin(int(line, 16))
    print(f"raw binary {raw_binary}")
    binary = raw_binary[2:].zfill(len(line * 4))
    current = 0
    print(f"len {len(binary)} binary {binary}")
    version_sum, _ = analyze_packet(binary, current)
    print(f"Version sum {version_sum}")


def analyze_packet(binary, start):
    current = start
    print(f"Starting from {current}, {binary[current:]}")
    version = int(binary[current:current + 3], 2)
    version_sum = version
    type_id = int(binary[current + 3:current + 6], 2)
    current += 6
    print(f"Analyzing version {version}, type_id {type_id}")
    if type_id == 4:
        print(f"Literal")
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
        print(f"Read num {number_decimal}")
    else:
        length_type_id = binary[current]
        current += 1
        if length_type_id == '0':
            print(f"Operator: known total bits")
            total_bits = int(binary[current:current + 15], 2)
            current += 15
            bits = binary[current:current + total_bits]
            print(f"Bits {bits}")
            subpackets_bits = 0
            while subpackets_bits < total_bits:
                version, length = analyze_packet(binary, current)
                version_sum += version
                subpackets_bits += length
                current += length

        elif length_type_id == '1':
            print(f"Operator: known total subpackets")
            subpackets = int(binary[current:current + 11], 2)
            current += 11
            for _ in range(subpackets):
                version, length = analyze_packet(binary, current)
                version_sum += version
                current += length
        else:
            raise Exception("lel")
    return version_sum, current - start


if __name__ == "__main__":
    main()
