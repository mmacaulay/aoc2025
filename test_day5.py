from helpers import read_inputs

example_inputs = [
    "3-5",
    "10-14",
    "16-20",
    "12-18",
    "",
    "1",
    "5",
    "8",
    "11",
    "17",
    "32",
]


class Day5:
    def parse_inputs(self, lines: [str]) -> [[range], [int]]:
        ranges = []
        ingredients = []
        found_blank = False
        for line in lines:
            if found_blank:
                ingredients.append(int(line))
            elif line == "":
                found_blank = True
                continue
            else:
                start, end = map(int, line.split("-"))
                ranges.append(range(start, end + 1))

        return ranges, ingredients

    def is_fresh(self, ingredient_id, ranges: [range]) -> bool:
        return any(r for r in ranges if ingredient_id in r)

    def fresh_ingredients(self, ranges, ingredient_ids: [int]) -> [int]:
        return list(i for i in ingredient_ids if self.is_fresh(i, ranges))

    def explode_ranges(self, ranges: [range]) -> int:
        ranges.sort(key=lambda r: r.start)
        result = [ranges[0]]

        # if 2 ranges intersect
        # find the union and that to the list
        # else add both to the list
        for r in ranges[1:]:
            last = result[-1]
            if self.ranges_overlap(last, r):
                union = self.union_of_ranges(last, r)
                result[-1] = union
            else:
                result.append(r)

        return sum(r.stop - r.start for r in result)

    def ranges_overlap(self, r1: range, r2: range) -> bool:
        if r1.start <= r2.start:
            return r1.stop > r2.start
        else:
            return r2.stop > r1.start

    def union_of_ranges(self, r1: range, r2: range) -> range:
        start = min(r1.start, r2.start)
        end = max(r1.stop, r2.stop)
        return range(start, end)

    def part1(self, lines: [str]) -> int:
        ranges, ingredients = self.parse_inputs(lines)
        fresh_ingredients = self.fresh_ingredients(ranges, ingredients)
        return len(fresh_ingredients)

    def part2(self, lines: [str]) -> int:
        ranges, _ = self.parse_inputs(lines)
        return self.explode_ranges(ranges)


def test_parse_inputs():
    day5 = Day5()
    ranges, ingredients = day5.parse_inputs(example_inputs)
    assert ranges == [range(3, 6), range(10, 15), range(16, 21), range(12, 19)]
    assert ingredients == [1, 5, 8, 11, 17, 32]


def test_fresh_ingredients():
    day5 = Day5()
    ranges, ingredients = day5.parse_inputs(example_inputs)
    fresh_ingredients = day5.fresh_ingredients(ranges, ingredients)
    assert fresh_ingredients == [5, 11, 17]


def test_explode_ranges():
    day5 = Day5()
    ranges, _ = day5.parse_inputs(example_inputs)
    exploded = day5.explode_ranges(ranges)
    assert sorted(list(exploded)) == [
        3,
        4,
        5,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
    ]


lines = [line.strip() for line in read_inputs("day5.txt")]
day5 = Day5()
print(f"Part 1: {day5.part1(lines)}")
print(f"Part 2: {day5.part2(lines)}")
