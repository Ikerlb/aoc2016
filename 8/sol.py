from sys import stdin
import re
from itertools import product

width = 50
height = 6

def parse(line):
    op, rest = line.split(" ", 1)
    match op:
        case "rect":
            w, h = rest.split("x")
            return op, int(h), int(w)
        case "rotate":
            regex = r'(column x|row y)=(\d+) by (\d+)'
            orient, n, by = re.findall(regex, rest).pop()
            return f'rotate_{orient.split(" ")[0]}', int(n), int(by)
        case other:
            return None

# mutates grid
def rotate_row(grid, row, k):
    arr = grid[row]
    rem = n = len(arr)
    i = 0
    while rem and i < n:
        start = i
        prev = arr[i]
        while True:
            ni = (i + k) % n
            prev, arr[ni] = arr[ni], prev
            i = ni
            rem -= 1
            if ni == start:
                break
        i += 1

# mutates grid
def rotate_column(grid, col, k):
    rem = n = len(grid)
    i = 0
    while rem and i < n:
        start = i
        prev = grid[i][col]
        while True:
            ni = (i + k) % n
            prev, grid[ni][col] = grid[ni][col], prev
            i = ni
            rem -= 1
            if ni == start:
                break
        i += 1


# mutates grid
def step(grid, instr):
    match instr:
        case ("rect", rows, cols):
            for r, c in product(range(rows), range(cols)):
                grid[r][c] = "#"
        case ("rotate_column", col, by):
            rotate_column(grid, col, by)
        case ("rotate_row", row, by):
            rotate_row(grid, row, by)
        case rest:
            print("error!")

def format(grid):
    return "\n".join("".join(row) for row in grid)

# mutates grid
def execute(grid, instructions):
    for instr in instructions:
        step(grid, instr)
    return grid

instructions = [parse(line[:-1]) for line in stdin]
grid = [["." for _ in range(width)] for _ in range(height)]
res = execute(grid, instructions)

# p1
print(sum(sum(1 for c in row if c == "#") for row in grid))

# p2
print(format(grid))
