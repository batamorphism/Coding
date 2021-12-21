# rに身長
# rに体重のテーブルを考え
# table[r][c] = 体重r, 身長cの人数
# tableのうち、[r, c]～[r+k, c+k]の部分和が最大となるr, cを求める
# r, cの組み合わせ数は5000**2 = 25000000なので間に合う

def main():
    n, k = map(int, input().split())
    r_end = c_end = 5001
    Table = [[0]*c_end for _ in range(r_end)]
    for _ in range(n):
        r, c = map(int, input().split())
        Table[r][c] += 1

    cumsum = [[0]*c_end for _ in range(r_end)]
    # cumsum[r][c] = Table[r][c]までの合計
    for r in range(r_end):
        for c in range(c_end):
            if r == 0 or c == 0:
                continue
            cumsum[r][c] = cumsum[r-1][c] + cumsum[r][c-1] + Table[r][c] - cumsum[r-1][c-1]

    ans = 0
    for r0 in range(1, r_end):
        for c0 in range(1, c_end):
            r1 = r0 + k
            c1 = c0 + k
            if r1 >= r_end or c1 >= c_end:
                continue
            sum_range = cumsum[r1][c1] - cumsum[r1][c0-1] - cumsum[r0-1][c1] + cumsum[r0-1][c0-1]
            ans = max(sum_range, ans)

    print(ans)


main()
