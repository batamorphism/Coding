def main():
    r_end, c_end = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(r_end)]
    B = [[0]*c_end for _ in range(r_end)]

    sum_of_row = [0]*r_end
    sum_of_col = [0]*c_end

    for r in range(r_end):
        for c in range(c_end):
            val = A[r][c]
            sum_of_row[r] += val
            sum_of_col[c] += val

    for r in range(r_end):
        for c in range(c_end):
            val = sum_of_row[r] + sum_of_col[c] - A[r][c]
            B[r][c] = val

    for b in B:
        print(*b)


main()
