from advent import Advent, runner


def parse(fh):
    stacks, moves = fh.read().split("\n\n")
    stacks = stacks.split("\n")

    queues = {int(n): [] for n in stacks[-1].split()}

    for stack in reversed(stacks[:-1]):
        for q in queues:
            c: str = stack[(q - 1) * 4 + 1]
            if c.isalpha():
                queues[q].append(c)

    parsed_moves = []
    for move in moves.split("\n"):
        _, x, _, y, _, z = move.split()
        parsed_moves.append((int(x), int(y), int(z)))

    return queues, parsed_moves


class Day05(Advent):
    PARSER = [parse]

    def part_one(self, rows):
        pass
        queues, moves = rows
        queues = {k: v.copy() for k, v in queues.items()}

        for qty, src, dst in moves:
            for _ in range(qty):
                x = queues[src].pop()
                queues[dst].append(x)
        return "".join([v[-1] for v in queues.values()])

    def part_two(self, rows):
        queues, moves = rows

        for qty, src, dst in moves:
            x = []
            for _ in range(qty):
                x.append(queues[src].pop())

            queues[dst] += reversed(x)

        return "".join([v[-1] for v in queues.values()])


runner(Day05())
