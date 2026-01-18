from dataclasses import dataclass
from math import sqrt

example_inputs = [
    "162,817,812",
    "57,618,57",
    "906,360,560",
    "592,479,940",
    "352,342,300",
    "466,668,158",
    "542,29,236",
    "431,825,988",
    "739,650,466",
    "52,470,668",
    "216,146,977",
    "819,987,18",
    "117,168,530",
    "805,96,715",
    "346,949,466",
    "970,615,88",
    "941,993,340",
    "862,61,35",
    "984,92,344",
    "425,690,689",
]


@dataclass
class Point:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    x: int
    y: int
    z: int


class Day8:
    def __init__(self, inputs: [str]):
        self.points = self.inputs_to_points(inputs=inputs)

    def euclidean_distance(self, point1, point2):
        return sqrt(
            (point1.x - point2.x) ** 2
            + (point1.y - point2.y) ** 2
            + (point1.z - point2.z) ** 2
        )

    def find_closest_pair(self, points: [Point]) -> (Point, float):
        min_distance = float("inf")
        closest_pair = (None, None)

        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dist = self.euclidean_distance(points[i], points[j])
                if dist < min_distance:
                    min_distance = dist
                    closest_pair = (points[i], points[j])

        return closest_pair, min_distance

    def inputs_to_points(self, inputs: [str]) -> [Point]:
        return list(
            map(
                lambda x: Point(x=int(x[0]), y=int(x[1]), z=int(x[2])),
                map(lambda i: i.split(","), inputs),
            )
        )

    def part1(self):
        points, dist = self.find_closest_pair(self.points)
        return points, dist


def test_find_closest_pair():
    day8 = Day8(example_inputs)
    points, dist = day8.find_closest_pair(day8.points)
    assert points == ((Point(162, 817, 812), Point(425, 690, 689)))
    assert round(dist, 4) == 316.9022
