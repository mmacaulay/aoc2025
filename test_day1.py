example_inputs = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]


class Day1:

    dial: int = 0

    def __init__(self, start: int = 50):
        self.dial = start

    def read_inputs(self, path: str = "day1.txt") -> [str]:
        with open(path, "r") as f:
            inputs = f.readlines()
        return inputs

    def rotate(self, cmd: str):
        direction = cmd[0]
        magnitude = int(cmd[1:])

        if direction == "L":
            magnitude *= -1

        self.dial += magnitude

        if self.dial < 0:
            self.dial = 100 + (self.dial % 100)

        if self.dial >= 100:
            self.dial = self.dial % 100

        print(f"direction {direction}")
        print(f"magnitude: {magnitude}")
        print(f"dial: {self.dial}\n")

    def part1(self, inputs: [str]) -> int:
        print(f"dial: {self.dial}")
        zeroes = 0
        for input in inputs:
            self.rotate(input)
            if self.dial == 0:
                zeroes += 1
        print(f"Total zeroes: {zeroes}")
        return zeroes

    def part2(self, inputs: [str]) -> int:
        pass


def test_day1_part1_examples():
    day1 = Day1()
    res = day1.part1(example_inputs)
    assert res == 3


def test_day1_rotate_handles_positive_wraparound():
    day1 = Day1(start=95)
    day1.rotate("R10")
    assert day1.dial == 5


def test_day1_rotate_handles_negative_wraparound():
    day1 = Day1(start=50)
    day1.rotate("L68")
    assert day1.dial == 82


def test_day1_rotate_positive_plus_one():
    day1 = Day1(start=99)
    day1.rotate("R1")
    assert day1.dial == 0


def test_day1_rotate_negative_minus_one():
    day1 = Day1(start=0)
    day1.rotate("L1")
    assert day1.dial == 99


def test_day1_rotate_handles_large_magnitude():
    day1 = Day1(start=10)
    day1.rotate("R250")
    assert day1.dial == 60


def test_day1_rotate_handles_large_negative_magnitude():
    day1 = Day1(start=10)
    day1.rotate("L270")
    assert day1.dial == 40


day1 = Day1()
day1.part1(day1.read_inputs())
