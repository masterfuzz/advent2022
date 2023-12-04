from . import Advent, runner
from collections import defaultdict
from math import prod

def parser(row):
    game_id, rounds = row.split(':')
    game_id = int(game_id.split()[1])
    rounds = rounds.split(';')
    rounds = [r.split(',') for r in rounds]
    rounds = [[c.split() for c in r] for r in rounds]
    return game_id, rounds

# CUBES = only 12 red cubes, 13 green cubes, and 14 blue cubes
CUBES = {'red': 12, 'green': 13, 'blue': 14}

class Day02(Advent):

    def part_one(self, rows):
        games = list(map(parser, rows))
        possible_games = 0
        for game_id, rounds in games:
            possible = True
            for r in rounds:
                cubes = CUBES.copy()
                for n, color in r:
                    cubes[color] -= int(n)
                if any(n < 0 for n in cubes.values()):
                    possible = False
                    break
            if possible:
                possible_games += game_id

        return possible_games

    def part_two(self, rows):
        games = list(map(parser, rows))

        power = 0
        for _, rounds in games:
            cubes = defaultdict(list)
            for r in rounds:
                # assert len(set(color for _, color in r)) == len(r) 
                for n, color in r:
                    cubes[color].append(int(n))
            power += prod(max(n) for n in cubes.values())
        return power
                
                




runner(Day02())
