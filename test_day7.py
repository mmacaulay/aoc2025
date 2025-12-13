from helpers import read_inputs

example_inputs = [
    ".......S.......",
    "...............",
    ".......^.......",
    "...............",
    "......^.^......",
    "...............",
    ".....^.^.^.....",
    "...............",
    "....^.^...^....",
    "...............",
    "...^.^...^.^...",
    "...............",
    "..^...^.....^..",
    "...............",
    ".^.^.^.^.^...^.",
    "...............",
]


class Day7:
    def __init__(self, input: [str]):
        self.input = input
        self.grid = [list(line) for line in input]

    def part1(self) -> int:
        beam_indices = set()
        beam_indices.add(self.grid[0].index("S"))
        split_coords = []
        splits = 0
        for r_index, r in enumerate(self.grid):
            for c_index, c in enumerate(r):
                if c == "^" and c_index in beam_indices:
                    splits += 1
                    split_coords.append((r_index, c_index))
                    beam_indices.remove(c_index)
                    beam_indices.add(c_index - 1)
                    beam_indices.add(c_index + 1)
        return splits


def test_part1():
    day7 = Day7(example_inputs)
    assert day7.part1() == 21


day7 = Day7(read_inputs("day7.txt"))
print(f"{day7.part1()}")
