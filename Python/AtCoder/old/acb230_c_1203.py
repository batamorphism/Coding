def main():
    n, a, b = map(int, input().split())
    p, q, r, s = map(int, input().split())

    # (a, b)からy=x方向に直線を引いたときに
    # r = c + x
    # a = b + x
    # x = a-b
    ans = []
    x = a-b
    col = r
    row = col + x
    while col <= s:
        ans.append((row, col))
        col += 1
        row = col + x

    # r = -c + x
    # a = -b + x
    # x = a+b
    x = a+b
    col = r
    row = -col + x
    while col <= s:
        ans.append((row, col))
        col += 1
        row = -col + x

    """
    grid = [['.'] * (s-r+1) for _ in range(q-p+1)]
    for x, y in ans:
        xx = x-p
        yy = y-r
        if (0 <= xx < len(grid) and 0 <= yy < len(grid[0])):
            grid[xx][yy] = '#'
    """

    grid = [['.'] * (s-r+1) for _ in range(q-p+1)]
    for row, col in ans:
        rr = row-p
        cc = col-r
        if (0 <= rr < len(grid) and 0 <= cc < len(grid[0])):
            grid[rr][cc] = '#'

    # print(ans)
    for g in grid:
        # print(g)
        print(''.join(g))


main()
