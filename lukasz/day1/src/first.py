import os
import sys

def main():
    with open("first-input.txt", "r") as input:
        measurements = [int(x) for x in input.readlines()]
        # current = -1
        increased = 0
        for i in range(3, len(measurements)):

            previous_measurement = measurements[i-3]
            current_measurement = measurements[i]
            if current_measurement > previous_measurement:
                increased += 1
        print(increased)



if __name__ == "__main__":
    main()