def __get_input_lines():
    with open("input.txt", "r", encoding="utf-8") as fh:
        return [line.strip() for line in fh.readlines()]


def day_1():
    lines = __get_input_lines()
    min_cube_req = {
        "red": 12,
        "green": 13,
        "blue": 14,
    }
    result = 0
    for line in lines:
        game_num = int(line.split(":")[0].split(" ")[1])
        game_valid = True
        for game in line.split(":")[1].split(";"):
            cubes = [g.strip() for g in game.split(",")]
            if not all(
                int(cube_count) <= min_cube_req[cube_color]
                for (cube_count, cube_color) in [c.split(" ") for c in cubes]
            ):
                game_valid = False
                break
        if game_valid:
            result += game_num
    print(result)


def day_2():
    lines = __get_input_lines()
    result = 0
    for line in lines:
        min_cube_req = {
            "red": 0,
            "green": 0,
            "blue": 0,
        }
        for game in line.split(":")[1].split(";"):
            for cube_count, cube_color in [
                g.strip().split(" ") for g in game.split(",")
            ]:
                min_cube_req[cube_color] = max(
                    min_cube_req[cube_color], int(cube_count)
                )
        result += min_cube_req["blue"] * min_cube_req["green"] * min_cube_req["red"]
    print(result)


def main():
    day_1()
    day_2()


if __name__ == "__main__":
    main()
