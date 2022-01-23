from collections import deque


# 身長をrに
# 体重をcに編集する
# 幅kの累積和の最大値が答え
def main():
    n, k = map(int, input().split())
    r_end = 5002
    c_end = 5002
    grid = [[0]*c_end for _ in range(r_end)]
    for _ in range(n):
        a, b = map(int, input().split())
        grid[a][b] += 1

    # 横に累積和
    for r in range(1, r_end):
        for c in range(1, c_end):
            grid[r][c] += grid[r][c-1]

    for r in range(1, r_end):
        for c in range(1, c_end):
            grid[r][c] += grid[r-1][c]

    ans = -1
    for r0 in range(1, r_end):
        for c0 in range(1, c_end):
            r1 = min(r0 + k, r_end-1)
            c1 = min(c0 + k, c_end-1)
            val = grid[r1][c1] - grid[r1][c0-1] - grid[r0-1][c1] + grid[r0-1][c0-1]
            ans = max(ans, val)

    print(ans)


main()
