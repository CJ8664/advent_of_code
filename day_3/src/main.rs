use std::{
    borrow::BorrowMut,
    collections::{HashMap, HashSet},
    fs::read_to_string,
};

struct SpecialChar {
    row: i16,
    col: i16,
    matched_nums: Vec<i32>,
}

impl SpecialChar {
    fn new(r: i16, c: i16) -> SpecialChar {
        let matched_nums = Vec::new();
        SpecialChar {
            row: r,
            col: c,
            matched_nums,
        }
    }
}

fn read_input() -> Vec<String> {
    let lines = read_to_string("input.txt")
        .expect("Failed to read file")
        .lines()
        .map(|x| x.to_string())
        .collect::<Vec<String>>();
    return lines;
}

fn check_candidate(
    row: i16,
    cols: HashSet<i16>,
    num: i32,
    special_char_coords: &mut HashMap<i16, Vec<SpecialChar>>,
) {
    for r in (row - 1)..(row + 2) {
        for c in (cols.iter().min().unwrap() - 1)..(cols.iter().max().unwrap() + 2) {
            special_char_coords.entry(r).and_modify(|special_chars| {
                special_chars.iter_mut().for_each(|special_char| {
                    if (special_char.row == r) && (special_char.col == c) {
                        special_char.matched_nums.push(num);
                        return;
                    }
                });
            });
        }
    }
}

fn common_parsing(special_char_coords: &mut HashMap<i16, Vec<SpecialChar>>) {
    let lines = read_input();
    for (r, line) in lines.iter().enumerate() {
        let row = i16::try_from(r).expect("Failed to convert row");
        for (c, ch) in line.char_indices() {
            let col = i16::try_from(c).expect("Failed to convert col");
            if !ch.is_digit(10) && ch != '.' {
                if !special_char_coords.contains_key(&row) {
                    special_char_coords.insert(row, Vec::new());
                }
                special_char_coords.entry(row).and_modify(|x| {
                    let special_char = SpecialChar::new(row, col);
                    println!("{} {}", row, col);
                    x.push(special_char);
                });
            }
        }
    }

    for (r, line) in lines.iter().enumerate() {
        let row = i16::try_from(r).expect("Failed to convert row");
        let mut num = String::new();
        let mut cols: HashSet<i16> = HashSet::new();
        for (c, ch) in line.char_indices() {
            let col = i16::try_from(c).expect("Failed to convert col");
            if ch.is_digit(10) {
                num += &ch.to_string();
                cols.insert(col);
            } else if num != "" {
                check_candidate(
                    row,
                    cols,
                    num.parse::<i32>()
                        .expect("Failed to convert num string to int"),
                    special_char_coords.borrow_mut(),
                );
                num = String::new();
                cols = HashSet::new();
            }
        }
        if num != "" {
            check_candidate(
                row,
                cols,
                num.parse::<i32>()
                    .expect("Failed to convert num string to int"),
                special_char_coords.borrow_mut(),
            );
        }
    }
}

fn part_1(special_char_coords: &HashMap<i16, Vec<SpecialChar>>) {
    let mut result = 0;
    special_char_coords.values().for_each(|special_chars| {
        special_chars.iter().for_each(|special_char| {
            result += special_char.matched_nums.iter().sum::<i32>();
        });
    });
    println!("Part 1 {}", result);
}

fn part_2(special_char_coords: &HashMap<i16, Vec<SpecialChar>>) {
    let mut result = 0;
    special_char_coords.values().for_each(|special_chars| {
        special_chars.iter().for_each(|special_char| {
            if special_char.matched_nums.len() == 2 {
                result += special_char.matched_nums[0] * special_char.matched_nums[1];
            }
        });
    });
    println!("Part 2 {}", result);
}

fn main() {
    let mut special_char_coords: HashMap<i16, Vec<SpecialChar>> = HashMap::new();
    common_parsing(special_char_coords.borrow_mut());
    part_1(&special_char_coords);
    part_2(&special_char_coords);
}
