# 2d_imos
# (r1, c1)に+1
# (r2, c2)に+1
# (r1, c2)に-1
# (r2, c1)に-1
def main():
    n = int(input())
    r_end = 1002
    c_end = 1002
    grid = [[0] * c_end for _ in range(r_end)]

    # 累積和は1-indexed
    for _ in range(n):
        r1, c1, r2, c2 = map(int, input().split())
        r1, c1, r2, c2 = r1+1, c1+1, r2+1, c2+1
        grid[r1][c1] += 1
        grid[r2][c2] += 1
        grid[r1][c2] -= 1
        grid[r2][c1] -= 1

    # 縦に横に
    for r in range(1, r_end):
        for c in range(1, c_end):
            grid[r][c] += grid[r-1][c]

    for r in range(1, r_end):
        for c in range(1, c_end):
            grid[r][c] += grid[r][c-1]

    cnt_of = [0]*(n+1)
    for r in range(r_end):
        for c in range(c_end):
            cnt_of[grid[r][c]] += 1

    for cnt in cnt_of[1:]:
        print(cnt)


main()
