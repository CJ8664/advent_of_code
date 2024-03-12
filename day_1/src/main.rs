use std::collections::{HashMap, HashSet};
use std::fs;

fn read_input_file() -> Vec<String> {
    let contents = fs::read_to_string("input.txt").expect("Failed to reead file");
    let lines = contents
        .split("\n")
        .map(|x| x.trim().to_string())
        .collect::<Vec<String>>();
    return lines;
}

fn part_1(lines: Vec<String>) -> u32 {
    let mut result = 0;
    for line in lines {
        let mut digits: Vec<u32> = vec![];
        for char in line.chars() {
            if char.is_numeric() {
                digits.push(char.to_digit(10).unwrap());
            }
        }
        if digits.len() > 1 {
            result += digits.first().unwrap() * 10 + digits.last().unwrap();
        } else {
            result += digits.first().unwrap() * 10 + digits.first().unwrap();
        }
    }
    return result;
}

fn part_2(lines: Vec<String>) -> u32 {
    let mut result = 0;
    let num_map: HashMap<&str, u32> = HashMap::from([
        ("one", 1),
        ("two", 2),
        ("three", 3),
        ("four", 4),
        ("five", 5),
        ("six", 6),
        ("seven", 7),
        ("eight", 8),
        ("nine", 9),
    ]);
    let start_chars: HashSet<char> =
        HashSet::from_iter(num_map.keys().map(|k| (k.chars().nth(0).unwrap())));
    for line in lines {
        let mut digits: Vec<u32> = vec![];
        for (idx, ch) in line.char_indices() {
            if ch.is_numeric() {
                digits.push(ch.to_digit(10).unwrap());
            } else if start_chars.contains(&ch) {
                for i in 3..6 {
                    if (idx + i) <= line.len() {
                        let k = line.get(idx..(idx + i)).unwrap();
                        if num_map.contains_key(k) {
                            digits.push(*num_map.get(k).unwrap());
                        }
                    }
                }
            }
        }
        if digits.len() > 1 {
            result += digits.first().unwrap() * 10 + digits.last().unwrap();
        } else {
            result += digits.first().unwrap() * 10 + digits.first().unwrap();
        }
    }
    return result;
}

fn main() {
    let lines = read_input_file();
    let result1 = part_1(lines.clone());
    println!("Day 1 {}", result1);
    let result2 = part_2(lines.clone());
    println!("Day 2 {}", result2);
}
