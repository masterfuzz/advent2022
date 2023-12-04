from advent.parser import StarParser
from . import Advent, runner

rps = {
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
    "A": "rock",
    "B": "paper",
    "C": "scissors",
}

beats = {"rock": "paper", "scissors": "rock", "paper": "scissors"}
loses = {v: k for k, v in beats.items()}

value = {"rock": 1, "paper": 2, "scissors": 3}

need_to = {"X": "lose", "Y": "draw", "Z": "win"}


class Day02(Advent):
    PARSER = StarParser(lambda x: next(x).split())

    def part_one(self, rows):
        score = 0
        for op, me in [[rps[r] for r in row] for row in rows]:
            score += value[me]
            if op == me:
                score += 3
            elif me == beats[op]:
                score += 6

        return score

    def part_two(self, rows):
        score = 0
        for op, me in rows:
            op_throw = rps[op]
            if need_to[me] == "lose":
                my_throw = loses[op_throw]
            elif need_to[me] == "win":
                my_throw = beats[op_throw]
                score += 6
            else:
                score += 3
                my_throw = op_throw
            score += value[my_throw]
        return score


runner(Day02())
