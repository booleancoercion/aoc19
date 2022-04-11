from typing import Dict, Tuple


def solve():
    with open("../inputs/day3.txt") as f:
        [wire1, wire2] = [wire.split(',') for wire in f.readlines()]

    pt1 = fill_grid(wire1)
    pt2 = fill_grid(wire2)

    isct = {(x, y): t + pt2[(x, y)]
            for ((x, y), t) in pt1.items() if (x, y) in pt2}
    dist = min(abs(x) + abs(y) for (x, y) in isct.keys())
    print(f"Part 1: {dist}")

    time = min(isct.values())
    print(f"Part 2: {time}")


def fill_grid(wire) -> Dict[Tuple[int, int], int]:
    x, y, t = 0, 0, 0
    grid = dict()

    for instr in wire:
        (dx, dy) = get_offset(instr[0])
        amt = int(instr[1:])

        for _ in range(amt):
            x += dx
            y += dy
            t += 1
            if (x, y) not in grid:
                grid[(x, y)] = t
    return grid


def get_offset(letter):
    if letter == 'R':
        return (1, 0)
    elif letter == 'L':
        return (-1, 0)
    elif letter == 'U':
        return (0, 1)
    elif letter == 'D':
        return (0, -1)


if __name__ == "__main__":
    solve()
