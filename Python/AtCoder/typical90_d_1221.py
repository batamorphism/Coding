def main():
    r_end, c_end = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(r_end)]

    sum_of_row = [0] * r_end
    sum_of_col = [0] * c_end

    for r in range(r_end):
        for c in range(c_end):
            sum_of_row[r] += A[r][c]
            sum_of_col[c] += A[r][c]

    ans_grid = [[0]*c_end for _ in range(r_end)]
    for r in range(r_end):
        for c in range(c_end):
            ans = sum_of_row[r] + sum_of_col[c] - A[r][c]
            ans_grid[r][c] = ans

    for ans in ans_grid:
        print(*ans)


main()
