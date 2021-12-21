# 二次元imos
def main():
    n = int(input())
    r_end = 1010
    c_end = 1010
    A = [[0] * c_end for _ in range(r_end)]

    for _ in range(n):
        lox, loy, hix, hiy = map(int, input().split())
        lox += 1
        loy += 1
        hix += 1
        hiy += 1
        A[lox][loy] += 1
        A[hix][hiy] += 1
        A[lox][hiy] -= 1
        A[hix][loy] -= 1

    for r in range(1, r_end):
        for c in range(1, c_end):
            A[r][c] += A[r][c-1]

    for c in range(1, c_end):
        for r in range(1, r_end):
            A[r][c] += A[r-1][c]

    cnt_of = [0]*(n+1)
    for c in range(1, c_end):
        for r in range(1, r_end):
            cnt_of[A[r][c]] += 1

    for i in range(1, n+1):
        print(cnt_of[i])


main()
