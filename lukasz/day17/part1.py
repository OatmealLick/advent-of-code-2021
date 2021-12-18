from collections import namedtuple

Vec2 = namedtuple('Vec2', ['x', 'y'])

class Solution:
    def __init__(self, x_bounds, y_bounds):
        self.x_bounds = x_bounds
        self.y_bounds = y_bounds

    def within_bounds(self, pos):
        return self.where_are_you(pos) == Vec2(0, 0)

    def where_are_you(self, pos):
        if pos.x < self.x_bounds[0]: 
            x = -1
        elif self.x_bounds[0] <= pos.x <= self.x_bounds[1]:
            x = 0
        else:
            x = 1
        if pos.y < self.y_bounds[0]:
            y = -1
        elif self.y_bounds[0] <= pos.y <= self.y_bounds[1]:
            y = 0
        else:
            y = 1
        return Vec2(x, y)

    def find_velocity(self):
        v = Vec2(2, 3)
        last_working_v = None
        last_max_y = None
        iterations = 1000
        i = 0
        while i < iterations:
            print(f"Trying v {v}")
            success, result, max_y = self.simulate_velocity(v)
            if success:
                last_working_v = v
                last_max_y = max_y
                v = Vec2(v.x, v.y + 1)
            else:
                if result.x == -1:
                    v = Vec2(v.x + 1, v.y)
                elif result.x == 1:
                    v = Vec2(v.x - 1, v.y)
                else:
                    v = Vec2(v.x, v.y + 1)
                    print(f"Overshoot {v}")
            i += 1
        print(f"Last max y {last_max_y}")
        return last_working_v


    def below_target_and_no_hope(self, pos, v):
        return pos.y < self.y_bounds[0] and v.y < 0

    def simulate_velocity(self, v):
        pos = Vec2(0, 0)
        max_y = 0
        result = self.where_are_you(pos)
        steps = 0
        while not self.below_target_and_no_hope(pos, v):
            # print(f"S {steps} pos {pos}, v {v}")
            pos = Vec2(pos.x + v.x, pos.y + v.y)
            max_y = max(max_y, pos.y)
            result = self.where_are_you(pos)
            if result == Vec2(0, 0):
                return True, result, max_y
            vx = v.x + 1 if v.x < 0 else v.x - 1
            v = Vec2(vx, v.y - 1)
            steps += 1
        return False, result, max_y

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
