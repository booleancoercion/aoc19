def calc_fuel(mass):
    return mass // 3 - 2


with open("../inputs/day1.txt") as inp:
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
