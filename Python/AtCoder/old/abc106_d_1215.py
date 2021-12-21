# (l_i, r_i)に点を打つ
# p_i <= l_i <= r_i <= q_iは、
# (p_i, p_i) <= (l_i, r_i) <= (q_i, q_i)と同値

def main():
    n, m, q = map(int, input().split())
    grid = [[0]*(n+1) for _ in range(n+1)]

    for _ in range(m):
        l_i, r_i = map(int, input().split())
        grid[l_i][r_i] += 1

    # 累積和
    for r in range(n+1):
        for c in range(n+1):
            grid[r][c] += grid[r][c-1]
    for r in range(n+1):
        for c in range(n+1):
            grid[r][c] += grid[r-1][c]

    def getsum(r0, c0, r1, c1):
        return grid[r1][c1] - grid[r1][c0-1] - grid[r0-1][c1] + grid[r0-1][c0-1]

    ans_list = []
    for _ in range(q):
        p_i, q_i = map(int, input().split())
        ans = getsum(p_i, p_i, q_i, q_i)
        ans_list.append(ans)

    print(*ans_list, sep='\n')


main()
