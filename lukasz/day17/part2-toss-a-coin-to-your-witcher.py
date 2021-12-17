from collections import namedtuple

Vec2 = namedtuple('Vec2', ['x', 'y'])


class Solution:
    def __init__(self, x_bounds, y_bounds):
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds

    def within_bounds(self, posx, posy):
        return self.x_bounds[0] <= posx <= self.x_bounds[1] and self.y_bounds[0] <= posy <= self.y_bounds[1]

    def find_velocity(self):
        count = 0
        for x in range(0, self.x_bounds[1] + 1):
            for y in range(self.y_bounds[0], 1111):
                vx = x
                vy = y
                # omg when you dont print its faster, who couldve known
                # print(f"Trying v {Vec2(x, y)}")
                posx = 0
                posy = 0
                while not self.below_target_and_no_hope(posy, posx):
                    posx = posx + vx
                    posy = posy + vy
                    if self.within_bounds(posx, posy):
                        count += 1
                        break
                        # omg break here
                    vx = vx -1 if vx > 0 else vx
                    vy -= 1
        return count

    def below_target_and_no_hope(self, posy, posx):
        # omg this was here before
        # return posy < self.y_bounds[0] and vy < 0
        return posy < self.y_bounds[0] or posx > self.x_bounds[1]


def main():
    filename = "input.txt"
    # filename = "input-sample.txt"
    with open(filename, "r") as f:
        line = f.read()
    line = line[13:].strip()
    parts = [part.strip()[2:] for part in line.split(",")]
    x_bounds = [int(p) for p in parts[0].split("..")]
    y_bounds = [int(p) for p in parts[1].split("..")]
    print(x_bounds, y_bounds)
    v = Solution(x_bounds, y_bounds).find_velocity()
    print(v)


if __name__ == "__main__":
    main()
