use std::{cmp::max, collections::HashMap, fs};

fn read_input_file() -> Vec<String> {
    let contents = fs::read_to_string("input.txt").expect("Failed to read file");
    let lines = contents
        .lines()
        .map(|x| x.trim().to_string())
        .collect::<Vec<String>>();
    return lines;
}

fn part_1(lines: Vec<String>) -> i32 {
    let min_cube_req = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);
    let mut result = 0;
    for line in lines {
        let parts = line.split(":").collect::<Vec<&str>>();
        let game_num = parts[0]
            .split(" ")
            .nth(1)
            .unwrap()
            .parse::<i32>()
            .expect("Parse error");
        let mut game_valid = true;
        for game in parts[1].split(";") {
            let mut cube_results = game.split(",").map(|x| -> (i32, &str) {
                let y = x.trim().split(" ").collect::<Vec<&str>>();
                return (y[0].parse::<i32>().expect("Parse error"), y[1]);
            });
            if !cube_results.all(|(cube_count, cube_color)| cube_count <= min_cube_req[cube_color])
            {
                game_valid = false;
                break;
            }
        }
        if game_valid {
            result += game_num;
        }
    }
    return result;
}

fn part_2(lines: Vec<String>) -> i32 {
    let mut result = 0;
    for line in lines {
        let mut min_cube_req = HashMap::from([("red", 0), ("green", 0), ("blue", 0)]);
        for game in line.split(":").nth(1).unwrap().split(";") {
            for (cube_count, cube_color) in game.split(",").map(|x| -> (i32, &str) {
                let y = x.trim().split(" ").collect::<Vec<&str>>();
                return (y[0].parse().expect("Parse error"), y[1]);
            }) {
                min_cube_req.insert(cube_color, max(min_cube_req[cube_color], cube_count));
            }
        }
        result += min_cube_req["blue"] * min_cube_req["green"] * min_cube_req["red"];
    }
    return result;
}

fn main() {
    let lines = read_input_file();
    let res_1 = part_1(lines.clone());
    println!("Part 1 {}", res_1);

    let res_2 = part_2(lines.clone());
    println!("Part 2 {}", res_2);
}
