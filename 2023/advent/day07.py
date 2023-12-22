from .parser import StarParser
from . import Advent, runner
from functools import total_ordering
from collections import Counter


def card(ch: str):
    if ch.isnumeric():
        return int(ch)
    return {
            'T': 10,
            'J': 11,
            'Q': 12,
            'K': 13,
            'A': 14,
            }[ch]


@total_ordering
class Hand:
    def __init__(self, fh):
        s = next(fh)
        if s.strip() == '':
            raise StopIteration()
        self.hand, self.bid = s.split()
        self.hand = tuple(card(ch) for ch in self.hand)
        self.bid = int(self.bid)

    def __repr__(self):
        return f"{self.hand} {self.bid}"

    def kind(self) -> int:
        counts = Counter(self.hand)
        sorted_counts = sorted(counts.values(), reverse=True)
        match sorted_counts:
            case [5]:
                return 6
            case [4, 1]:
                return 5
            case [3, 2]:
                return 4
            case [3, 1, 1]:
                return 3
            case [2, 2, 1]:
                return 2
            case [2, 1, 1, 1]:
                return 1
            case [1, 1, 1, 1, 1]:
                return 0
        raise Exception(f"this didn't get ranked: {self.hand} -> {sorted_counts}")

    def __lt__(self, b: 'Hand'):
        if self.kind() == b.kind():
            return self.hand < b.hand
        return self.kind() < b.kind()


Joker = 1
class Hand2(Hand):
    def __init__(self, fh):
        super().__init__(fh)

        self.hand = tuple(1 if h == 11 else h for h in self.hand)

    def kind(self) -> int:
        counts = Counter(self.hand)
        sorted_counts = sorted(counts.values(), reverse=True)
        jokers = counts.get(Joker)
        match sorted_counts:
            case [5]:
                return 6
            case [4, 1]:
                if jokers:
                    return 6
                return 5
            case [3, 2]:
                if jokers:
                    return 6
                return 4
            case [3, 1, 1]:
                if jokers:
                    return 5
                return 3
            case [2, 2, 1]:
                if jokers == 2:
                    return 5
                if jokers == 1:
                    return 4
                return 2
            case [2, 1, 1, 1]:
                if jokers:
                    return 3
                return 1
            case [1, 1, 1, 1, 1]:
                if jokers:
                    return 1
                return 0
        raise Exception(f"this didn't get ranked: {self.hand} -> {sorted_counts}")


class Day07(Advent):
    PARSER = StarParser(Hand)
    PARSER_2 = StarParser(Hand2)

    def part_one(self, rows):
        return sum((i+1)*hand.bid for i, hand in enumerate(sorted(rows)))

    def part_two(self, rows):
        return sum((i+1)*hand.bid for i, hand in enumerate(sorted(rows)))


runner(Day07())
