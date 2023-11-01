from sys import stdin
from collections import Counter

messages = [line[:-1] for line in stdin]

def solve(messages, k):
    n = len(messages[0])
    res = []
    for i in range(n):
        c = Counter(m[i] for m in messages)
        s = sorted((ch for ch in c), key = lambda x: c[x])
        res.append(s[k])
    return "".join(res)

# p1
print(solve(messages, -1))

# p2
print(solve(messages, 0))
