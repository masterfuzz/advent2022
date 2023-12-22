from . import Advent, runner
from math import prod

def nlist(fh):
    return [int(x) for x in next(fh).split()[1:]]

def catlist(fh):
    return int("".join(next(fh).split()[1:]))

class Day06(Advent):
    PARSER = [nlist, nlist]
    PARSER_2 = [catlist, catlist]

    def part_one(self, rows):
        races = list(zip(*rows))

        total_wins = []
        for time, dist in races:
            race_wins = 0
            for n in range(1, time-1):
                if (time - n) * n > dist:
                    race_wins += 1
                elif race_wins > 0:
                    break
            total_wins.append(race_wins)
        return prod(total_wins)

    def part_two(self, rows):
        time, dist = rows
        race_wins = 0
        for n in range(1, time-1):
            if (time - n) * n > dist:
                race_wins += 1
            elif race_wins > 0:
                break
        return race_wins


runner(Day06())
