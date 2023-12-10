from .parser import StarParser
from . import Advent, runner

def card_pair(fh):
    card_id, nums = next(fh).split(':')
    card_id = int(card_id.split()[1])

    winners, my_nums = [list(map(int, n.split())) for n in nums.split('|')]

    return card_id, winners, my_nums

def card_wins(winners, my_nums):
    same = set(winners).intersection(set(my_nums))
    return len(same)

class Day04(Advent):
    PARSER = StarParser(card_pair)

    def part_one(self, rows):
        total = 0
        for _card_id, winners, my_nums in rows:
            same = set(winners).intersection(set(my_nums))
            # print(card_id, same, len(same))
            if len(same) > 0:
                total += 2**(len(same)-1)
        return int(total)


    def part_two(self, rows):
        wins = {card_id: card_wins(winners, my_nums) for card_id, winners, my_nums in rows}
        copies = {card_id: 1 for card_id, _, _ in rows}

        # def rwins(card_id):
        #     pass
        #
        # total = 0
        for card_id, w in wins.items():
            # print(card_id, w)
            for n in range(w):
                # print("copy", card_id+n+1)
                copies[card_id+n+1] += copies[card_id]

        return sum(copies.values())

runner(Day04())
