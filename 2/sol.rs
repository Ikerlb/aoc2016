use std::io::{BufRead, self};
use std::cmp::{min, max};

fn step(grid: &Vec<Vec<char>>, r: isize, c: isize, dr: isize, dc: isize) -> (isize, isize) {
    let n = grid.len() as isize;
    let m = grid[grid.len() - 1].len() as isize;
    if ((r + dr) < 0) | ((c + dc) < 0) | ((r + dr) == n) | ((c + dc) == m) {
        return (r, c);
    } else {
        let nr = (r + dr) as usize;
        let nc = (c + dc) as usize;
        if grid[nr][nc] == '#' {
            return (r, c);
        } else {
            return (nr as isize, nc as isize);
        }
    }

}

fn steps(grid: &Vec<Vec<char>>, r: usize, c: usize, instrs: &str) -> (usize, usize) {
    let mut r = r as isize;
    let mut c = c as isize;

    let n = grid.len() as isize;
    let m = grid.len() as isize;
    for ch in instrs.chars() {
        (r, c) = match ch {  
            'U' => step(grid, r, c, -1, 0),
            'D' => step(grid, r, c, 1, 0),
            'L' => step(grid, r, c, 0, -1),
            'R' => step(grid, r, c, 0, 1),
            _   => panic!(),
        };
    }
    return (r as usize, c as usize);
}

fn solve(grid: &Vec<Vec<char>>, mut r: usize, mut c: usize, instructions: &Vec<String>) -> String {
    let mut res = Vec::new();

    for instr in instructions {
        (r, c) = steps(grid, r, c, &instr);
        res.push(format!("{}", grid[r][c]));
    }
    return res.join("");
}

fn main() -> io::Result<()> {
    let stdin = io::stdin();
    let instructions = stdin
        .lock()
        .lines()
        .collect::<io::Result<Vec<_>>>()?;

    // p1
    let mut grid_p1 = vec![
        vec!['1', '2', '3'],
        vec!['4', '5', '6'],
        vec!['7', '8', '9']
    ];
    println!("{}", solve(&grid_p1, 1, 1, &instructions));

    // p2
    let mut grid_p2 = vec![
        vec!['#','#','1','#','#'],
        vec!['#','2','3','4','#'],
        vec!['5','6','7','8','9'],
        vec!['#','A','B','C','#'],
        vec!['#','#','D','#','#'],
    ];
    println!("{}", solve(&grid_p2, 2, 0, &instructions));


    Ok(())
}
