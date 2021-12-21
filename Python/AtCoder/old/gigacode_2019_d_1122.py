def main():
    r_end, c_end, k, v = map(int, input().split())
    # 累積和は1-indexed
    r_end += 1
    c_end += 1

    A = [[0] * c_end for _ in range(r_end)]
    for r in range(1, r_end):
        row = list(map(int, input().split()))
        for c in range(1, c_end):
            A[r][c] = row[c-1]

    # Aを累積和に
    for r in range(1, r_end):
        for c in range(1, c_end):
            A[r][c] += A[r-1][c]

    for r in range(1, r_end):
        for c in range(1, c_end):
            A[r][c] += A[r][c-1]

    def getsum(r1, c1, r2, c2):
        # [(r1, c1), (r2, c2)]の区間の累積和を返す
        r1 -= 1
        c1 -= 1
        return A[r2][c2] - A[r2][c1] - A[r1][c2] + A[r1][c1]

    def getmes(r1, c1, r2, c2):
        r1 -= 1
        c1 -= 1
        return (r2-r1) * (c2-c1)

    def getcost(r1, c1, r2, c2):
        # [(r1, c1), (r2, c2)]の区間のコストを返す
        s = getmes(r1, c1, r2, c2)
        return s*k+getsum(r1, c1, r2, c2)

    ans = 0
    for r1 in range(1, r_end):
        for c1 in range(1, c_end):
            for r2 in range(r1, r_end):
                for c2 in range(c1, c_end):
                    cost = getcost(r1, c1, r2, c2)
                    if cost <= v:
                        ans = max(ans, getmes(r1, c1, r2, c2))

    print(ans)


main()
