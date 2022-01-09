from itertools import product


# 斜めに塗られる
# (r-a) = (c-b)もしくは
# (r-a) = -(c-b)のマスが塗られる
def main():
    n, a, b = map(int, input().split())
    r_0, r_1, c_0, c_1 = map(int, input().split())

    r_1 += 1
    c_1 += 1
    r_end = r_1 - r_0
    c_end = c_1 - c_0
    grid = [['.']*(c_end) for _ in range(r_end)]

    def is_black(r, c, a, b):
        if (r-a) == (c-b):
            return True
        if (r-a) == -(c-b):
            return True
        return False

    for r, c in product(range(r_0, r_1), range(c_0, c_1)):
        if is_black(r, c, a, b):
            grid[r-r_0][c-c_0] = '#'

    for row in grid:
        print(''.join(row))


main()
