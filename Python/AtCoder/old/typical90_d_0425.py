def main():
    r_end, c_end = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(r_end)]

    ans = [[0]*c_end for _ in range(r_end)]

    # sum_of_row[r] = r行目の総和
    sum_of_row = [0]*r_end
    sum_of_col = [0]*c_end

    # set sum_of
    for r in range(r_end):
        for c in range(c_end):
            a_rc = A[r][c]
            sum_of_row[r] += a_rc
            sum_of_col[c] += a_rc

    # calc ans
    for r in range(r_end):
        for c in range(c_end):
            ans[r][c] += sum_of_row[r]
            ans[r][c] += sum_of_col[c]
            ans[r][c] -= A[r][c]

    # print ans
    for r in range(r_end):
        print(*ans[r])


main()
