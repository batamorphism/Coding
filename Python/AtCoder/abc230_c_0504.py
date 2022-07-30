def main():
    N, A, B = map(int, input().split())
    P, Q, R, S = map(int, input().split())
    r_end = Q-P+1
    c_end = S-R+1
    grid = [['.']*c_end for _ in range(r_end)]

    # a+k, b+kを黒く塗る
    # r = a+k and c = b+kは
    # r-c=a-bと同値
    # a+k, b-kは
    # r+c = a+bと同値

    for r in range(r_end):
        for c in range(c_end):
            fix_r = r+P
            fix_c = c+R
            if fix_r-fix_c == A-B:
                grid[r][c] = '#'
            if fix_r+fix_c == A+B:
                grid[r][c] = '#'

    for row in grid:
        print(''.join(row))


main()
