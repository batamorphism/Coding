# p_i <= le <= ri <= q_i
# を満たすle, riの組み合わせ数を数える
# le <= ri墓ならず満たすため
# p_i <= le, ri <= q_iでよい
# 二次元累積和

def main():
    n, m, q = map(int, input().split())
    # 累積和は1-indexed
    r_end = n+1
    c_end = n+1
    accum = [[0]*r_end for _ in range(c_end)]

    for _ in range(m):
        le, ri = map(int, input().split())
        accum[le][ri] += 1

    query_list = []
    for _ in range(q):
        p, q = map(int, input().split())
        query_list.append((p, q))

    # 累積和にする
    for r in range(1, r_end):
        for c in range(1, c_end):
            accum[r][c] += accum[r][c-1]

    for r in range(1, r_end):
        for c in range(1, c_end):
            accum[r][c] += accum[r-1][c]

    def getsum(r1, c1, r2, c2):
        # [(r1, c1), (r2, c2)]の累積和を返す
        return accum[r2][c2] - accum[r2][c1-1] - accum[r1-1][c2] + accum[r1-1][c1-1]

    for p, q in query_list:
        ans = getsum(p, p, q, q)
        print(ans)


main()
