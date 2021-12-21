def main():
    r_end, c_end = map(int, input().split())
    grid = [tuple(map(int, input().split())) for _ in range(r_end)]

    all = 1 << r_end
    ans = 0
    for bit in range(1, all):
        sub_grid = []
        for r in range(r_end):
            if bit & (1 << r):
                sub_grid.append(grid[r])
            # sub_gridのうち、縦が全部同じ数になっている列の数を数える
        # print(cnt_same_col(sub_grid), bit)
        ans = max(ans, cnt_same_col(sub_grid))
    print(ans)


def cnt_same_col(grid):
    # 縦が全部同じ数だったら+1する
    ret = 0
    ret_of = {}
    ret_of[0] = 0
    # 転置する
    grid = list(zip(*grid))
    # 行が全部同じだったら、その数に+1する
    r_end = len(grid)
    c_end = len(grid[0])
    for r in range(r_end):
        row = grid[r]
        if len(set(row)) == 1:
            ret_of[row[0]] = ret_of.get(row[0], 0) + c_end
    ret_of_list = list(ret_of.values())
    ret = max(ret_of_list)
    return ret


main()
