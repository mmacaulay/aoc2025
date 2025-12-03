from helpers import read_inputs

example_inputs = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,\
1698522-1698528,446443-446449,38593856-38593862,565653-565659,\
824824821-824824827,2121212118-2121212124"


class Day2:
    def __init__(self):
        pass

    def run(self, inputs: str) -> [int, int]:
        ranges = inputs.split(",")
        invalid_sum_part1 = 0
        invalid_sum_part2 = 0
        for r in ranges:
            start, end = r.split("-")
            start = int(start)
            end = int(end)
            for num in range(start, end + 1):
                if self.is_invalid_part1(num):
                    invalid_sum_part1 += num
                if self.is_invalid_part2(num):
                    invalid_sum_part2 += num
        return invalid_sum_part1, invalid_sum_part2

    def is_invalid_part1(self, num: int) -> bool:
        s = str(num)
        if (len(s) % 2) != 0:
            return False

        first_half = s[: len(s) // 2]
        second_half = s[len(s) // 2 :]

        if first_half == second_half:
            return True

        return False

    def is_invalid_part2(self, num: int) -> bool:
        s = str(num)
        s_len = len(s)
        factors = self.find_factors(len(s))
        factors.remove(1)  # remove 1 since it always matches

        for f in factors:
            segments = []
            segment_length = s_len // f
            for i in range(0, s_len // segment_length):
                segment = s[segment_length * i : segment_length * (i + 1)]
                segments.append(segment)

            if all(x == segments[0] for x in segments):
                return True

        return False

    def find_factors(self, num: int) -> [int]:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        return factors


def test_day2_isinvalid_basic():
    day2 = Day2()
    assert day2.is_invalid_part1(11) is True
    assert day2.is_invalid_part1(22) is True
    assert day2.is_invalid_part1(99) is True

    assert day2.is_invalid_part1(12) is False
    assert day2.is_invalid_part1(95) is False
    assert day2.is_invalid_part1(1) is False


def test_day2_isinvalid_four_digits():
    day2 = Day2()
    assert day2.is_invalid_part1(2222) is True
    assert day2.is_invalid_part1(9999) is True

    assert day2.is_invalid_part1(1212) is True
    assert day2.is_invalid_part1(5353) is True

    assert day2.is_invalid_part1(1234) is False
    assert day2.is_invalid_part1(1222) is False


def test_day2_is_invalid_part2_examples():
    day2 = Day2()
    assert day2.is_invalid_part2(1212) is True
    assert day2.is_invalid_part2(123123) is True
    assert day2.is_invalid_part2(12341234) is True

    assert day2.is_invalid_part2(1234) is False
    assert day2.is_invalid_part2(111222) is False
    assert day2.is_invalid_part2(1231231) is False


def test_day2_part1_examples():
    day2 = Day2()
    res_part1, _ = day2.run(example_inputs)
    assert res_part1 == 1227775554


def test_day1_part2_examples():
    day2 = Day2()
    _, res_part2 = day2.run(example_inputs)
    assert res_part2 == 4174379265


def test_day2_find_factors():
    day2 = Day2()
    factors = day2.find_factors(28)
    assert factors == [1, 2, 4, 7, 14, 28]

    factors = day2.find_factors(12)
    assert factors == [1, 2, 3, 4, 6, 12]


day2 = Day2()
result1, result2 = day2.run(read_inputs("day2.txt")[0])
print(f"Day 2 part 1: {result1}")
print(f"Day 2 part 2: {result2}")
