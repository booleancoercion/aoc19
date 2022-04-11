def solve():
    inp = open("../inputs/day1.txt")
    modules = [int(line) for line in inp.readlines()]
    output = sum([calc_fuel(mass) for mass in modules])
    print(f"Part 1: {output}")

    output = 0
    for mass in modules:
        fuel = calc_fuel(mass)
        while fuel > 0:
            output += fuel
            fuel = calc_fuel(fuel)

    print(f"Part 2: {output}")


def calc_fuel(mass):
    return mass // 3 - 2


if __name__ == "__main__":
    solve()
