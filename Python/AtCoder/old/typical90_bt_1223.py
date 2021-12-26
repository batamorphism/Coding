# バックトラック
from itertools import product
ans = -1


def main():
    r_end, c_end = map(int, input().split())
    # . -> 開いてる
    # # -> 通れない
    # * -> 通ったことがある
    grid = [list(input()) for _ in range(r_end)]

    def nei_of(grid_tup, pre_r, pre_c):
        drc = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        for dr, dc in drc:
            cur_r = pre_r + dr
            cur_c = pre_c + dc
            if not (0 <= cur_r < r_end and 0 <= cur_c < c_end):
                continue
            if not (grid_tup[cur_r][cur_c] == '.'):
                continue
            yield cur_r, cur_c

    def dfs(grid_tup, pre_cnt, pre_r, pre_c, st_r, st_c):
        global ans
        if pre_cnt >= 3 and pre_r == st_r and pre_c == st_c:
            ans = max(ans, pre_cnt)
            return
        cur_cnt = pre_cnt + 1
        for cur_r, cur_c in nei_of(grid_tup, pre_r, pre_c):
            cur_grid_list = tuple_to_list(grid_tup)
            cur_grid_list[cur_r][cur_c] = '*'
            cur_grid_tup = list_to_tuple(cur_grid_list)
            dfs(cur_grid_tup, cur_cnt, cur_r, cur_c, st_r, st_c)

    grid_tup = list_to_tuple(grid)
    for fr_r, fr_c in product(range(r_end), range(c_end)):
        if grid[fr_r][fr_c] == '.':
            dfs(grid_tup, 0, fr_r, fr_c, fr_r, fr_c)

    print(ans)


def list_to_tuple(grid):
    ret = []
    for row in grid:
        ret.append(tuple(row))
    ret = tuple(ret)
    return ret


def tuple_to_list(grid):
    ret = []
    for row in grid:
        ret.append(list(row))
    return ret


main()
