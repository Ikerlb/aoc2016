from hashlib import md5

def next_character(k, door_id, start):
    i = start
    while True: 
        res = md5(bytes(f"{door_id}{i}", encoding = "ascii"))
        dig = res.digest().hex()
        i += 1
        if all(d == '0' for d in dig[:k]):
            return i, dig

def part1(door_id):
    res = []
    i = 0
    for _ in range(8):
        i, dig = next_character(5, door_id, i)
        res.append(dig[5])
    return "".join(res)

def parse_hex(h):
    if h in "01234567":
        return int(h)
    return -1

def part2(door_id):
    res = [None] * 8
    i = 0
    while any(r is None for r in res):
        i, dig = next_character(5, door_id, i)
        pos, val = parse_hex(dig[5]), dig[6]
        if pos > -1 and res[pos] is None:
            res[pos] = val
    return "".join(res)

door_id = input()

# p1
print(part1(door_id))

# p2
print(part2(door_id))
