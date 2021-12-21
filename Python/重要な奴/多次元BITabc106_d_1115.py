class BIT:
    def __init__(self, bit_end):
        self.bit_end = bit_end+1
        self.data = [0] * (self.bit_end)

    def add(self, pos, val):
        pos += 1
        while pos < self.bit_end:
            self.data[pos] += val
            pos += pos & -pos

    def get_sum(self, pos):
        ret = 0
        pos += 1
        while pos > 0:
            ret += self.data[pos]
            pos -= pos & -pos
        return ret


class BIT2D:
    def __init__(self, r_end, c_end):
        self.bit_end = r_end+1
        self.data = [BIT(c_end+1) for _ in range(r_end+1)]

    def add(self, r, c, val):
        r += 1
        while r < self.bit_end:
            self.data[r].add(c, val)
            r += r & -r

    def get_sum(self, r, c):
        ret = 0
        r += 1
        while r > 0:
            ret += self.data[r].get_sum(c)
            r -= r & -r
        return ret


def main():
    n, m, q = map(int, input().split())
    bit2d = BIT2D(n+1, n+1)
    for _ in range(m):
        le, ri = map(int, input().split())
        bit2d.add(le, ri, 1)

    ans_list = []

    for _ in range(q):
        p, q = map(int, input().split())
        ans = bit2d.get_sum(q, q) - bit2d.get_sum(p-1, q) - bit2d.get_sum(q, p-1) + bit2d.get_sum(p-1, p-1)
        ans_list.append(ans)

    print(*ans_list, sep='\n')


main()
