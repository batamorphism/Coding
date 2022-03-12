# [L, R] in [p, q]となる数
# (L, R)に点を打つ
# (p, p) ~ (q, q)の矩形区間に点が入っているとき
# p <= L <= q and p <= R <= qで題意を満たす
def main():
    n, m, q = map(int, input().split())
    rc_end = 510
    grid = [[0]*rc_end for _ in range(rc_end)]

    # 累積和は1-indexed
    for _ in range(m):
        le, ri = map(int, input().split())
        grid[le][ri] += 1

    for r in range(1, rc_end):
        for c in range(1, rc_end):
            grid[r][c] += grid[r-1][c]

    for r in range(1, rc_end):
        for c in range(1, rc_end):
            grid[r][c] += grid[r][c-1]

    ans_list = []
    for _ in range(q):
        p, q = map(int, input().split())
        p -= 1
        ans = grid[q][q] - grid[q][p] - grid[p][q] + grid[p][p]
        ans_list.append(ans)

    print(*ans_list, sep='\n')


main()
