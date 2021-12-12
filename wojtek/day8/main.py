from collections import Counter


def crack_code(code):

    display = {}
    numbers = {}
    ctr = Counter(code)

    for key, value in ctr.items():
        if value in (9, 6, 4):
            if value == 9:
                display[4] = key
            if value == 6:
                display[3] = key
            if value == 4:
                display[7] = key

    for word in [''.join(sorted(x)) for x in str(code).strip().split()]:
        if len(word) in (2, 3, 4):
            if len(word) == 2:
                numbers[1] = word
            if len(word) == 3:
                numbers[7] = word
            if len(word) == 4:
                numbers[4] = word

    display[5] = numbers[1].replace(display[4], '')
    display[1] = numbers[7]
    for c in numbers[1]:
        display[1] = display[1].replace(c, '')
    display[2] = numbers[4]
    temp = ''.join(sorted(numbers[1] + display[3]))
    for c in temp:
        display[2] = display[2].replace(c, '')
    for key, value in ctr.items():
        if value == 7 and key != display[2]:
            display[6] = key
    return display


def decode(message, display):
    display_map = {"134567": "0", "45": '1', '12567': '2', '12456': '3', '2345': '4', '12346': '5', '123467': '6',
                   "145": '7', '1234567': '8', '123456': '9'}
    decoded = ''
    for n in (str(message).split()):
        for c in sorted(n):
            for key, letter in display.items():
                if letter == c:
                    n = n.replace(c, str(key))
        decoded += display_map[''.join(sorted(n))]
    return int(decoded)


if __name__ == "__main__":
    with open("input.txt") as f:
        lines = f.read().splitlines()
        notes = [line.split('|') for line in lines]
        output = 0
        for code, message in notes:
            key = crack_code(code)
            output += decode(message, key)
        print(output)
