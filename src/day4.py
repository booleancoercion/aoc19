def solve():
    with open("../inputs/day4.txt") as f:
        data = f.read()

    a, b = data.split('-')
    a, b = int(a), int(b)

    valid1 = [pwd for pwd in range(a, b+1) if is_valid(pwd)]
    print(f"Part 1: {len(valid1)}")

    valid2 = [pwd for pwd in valid1 if is_valid2(pwd)]
    print(f"Part 2: {len(valid2)}")


def is_valid(pwd):
    last_digit = 10
    has_double = False

    for _ in range(6):
        digit = pwd % 10
        if digit == last_digit:
            has_double = True
        if digit > last_digit:
            return False

        last_digit = digit
        pwd //= 10

    return has_double


def is_valid2(pwd):
    counts = [0 for _ in range(10)]
    for _ in range(6):
        counts[pwd % 10] += 1
        pwd //= 10

    return any(x == 2 for x in counts)


if __name__ == "__main__":
    solve()
