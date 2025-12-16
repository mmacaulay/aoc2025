from helpers import read_inputs
from dataclasses import dataclass


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


@dataclass
class Node:
    data: str
    particles: int


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

    def part2(self) -> int:
        previous_row = [Node(data="", particles=0)] * len(self.grid)
        current_row = [Node(data="", particles=0)] * len(self.grid)
        start_index = self.grid[0].index("S")
        previous_row[start_index] = Node(data="S", particles=1)

        for r_index, r in enumerate(self.grid):
            for c_index, c in enumerate(r):
                left_parent = (
                    previous_row[c_index - 1]
                    if c_index > 0
                    else Node(data=None, particles=0)
                )
                right_parent = (
                    previous_row[c_index + 1]
                    if c_index < len(self.grid) - 1
                    else Node(data=None, particles=0)
                )
                direct_parent = previous_row[c_index]

                particles = 0
                if direct_parent.data != "^":
                    particles = direct_parent.particles
                if left_parent.data == "^":
                    particles += left_parent.particles
                if right_parent.data == "^":
                    particles += right_parent.particles

                current_row[c_index] = Node(data=c, particles=particles)

            previous_row = current_row
            current_row = [Node(data="", particles=0)] * len(self.grid)

        return sum(map(lambda b: b.particles, previous_row))


def test_part1():
    day7 = Day7(example_inputs)
    assert day7.part1() == 21


def test_part2():
    day7 = Day7(example_inputs)
    assert day7.part2_loop_rows() == 40


day7 = Day7(read_inputs("day7.txt"))
print(f"{day7.part1()}")
print(f"{day7.part2()}")
