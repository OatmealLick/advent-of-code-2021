from collections import defaultdict
import time

class Day12:

    def __init__(self, connections):
        self.connections = connections

    def part1(self):
        routes = []
        return self.router(['start'], routes)

    def router(self, route: list, routes):
        location = route[-1]
        for r in self.connections[location]:

            if r == 'end':

                routes.append(route + [r])
                continue

            if str(r).islower():
                if r in route:
                    continue

            self.router(route.copy() + [r], routes)
        return routes

class Day12Part2:

    def __init__(self, connections):
        self.connections = connections
        self.routes = self.router(['start'], [])

    def get_routes(self):
        return self.routes

    def mommy_can_we_go_back_to_small_cave(self, route):
        route_lower = [i for i in route if str(i).islower()]
        return len(route_lower) == len(set(route_lower))

    def router(self, route: list, routes):

        location = route[-1]
        for r in self.connections[location]:

            if r == 'end':
                routes.append(route + [r])
                continue

            if str(r).islower():
                if r == 'start':
                    continue

                if r in route:
                    if self.mommy_can_we_go_back_to_small_cave(route):
                        self.router(route + [r], routes)
                        continue
                    continue

            self.router(route + [r], routes)
        return routes

if __name__ == "__main__":
    with open('input.txt') as f:
        lines = f.read().splitlines()
        _connections = [line.split("-") for line in lines]
        d = defaultdict(list)
        for a, b in _connections:
            d[a].append(b)
            d[b].append(a)




        start_time = time.perf_counter()
        x = Day12(d.copy())
        _routes_part1 = x.part1()
        print(len(_routes_part1), time.perf_counter() - start_time)

        start_time = time.process_time()
        y = Day12Part2(d.copy())
        _routes_part2 = y.get_routes()
        print(len(_routes_part2), time.process_time() - start_time)



