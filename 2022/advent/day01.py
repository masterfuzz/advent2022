with open("../inputs/01_big") as fh:
    elves = [sum(int(x) for x in elf.split()) for elf in fh.read().split("\n\n")]

print(sum(sorted(elves)[-3:]))
