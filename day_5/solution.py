import enum
from typing import List

sample = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4"""


class RangeMap:
    def __init__(self, start, delta, range):
        self.start = start
        self.delta = delta
        self.range = range

    def is_within_range(self, num):
        return self.start <= num <= self.start + self.range

    def get_destination(self, num):
        return num + self.delta

    def __repr__(self):
        return f"start: {self.start}, delta: {self.delta}, range: {self.range}\n"


class MapTypes(enum.Enum):
    SEED_TO_SOIL = enum.auto()
    SOIL_TO_FERTILIZER = enum.auto()
    FERTILIZER_TO_WATER = enum.auto()
    WATER_TO_LIGHT = enum.auto()
    LIGHT_TO_TEMP = enum.auto()
    TEMP_TO_HUMIDITY = enum.auto()
    HUMIDITY_TO_LOCATION = enum.auto()


type_map_map = {
    MapTypes.SEED_TO_SOIL: [],
    MapTypes.SOIL_TO_FERTILIZER: [],
    MapTypes.FERTILIZER_TO_WATER: [],
    MapTypes.WATER_TO_LIGHT: [],
    MapTypes.LIGHT_TO_TEMP: [],
    MapTypes.TEMP_TO_HUMIDITY: [],
    MapTypes.HUMIDITY_TO_LOCATION: [],
}

text_type_map_map = {
    "seed-to-soil map:": MapTypes.SEED_TO_SOIL,
    "soil-to-fertilizer map:": MapTypes.SOIL_TO_FERTILIZER,
    "fertilizer-to-water map:": MapTypes.FERTILIZER_TO_WATER,
    "water-to-light map:": MapTypes.WATER_TO_LIGHT,
    "light-to-temperature map:": MapTypes.LIGHT_TO_TEMP,
    "temperature-to-humidity map:": MapTypes.TEMP_TO_HUMIDITY,
    "humidity-to-location map:": MapTypes.HUMIDITY_TO_LOCATION,
}

SEEDS = []


def __get_input_lines():
    # return sample.splitlines()
    with open("input.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh.readlines()]


def common_parsing():
    global SEEDS, type_map_map
    lines = __get_input_lines()
    SEEDS = [int(x) for x in lines[0].split(":")[1].strip().split(" ")]
    idx = 1
    map_type = ""
    while idx < len(lines):
        if ":" in lines[idx]:
            map_type = lines[idx]
            temp_list: List[RangeMap] = []
            idx += 1
            while idx < len(lines) and lines[idx] != "":
                ranges = [int(x) for x in lines[idx].strip().split(" ")]
                range = RangeMap(ranges[1], (ranges[0] - ranges[1]), ranges[2])
                temp_list.append(range)
                idx += 1
            type_map_map[text_type_map_map[map_type]] = temp_list
        idx += 1


def get_mapped_value(num: int, map_type: MapTypes) -> int:
    for range in type_map_map[map_type]:
        if not range.is_within_range(num):
            continue
        return range.get_destination(num)
    return num


def part_1():
    locations = set()
    for seed in SEEDS:
        soil = get_mapped_value(seed, MapTypes.SEED_TO_SOIL)
        fertilizer = get_mapped_value(soil, MapTypes.SOIL_TO_FERTILIZER)
        water = get_mapped_value(fertilizer, MapTypes.FERTILIZER_TO_WATER)
        light = get_mapped_value(water, MapTypes.WATER_TO_LIGHT)
        temp = get_mapped_value(light, MapTypes.LIGHT_TO_TEMP)
        humidity = get_mapped_value(temp, MapTypes.TEMP_TO_HUMIDITY)
        location = get_mapped_value(humidity, MapTypes.HUMIDITY_TO_LOCATION)
        print(
            f"Seed: {seed}, soil: {soil}, fertilizer: {fertilizer}, water: {water}, light: {light}, temp: {temp}, humidity: {humidity}, location: {location}"
        )
        locations.add(location)
    print(f"Min location: {min(locations)}")


def part_2():
    pass


def main():
    common_parsing()
    part_1()
    # part_2(card_match_count)


if __name__ == "__main__":
    main()
