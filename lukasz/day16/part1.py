def main():
    # filename = "input.txt"
    filename = "input-sample.txt"
    with open(filename, "r") as f:
        line = f.read()
    print(f"hex {line}")
    raw_binary = bin(int(line, 16))
    print(f"raw binary {raw_binary}")
    binary = raw_binary[2:].zfill(len(line * 4))
    current = 0
    version_sum = 0
    print(f"len {len(binary)} binary {binary}")
    while current < len(binary):
        current, version = analyze_packet(binary, current)
        print(f"Current {current}, version {version}")
        version_sum += version
    print(version_sum)


def analyze_packet(binary, start, version_sum=0):
    current = start
    print(f"Starting from {current}, {binary[current:]}")
    version = int(binary[current:current + 3], 2)
    version_sum += version
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
        print(f"Operator: Length type id {length_type_id}")
        if length_type_id == '0':
            total_bits = int(binary[current:current + 15], 2)
            current += 15
            bits = binary[current:current + total_bits]
            print(f"Bits {bits}")
            current += total_bits
        elif length_type_id == '1':
            subpackets = int(binary[current:current + 11], 2)
            current += 11
            bits = binary[current:current + subpackets * 11]
            print(f"Bits {bits}")
            current += subpackets * 11
        else:
            raise Exception("lel")
    current += 4 - (current % 4)
    return version_sum, current - start


if __name__ == "__main__":
    main()
