def main():
    r_end, c_end, r1, c1, r2, c2 = map(int, input().split())
    A = [[-1] + list(map(int, input().split())) for _ in range(r_end)]
    # 1-indexed
    r_end += 1
    c_end += 1
    A = [[-1]*c_end] + A
    print(A)

    # Aの二次元累積和SUMを作成
    SUM = [[0]*c_end for _ in range(r_end)]
    for r in range(1, r_end):
        for c in range(1, c_end):
            SUM[r][c] = A[r][c] + SUM[r-1][c] + SUM[r][c-1] - SUM[r-1][c-1]

    # 高橋君、青木君がスタンプで塗りつぶす長方形内のAの総和
    Taka = [[0]*c_end for _ in range(r_end)]
    Aoki = [[0]*c_end for _ in range(r_end)]
    for r in range(1, r_end):
        for c in range(1, c_end):
            rr = min(r+r1, r_end)
            cc = min(c+c1, c_end)
            Taka[r][c] = SUM[rr][cc] - SUM[r][cc] - SUM[rr][c] + SUM[r][c]

    for r in range(1, r_end):
        for c in range(1, c_end):
            rr = min(r+r2, r_end)
            cc = min(c+c2, c_end)
            Aoki[r][c] = SUM[rr][cc] - SUM[r][cc] - SUM[rr][c] + SUM[r][c]

main()
