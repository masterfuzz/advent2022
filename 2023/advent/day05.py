from . import Advent, runner
from .parser import ParserSkip, StarParser

class Mapper:
    def __init__(self, rows) -> None:
        self.rows = rows

    def get(self, ix):
        for dest, src, length in self.rows:
            if ix >= src and ix < src + length:
                return ix - src + dest, length - (ix - src)
        return ix, 0

    def get_range(self, ix, length):
        L1, R1 = ix, ix + length - 1

        empty = True
        for dest, src, rng in self.rows:
            L2, R2 = src, src + rng - 1

            # disjoint
            if L1 > R2 or R1 < L2: continue

            # intersection
            L3, R3 = max(L1, L2), min(R1, R2)

            print(f"{ix},{length} -> {L3-src+dest},{R3-L3}")
            yield L3 - src + dest, R3-L3
            empty = False

        if empty:
            print(f"{ix},{length} -> doesn't match!")
            yield ix, length

        

    def __repr__(self) -> str:
        return f"Mapper<{self.rows}>"

def parse(fh):
    return [int(x) for x in next(fh).split(': ')[1].split()]


def mapper(fh) -> Mapper:
    rows = []
    next(fh)
    while row := next(fh).strip():
        rows.append([int(x) for x in row.split()])
    return Mapper(rows)


class Day05(Advent):
    PARSER = [parse, ParserSkip(), StarParser(mapper)]

    def part_one(self, rows):
        seeds, mappers = rows
        # print(seeds)
        # for mapper in mappers:
        #     print(mapper)

        locations = []
        for seed in seeds:
            loc = seed
            for mapper in mappers:
                loc, _ = mapper.get(loc)
            locations.append(loc)
        return min(locations)


    def part_two(self, rows):
        seeds, mappers = rows
        seed_ranges = [(seeds[i], seeds[i+1]) for i in range(0, len(seeds), 2)]
        print(seed_ranges)
        print(sum(r for _, r in seed_ranges))

        min_location = None
        for start, length in seed_ranges:
            rngs = list(mappers[0].get_range(start, length))
            for m in mappers[1:]:
                rngs = [rng for a, b in rngs for rng in m.get_range(a, b)]
            n = min([ix for ix, _ in rngs])
            min_location = min(n, min_location) if min_location else n

        return min_location

runner(Day05())
