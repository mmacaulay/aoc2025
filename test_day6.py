from helpers import read_inputs
from dataclasses import dataclass
from math import prod

# had to preserve spacing here for part 2
example_inputs = [
    "123 328  51 64 ",
    " 45 64  387 23 ",
    "  6 98  215 314",
    "*   +   *   +  ",
]


@dataclass
class Problem:
    operator: str
    operands: [int]


class Day6:
    def __init__(self, inputs: [str] = []):
        self.inputs = inputs

    def parse_inputs(self, inputs: [str]) -> [Problem]:
        lines = [i.split() for i in inputs]
        problems = []
        for i in range(len(lines[0])):
            operands = []
            operator = ""
            for j in range(len(lines)):
                item = lines[j][i]
                if item == "*" or item == "+":
                    operator = item
                else:
                    operands.append(int(item))
            problems.append(Problem(operator=operator, operands=operands))
        return problems

    def solve(self, problem: Problem) -> int:
        fn = sum if problem.operator == "+" else prod
        return fn(problem.operands)

    def part1(self) -> int:
        problems = self.parse_inputs(self.inputs)
        return sum(self.solve(p) for p in problems)

    def parse_right_to_left_columns(self, rows: [[str]]) -> [Problem]:
        problems = []
        current_operator = None
        current_columns = []
        for c in range(len(rows[0]) - 1, -1, -1):
            # if all columns are a space, then move to next problem
            chars_in_column = [r[c] for r in rows]
            last_char = chars_in_column.pop()
            current_columns.append(chars_in_column)
            if all(c == " " for c in chars_in_column):
                continue
            elif last_char == "+" or last_char == "*":
                current_operator = last_char
                # operands are always left-aligned, so this is the end of the current problem
                operands = self.parse_columns_to_operands(current_columns)
                problems.append(Problem(operator=current_operator, operands=operands))
                current_columns = []
                current_operator = None

        return problems

    def parse_columns_to_operands(self, columns: [[str]]) -> [int]:
        operands = []
        for col in columns:
            number_str = "".join(col).strip()
            if number_str:
                operands.append(int(number_str))
        return operands

    def part2(self) -> int:
        rows = [list(i) for i in self.inputs]
        problems = self.parse_right_to_left_columns(rows)
        return sum(self.solve(p) for p in problems)


def test_example_inputs():
    day6 = Day6(example_inputs)
    assert day6.part1() == 4277556


day6 = Day6(read_inputs("day6.txt"))
print(f"{day6.part1()}")
print(f"{day6.part2()}")
