from collections import Counter
import itertools

def main():
    n = int(input())
    r_end = 1002
    c_end = 1002
    grid = [[0]*c_end for _ in range(r_end)]

    for _ in range(n):
        le_x, le_y, ri_x, ri_y = map(int, input().split())
        le_x += 1
        le_y += 1
        ri_x += 1
        ri_y += 1
        grid[le_x][le_y] += 1
        grid[le_x][ri_y] -= 1
        grid[ri_x][le_y] -= 1
        grid[ri_x][ri_y] += 1

    # 2d-imos
    for r in range(1, r_end):
        for c in range(1, c_end):
            grid[r][c] += grid[r-1][c]
    for r in range(1, r_end):
        for c in range(1, c_end):
            grid[r][c] += grid[r][c-1]

    flat_arr = itertools.chain.from_iterable(grid)
    cnt_of = Counter(flat_arr)
    for k in range(1, n+1):
        print(cnt_of[k])


main()
