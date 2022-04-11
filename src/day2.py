from typing import Tuple


class VM:
    def __init__(self, data):
        self._pc = 0
        self.data = data[:]

    def step(self) -> bool:
        opcode = self.data[self._pc]
        pc = self._pc

        if opcode in [1, 2]:
            pos = self.data[pc+1:pc+4]
            num1, num2 = self.data[pos[0]], self.data[pos[1]]

            if opcode == 1:
                result = num1 + num2
            elif opcode == 2:
                result = num1 * num2

            self.data[pos[2]] = result
            self._pc += 4
            return True

        elif opcode == 99:
            return False
        else:
            raise Exception("Invalid Opcode")

    def simulate(self):
        while self.step():
            pass


def bruteforce(data, desired) -> Tuple[int, int]:
    for noun in range(100):
        for verb in range(100):
            vm = VM(data)
            vm.data[1] = noun
            vm.data[2] = verb

            vm.simulate()
            if vm.data[0] == desired:
                return noun, verb

    raise Exception("Couldn't find noun and verb")


with open("../inputs/day2.txt") as f:
    data = [int(x) for x in f.read().split(',')]

vm = VM(data)
vm.data[1] = 12
vm.data[2] = 2
vm.simulate()
print(f"Part 1: {vm.data[0]}")

noun, verb = bruteforce(data, 19690720)
print(f"Part 2: {100 * noun + verb}")
