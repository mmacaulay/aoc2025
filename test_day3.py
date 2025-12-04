from helpers import read_inputs

example_inputs = [
    987654321111111,
    811111111111119,
    234234234234278,
    818181911112111,
]


class Day3:
    def __init__(self, banks: [int] = []):
        self.banks = banks

    def total_output_joltage(self) -> int:
        total = 0
        for bank in self.banks:
            total += self.largest_joltage(bank)
        return total

    def largest_joltage(self, bank: int) -> int:
        digits = list(map(int, str(bank)))

        # exclude last digit
        max_digit, index = self.find_max_digit(digits[: len(digits) - 1])

        # search right of max digit for next max
        next_max_digit, _ = self.find_max_digit(digits[index + 1 :])
        return int(str(max_digit) + str(next_max_digit))

    def find_max_digit(self, digits: []) -> [int, int]:
        max = 0
        index = 0
        for i in range(len(digits)):
            digit = digits[i]
            if digit > max:
                max = digit
                index = i
        return max, index


def test_find_max_digit():
    day3 = Day3()
    assert day3.find_max_digit([1, 2, 3, 4, 5]) == (5, 4)
    assert day3.find_max_digit([5, 4, 3, 2, 1]) == (5, 0)
    assert day3.find_max_digit([1, 3, 2, 5, 4]) == (5, 3)


def test_largest_joltage():
    day3 = Day3()
    assert day3.largest_joltage(987654321111111) == 98
    assert day3.largest_joltage(811111111111119) == 89
    assert day3.largest_joltage(234234234234278) == 78
    assert day3.largest_joltage(818181911112111) == 92


day3 = Day3(map(int, read_inputs("day3.txt")))

print(f"Total joltage: {day3.total_output_joltage()}")
