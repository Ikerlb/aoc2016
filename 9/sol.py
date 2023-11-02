def decompress(s):
    n = len(s)
    buf = []
    res = []
    i = 0
    while i < n:
        c = s[i]
        if c == "(":
            j = i + 1
            while j < n and s[j] != ")":
                j += 1
            ss, times = map(int, s[i + 1:j].split("x"))
            ss_end = j + 1 + ss
            res.append("".join(buf))
            res.append("".join(s[j + 1:ss_end] * times))
            buf.clear()
            i = ss_end
        else:
            buf.append(c)
            i += 1
    res.append("".join(buf))
    return "".join(res)

class Node:
    def __init__(self, length, times):
        self.children = []
        self.length = length
        self.times = times

    def append(self, node):
        self.children.append(node)

    def __repr__(self):
        res = ",".join(f"{ch}" for ch in self.children)
        return f"({self.length}x{self.times}){res}"

    def __iter__(self):
        yield from self.children

# hope to god it doesn't overflow the stack
def parse(s, start, end, parent):
    n = len(s)
    i = start
    while i < end:
        c = s[i]
        if c == "(":
            j = i + 1
            while j < n and s[j] != ")":
                j += 1
            ss, times = map(int, s[i + 1:j].split("x"))
            ss_end = j + 1 + ss
            node = Node(ss, times)
            parse(s, j + 1, ss_end, node)
            parent.append(node)
            i = ss_end
        else:
            parent.append(1)
            i += 1

def dfs(node):
    if not node.children:
        return node.times * node.length
    s = 0
    for child in node.children:
        if type(child) is Node:
            r = dfs(child)
            s += node.times * r 
        else:
            s += node.times * child
    return s

def part1(s):
    return len(decompress(s))

def part2(s):
    parent = Node(-1, -1)
    parse(s, 0, len(s) - 1, parent)
    res = 0
    for child in parent:
        res += dfs(child) if type(child) is Node else child
    return res

s = input()
print(part1(s))
print(part2(s))
