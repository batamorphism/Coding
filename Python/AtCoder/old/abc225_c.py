def main():
    n, m = map(int, input().split())
    B = [list(map(int, input().split())) for _ in range(n)]

    # 1行目について、7の倍数が右端以外に出てきてはならない
    row = B[0]
    for b in row[:-1]:
        if b % 7 == 0:
            print('No')
            return

    for r in range(n):
        for c in range(m):
            if r >= 1:
                if not (B[r][c] == B[r-1][c]+7):
                    print('No')
                    return
            if c >= 1:
                if not (B[r][c] == B[r][c-1]+1):
                    print('No')
                    return

    print('Yes')


main()
