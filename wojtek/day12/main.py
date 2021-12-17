from collections import defaultdict


class Day12Part1:

    def __init__(self, connections):
        self.connections = connections
        self.routes = []

    def router(self, route: list, location):
        for r in self.connections[location]:

            if r == 'end':
                route.append(r)
                self.routes.append(route)
                continue

            if str(r).islower():
                if r in route:
                    continue

            temp = route.copy()
            temp.append(r)
            self.router(temp, r)
        return self.routes

class Day12Part2:

    def __init__(self, connections):
        self.connections = connections
        self.routes = []

    def mommy_can_we_go_back_to_small_cave(self, route):
        route_lower = [i for i in route if str(i).islower()]
        return len(route_lower) == len(set(route_lower))

    def router(self, route: list, location):
        for r in self.connections[location]:

            if r == 'end':
                temp = route.copy()
                temp.append(r)
                self.routes.append(temp)
                continue

            if str(r).islower():
                if r == 'start':
                    continue
                if r in route:
                    if self.mommy_can_we_go_back_to_small_cave(route):
                        temp = route.copy()
                        temp.append(r)
                        self.router(temp, r)
                        continue

                    continue


            temp = route.copy()
            temp.append(r)
            self.router(temp, r)
        return self.routes

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.read().splitlines()
        _connections = [line.split("-") for line in lines]
        d = defaultdict(list)
        for a, b in _connections:
            d[a].append(b)
            d[b].append(a)

        x = Day12Part1(d.copy())
        y = Day12Part2(d.copy())
        _routes_part2 = y.router(['start'], 'start')
        _routes_part1 = x.router(['start'], 'start')
        #print(*_routes_part1, sep='\n')
        print(len(_routes_part1))
        print(len(_routes_part2))

