from helpers import read_inputs

example_inputs = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
824824821-824824827,2121212118-2121212124"


class Day2:
    def __init__(self):
        pass

    def part1(self, inputs: str) -> int:
        ranges = inputs.split(",")
        invalid_sum = 0
        for r in ranges:
            start, end = r.split("-")
            start = int(start)
            end = int(end)
            for num in range(start, end + 1):
                if self.isinvalid(num):
                    invalid_sum += num
        return invalid_sum

    def isinvalid(self, num: int) -> bool:
        s = str(num)
        if (len(s) % 2) != 0:
            return False

        first_half = s[: len(s) // 2]
        second_half = s[len(s) // 2 :]
        # print(f"first_half: {first_half}, second_half: {second_half}")
        if first_half == second_half:
            return True

        return False


def test_day2_isinvalid_basic():
    day2 = Day2()
    assert day2.isinvalid(11) is True
    assert day2.isinvalid(22) is True
    assert day2.isinvalid(99) is True

    assert day2.isinvalid(12) is False
    assert day2.isinvalid(95) is False
    assert day2.isinvalid(1) is False


def test_day2_isinvalid_four_digits():
    day2 = Day2()
    assert day2.isinvalid(2222) is True
    assert day2.isinvalid(9999) is True

    assert day2.isinvalid(1212) is True
    assert day2.isinvalid(5353) is True

    assert day2.isinvalid(1234) is False
    assert day2.isinvalid(1222) is False


def test_day2_part1_examples():
    day2 = Day2()
    res = day2.part1(example_inputs)
    assert res == 1227775554


day2 = Day2()
res = day2.part1(read_inputs("day2.txt")[0])
print(f"Day 2 part 1: {res}")
