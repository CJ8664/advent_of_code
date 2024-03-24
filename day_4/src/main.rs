use std::{
    collections::{HashMap, HashSet, VecDeque},
    fs::read_to_string,
};

fn read_input() -> Vec<String> {
    let lines = read_to_string("input.txt")
        .expect("Failed to read files")
        .lines()
        .map(|l| l.to_string())
        .collect::<Vec<String>>();
    return lines;
}

fn common_parsing(lines: &Vec<String>) -> HashMap<u16, u16> {
    let mut card_match_count = HashMap::new();
    for line in lines {
        let card_sepr = line.find(":").expect("Line should have this");
        let nums_sepr = line.find("|").expect("Line should have this");
        let card_num = line[..card_sepr]
            .split(" ")
            .last()
            .expect("Should exist")
            .parse::<u16>()
            .expect("Should be parseable");
        let winning_string = &line[(card_sepr + 1)..nums_sepr].trim();
        let actual_string = &line[(nums_sepr + 1)..].trim();
        let winning_nums: HashSet<u16> =
            HashSet::from_iter(winning_string.split(" ").filter_map(|x| x.parse().ok()));
        let actual_nums: HashSet<u16> =
            HashSet::from_iter(actual_string.split(" ").filter_map(|x| x.parse().ok()));
        card_match_count.insert(
            card_num,
            u16::try_from(winning_nums.intersection(&actual_nums).count())
                .expect("Count should be convertable"),
        );
    }
    return card_match_count;
}

fn part_1(card_match_count: &HashMap<u16, u16>) {
    let mut result: u16 = 0;
    card_match_count.values().for_each(|c| {
        if *c > 0 {
            result += 2_u16.pow((c - 1).into());
        }
    });
    println!("Part 1 {}", result);
}

fn part_2(card_match_count: &HashMap<u16, u16>) {
    let mut card_count = 0;
    let mut deque: VecDeque<u16> = VecDeque::new();
    deque.extend(card_match_count.keys());

    while deque.len() > 0 {
        let card_num = deque.pop_front().expect("Should exist");
        card_count += 1;
        let match_count = card_match_count.get(&card_num).expect("Should exist");
        for i in (card_num + 1)..(card_num + match_count + 1) {
            deque.push_back(i);
        }
    }
    println!("Part 2 {}", card_count);
}

fn main() {
    let lines = read_input();
    let card_match_count = common_parsing(&lines);
    part_1(&card_match_count);
    part_2(&card_match_count);
}
