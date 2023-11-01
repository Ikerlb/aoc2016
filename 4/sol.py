import re
from sys import stdin
from collections import defaultdict

def sort_by_frequency(name):
    count = defaultdict(int)
    for w in name.split("-"):
        for c in w:
            count[c] += 1
    
    return [c for _, c in sorted((-f, c) for c, f in count.items())[:5]]

def parse(line):
    regex = r"(.+)-(\d+)\[(.+)\]"
    res = re.search(regex, line)
    names, s_id, checksum = res.groups()
    return names, int(s_id), checksum

def part1(lines):
    res = 0
    for name, sid, checksum in lines:
        sbf = "".join(sort_by_frequency(name))
        res += sid if sbf == checksum else 0
    return res

def num(c):
    return ord(c) - ord('a')

def rotate(name, k):
    res = []
    for w in name.split("-"):
        res.append("".join(chr(((num(c) + k) % 26) + ord('a')) for c in w))
    return " ".join(res)

def part2(lines):
    for name, sid, _ in lines:
        if rotate(name, sid).startswith("northpole"):
            return sid

lines = [parse(line[:-1]) for line in stdin]

# p1
print(part1(lines))

# p2
print(part2(lines))
