from sys import stdin

def parse(line):
    for ss in line.split(" "):
        if not ss:
            continue
        yield int(ss)

def are_triangle(s1, s2, s3):
    if s1 + s2 <= s3:
        return False
    if s1 + s3 <= s2:
        return False
    if s3 + s2 <= s1:
        return False
    return True

def part1(triangles):
    return sum(1 for t in triangles if are_triangle(*t))

def chunks(arr, k):
    for i in range(0, len(arr), k):
        yield arr[i:i + k]

def part2(triangles, k):
    res = 0
    for i in range(k):
        for ch in chunks(triangles, k):
            res += are_triangle(*(c[i] for c in ch))
    return res

triangles = [tuple(parse(line[:-1])) for line in stdin]

# p1
print(part1(triangles))

# p1
print(part2(triangles, 3))
