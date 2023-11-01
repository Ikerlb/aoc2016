import re
from sys import stdin

def is_abba(w):
    return len(w) == 4 and w[0] == w[-1] and w[1] == w[-2] and w[0] != w[1]

def parse(line):
    rx = r"\[[a-z0-9_]+\]"
    prev = 0
    outside = []
    inside = []
    for m in re.finditer(rx, line):
        s, e = m.span()
        outside.append(line[prev:s])
        inside.append(line[s + 1:e - 1])
        prev = e
    outside.append(line[prev:])
    return inside, outside
    

def windows(s, k):
    for i in range(0, len(s) - k + 1):
        yield s[i:i + k]

#def supports_tls(out1, hyper, out2):
#    for chunk in windows(hyper, 4):
#        if is_abba(chunk):
#            return False
#    for chunk in windows(out1, 4):
#        if is_abba(chunk):
#            return True
#    for chunk in windows(out2, 4):
#        if is_abba(chunk):
#            return True
#    return False

def is_aba(s):
    return len(s) == 3 and s[0] == s[-1] and s[1] != s[0]

def aba_compliment(s):
    return f"{s[1]}{s[0]}{s[1]}"

def supports_ssl(inside, outside):
    abas = set()
    for out in outside:
        abas |= {w for w in windows(out, 3) if is_aba(w)}
    for ins in inside:
        for w in windows(ins, 3):
            if is_aba(w) and aba_compliment(w) in abas:
                return True
    return False

def supports_tls(inside, outside):
    for ins in inside:
        if any(is_abba(w) for w in windows(ins, 4)):
            return False
    for out in outside:
        if any(is_abba(w) for w in windows(out, 4)):
            return True
    return False

def part1(ips):
    return sum(supports_tls(ins, out) for ins, out in ips)

def part2(ips):
    return sum(supports_ssl(ins, out) for ins, out in ips)

ips = [parse(line[:-1]) for line in stdin]

# p1
print(part1(ips))

# p2
print(part2(ips))
