# 貪欲
def main():
    r_end, c_end = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(r_end)]
    aft_grid = [list(map(int, input().split())) for _ in range(r_end)]

    # gridを操作して、aft_gridにする
    def update(grid, aft_grid, r, c):
        # gridのr, cを更新し、aft_gridに揃え、必要な更新回数を返す
        if r == r_end -1 or c == c_end-1:
            return 0
        bef_val = grid[r][c]
        aft_val = aft_grid[r][c]
        del_val = aft_val - bef_val
        grid[r][c] += del_val
        grid[r][c+1] += del_val
        grid[r+1][c] += del_val
        grid[r+1][c+1] += del_val
        return abs(del_val)

    ans = 0
    for r in range(r_end-1):
        for c in range(c_end-1):
            ans += update(grid, aft_grid, r, c)

    if grid == aft_grid:
        print('Yes')
        print(ans)
    else:
        print('No')


main()
