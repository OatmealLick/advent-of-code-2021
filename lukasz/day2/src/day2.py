import os
import sys

def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    horizontal = 0
    depth = 0
    aim = 0
    with open(filename, "r") as f:
        lines = f.readlines()
    for line in lines:
        parts = line.split(" ")
        command = parts[0]
        number = int(parts[1])
        if command == "up":
            # depth -= number
            aim -= number
        elif command == "down":
            # depth += number
            aim += number
        elif command == "forward":
            horizontal += number
            depth += aim * number
    print(horizontal * depth)


if __name__ == "__main__":
    main()
