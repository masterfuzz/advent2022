from advent import Advent, runner
from progressbar import progressbar


def get_heightmap(fh):
    start = None
    goal = None
    rows = []
    for i, row in enumerate(fh.read().split("\n")):
        if "S" in row:
            start = i, row.index("S")
            row = row.replace("S", "a")
        if "E" in row:
            goal = i, row.index("E")
            row = row.replace("E", "z")
        rows.append([ord(c) - 97 for c in row])
    # print(rows)
    return start, goal, rows


class Day12(Advent):
    PARSER = [get_heightmap]

    def part_one(self, rows):
        start, goal, heights = rows
        # print(heights)
        # print(start, goal)

        return a_star(start, goal, heuristic, lambda n: get_neighbors(heights, n))

    def part_two(self, rows):
        start, goal, heights = rows

        return min(
            [
                q
                for q in progressbar(
                    [
                        a_star(
                            (i, j), goal, heuristic, lambda n: get_neighbors(heights, n)
                        )
                        for j in range(len(heights[0]))
                        for i in range(len(heights))
                        if heights[i][j] == 0
                    ]
                )
                if q
            ]
        )


def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def get_neighbors(grid, p):
    x, y = p
    for i, j in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
        if i < 0 or j < 0 or i > len(grid) - 1 or j > len(grid[0]) - 1:
            continue
        # print(len(grid), len(grid[0]))
        # print(i, j)
        if grid[i][j] <= grid[x][y] + 1:
            yield i, j
        # elif grid[i][j] == grid[x][y] + 1:
        #     yield i, j


def a_star(start, goal, heuristic, neighbors):
    INF = 3085350395009395
    open_set = {start}
    came_from = {}

    g_score = {}
    g_score[start] = 0

    f_score = {}
    f_score[start] = heuristic(start, goal)

    while open_set:
        current = sorted(open_set, key=lambda o: f_score[o])[0]
        # print(current)
        # del f_score[current]

        if current == goal:
            path = reconstruct_path(came_from, current)
            # print(path)
            return len(path)

        open_set.remove(current)

        n = list(neighbors(current))
        # print(n)
        for neighbor in neighbors(current):
            tentative_g = g_score[current] + 0.5
            if tentative_g < g_score.get(neighbor, INF):
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristic(neighbor, goal)

                open_set.add(neighbor)
    return None


def reconstruct_path(came_from, current):
    path = []
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path


runner(Day12())
