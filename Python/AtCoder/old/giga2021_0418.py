def main():
    r_end, c_end, k, v = map(int, input().split())
    # 累積和は0_indexed
    r_end += 1
    c_end += 1
    grid = []
    grid.append([0]*c_end)
    for _ in range(r_end-1):
        row = [0] + list(map(int, input().split()))
        grid.append(row)

    # 累積和を取る
    for r in range(1, r_end):
        for c in range(1, c_end):
            grid[r][c] += grid[r][c-1]

    for r in range(1, r_end):
        for c in range(1, c_end):
            grid[r][c] += grid[r-1][c]

    def calc_size(r0, r1, c0, c1):
        w = c1 - c0
        h = r1 - r0
        return w*h

    def calc_cost(r0, r1, c0, c1):
        # (r0, r1], (c0, c1] で算出したコストを返す
        size = calc_size(r0, r1, c0, c1)
        grid_sum = grid[r1][c1] - grid[r1][c0] - grid[r0][c1] + grid[r0][c0]
        cost = (size * k) + grid_sum
        return cost

    ans = 0
    for r0 in range(r_end):
        for r1 in range(r0+1, r_end):
            for c0 in range(c_end):
                for c1 in range(c0+1, c_end):
                    cost = calc_cost(r0, r1, c0, c1)
                    if cost > v:
                        break
                    ans = max(ans, calc_size(r0, r1, c0, c1))

    print(ans)


main()
