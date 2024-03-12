use std::fs;

fn read_input_file() -> Vec<String> {
    let contents = fs::read_to_string("input.txt").expect("Failed to reead file");
    let lines = contents
        .split("\n")
        .map(|x| x.trim().to_string())
        .collect::<Vec<String>>();
    return lines;
}

fn day_1(lines: Vec<String>) -> u32 {
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

fn main() {
    let lines = read_input_file();
    let result = day_1(lines);
    println!("Day 1 {}", result);
}
