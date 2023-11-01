use std::io::{self, BufRead};
use std::collections::HashSet;

#[derive(Clone, Copy)]
enum Turn {
    Left,
    Right,
}

impl Turn {
    fn new(c: char) -> Self {
        if c == 'L' {
            return Self::Left;
        } else {
            return Self::Right;
        }
    }
}

// >  to  ^  ->  0,1  to  -1,0
// ^  to  <  -> -1,0  to  0,-1
// <  to  v  -> 0,-1  to   1,0
// v  to  >  ->  1,0  to  0,-1
fn turn_left(dr: isize, dc: isize) -> (isize, isize) {
    return (-dc, dr);
}

// >  to  v  ->  0,1  to   1,0
// v  to  <  ->  1,0  to  0,-1
// <  to  ^  -> 0,-1  to  -1,0
// ^  to  >  -> -1,0  to   0,1
fn turn_right(dr: isize, dc: isize) -> (isize, isize) {
    return (dc, -dr);
}

fn advance_multiple(r: isize, c: isize, dr: isize, dc: isize, n: isize) -> (isize, isize) {
    let ndr = dr * n;
    let ndc = dc * n;
    return (r + ndr, c + ndc);
}

fn part1(instructions: &Vec<(Turn, isize)>) -> isize {
    let mut r = 0;
    let mut c = 0;

    let mut dr = -1;
    let mut dc = 0;

    for &(turn, n) in instructions {
        (dr, dc) = match turn {
            Turn::Left => turn_left(dr, dc),
            Turn::Right => turn_right(dr, dc),
        };
        (r, c) = advance_multiple(r, c, dr, dc, n);
    }
    return r.abs() + c.abs();
}

fn part2(instructions: &Vec<(Turn, isize)>) -> isize {
    let mut r = 0;
    let mut c = 0;

    let mut dr = -1;
    let mut dc = 0;

    let mut hm = HashSet::new();
    hm.insert((r, c));

    for &(turn, n) in instructions {
        (dr, dc) = match turn {
            Turn::Left => turn_left(dr, dc),
            Turn::Right => turn_right(dr, dc),
        };
        for _ in 0..n {
            (r, c) = (r + dr, c + dc);
            if hm.contains(&(r, c)) {
                return r.abs() + c.abs();
            } else {
                hm.insert((r, c));
            }
        }
    }
    return -1;
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let mut lines = stdin
        .lock()
        .lines();
    let mut line = lines.next().unwrap().unwrap();
    let instrs = line
        .split(", ")
        .map(|s| {
            let mut chars = s.chars();
            let turn = Turn::new(chars.next().unwrap());
            let n = chars.collect::<String>().parse::<isize>().unwrap();
            return (turn, n);
        })
        .collect::<Vec<_>>();

    // p1
    println!("{}", part1(&instrs));

    // p2
    println!("{}", part2(&instrs));

    Ok(())
}
