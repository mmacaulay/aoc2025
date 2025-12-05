from helpers import read_inputs

example_inputs = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]


class Day4:
    def __init__(self, grid: [list[str]] = []):
        self.grid = grid

    def part1(self):
        result = 0
        print(self.grid)
        for r, row in enumerate(self.grid):
            for c, col in enumerate(row):
                if (self.grid[r][c]) != "@":
                    continue
                neighbours = self.find_surrounding(r, c)
                print(f"row {r} col {c} neighbours: {neighbours}")
                if sum(1 for n in neighbours if n == "@") < 4:
                    print(f"row {r} col {c} is accessible")
                    result += 1

        return result

    def find_surrounding(self, row_index: int, col_index: int) -> list[str]:
        result = []
        for r, c in [
            (row_index - 1, col_index - 1),
            (row_index - 1, col_index),
            (row_index - 1, col_index + 1),
            (row_index, col_index - 1),
            (row_index, col_index + 1),
            (row_index + 1, col_index - 1),
            (row_index + 1, col_index),
            (row_index + 1, col_index + 1),
        ]:
            if r >= 0 and r < len(self.grid) and c >= 0 and c < len(self.grid[r]):
                result.append(self.grid[r][c])

        return result


def test_part1():
    day4 = Day4(list(map(list, example_inputs)))
    assert day4.part1() == 13


day4 = Day4(list(map(list, read_inputs("day4.txt"))))
print(f"{day4.part1()}")
