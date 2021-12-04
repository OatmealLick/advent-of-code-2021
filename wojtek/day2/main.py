# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.



def path_route(commands):
    aim = 0
    x = 0
    y = 0
    for c, value in commands:
        if c == "forward":
            x += value
            y += value * aim
        elif c == "down":
            aim += value
        else:
            aim -= value

    return x * y

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open("input.txt") as f:
        lines = [line.strip().split(" ") for line in f.readlines()]
        commands = [[command[0], int(command[1])] for command in lines]
    #print(path_route([['forward', 5], ['down', 5], ['forward', 8], ['up', 3], ['down', 8], ['forward', 2]]))
    print(path_route(commands))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
