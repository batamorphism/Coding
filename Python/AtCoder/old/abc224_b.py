def main():
    r_end, c_end = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(r_end)]
    ans = True
    for r1 in range(r_end):
        for r2 in range(r1, r_end):
            if r1 == r2:
                continue
            for c1 in range(c_end):
                for c2 in range(c1, c_end):
                    if c1 == c2:
                        continue
                    if not (A[r1][c1]+A[r2][c2] <= A[r1][c2]+A[r2][c1]):
                        ans = False
    if ans:
        print('Yes')
    else:
        print('No')


main()
