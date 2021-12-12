from collections import Counter
from collections import defaultdict
def calculate_cost_of_alignment(crabs):
    crabs_counter = Counter(crabs)
    fuel_consumption = defaultdict(int)
    for x in range(max(crabs_counter.keys())):
        for key, value in crabs_counter.items():
            fuel_consumption[x] += triangular_number(abs(key - x)) * value
    print(min(fuel_consumption.values()))
    pass

def triangular_number(number):
    return number * (number + 1) // 2

if __name__ == "__main__":
    with open("input.txt") as f:
        crabs = [int(n) for n in f.read().split(",")]
        calculate_cost_of_alignment(crabs)
