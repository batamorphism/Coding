import heapq as hp


def main():
    r_end, c_end, h1, w1, h2, w2 = map(int, input().split())
    h2 = min(h2, h1)
    w2 = min(w2, w1)

    # 1-indexedにする
    r_end += 1
    c_end += 1
    grid = [[0] * (c_end) for _ in range(r_end)]
    for r in range(1, r_end):
        A = list(map(int, input().split()))
        for c_, a in enumerate(A):
            c = c_ + 1
            grid[r][c] = a

    # 累積和を求める
    for r in range(1, r_end):
        for c in range(1, c_end):
            grid[r][c] += grid[r][c-1]

    for r in range(1, r_end):
        for c in range(1, c_end):
            grid[r][c] += grid[r-1][c]

    def getsum(rc1, rc2):
        # [(r1, c1), (r2, c2)]の部分和を求める
        r1, c1 = rc1
        r2, c2 = rc2
        r1 -= 1
        c1 -= 1
        return grid[r2][c2] - grid[r1][c2] - grid[r2][c1] + grid[r1][c1]

    # [(r, c), (r+h1-1, c+w1-1)]の合計
    Aoki_Score = [[0]*c_end for _ in range(r_end)]
    # [(r, c), (r+h2-1, c+w2-1)]の合計
    # その後、縦にh1-h2+1個のスライド最大値
    # 　　　　横にw1-w2+1個のスライド最大値にする
    Taka_Score = [[0]*c_end for _ in range(r_end)]
    for r in range(1, r_end):
        for c in range(1, c_end):
            ra, ca = min(r+h1-1, r_end-1), min(c+w1-1, c_end-1)
            rt, ct = min(r+h2-1, r_end-1), min(c+w2-1, c_end-1)
            Aoki_Score[r][c] = getsum((r, c), (ra, ca))
            Taka_Score[r][c] = getsum((r, c), (rt, ct))

    # スライド最大値
    for r in range(r_end-1, -1, -1):
        que = []
        k = w1-w2+1
        for c in range(c_end-1, -1, -1):
            # [le, ri]
            le = c
            ri = min(le+k-1, c_end-1)
            hp.heappush(que, (-Taka_Score[r][c], le))
            while que[0][1] > ri:
                hp.heappop(que)
            Taka_Score[r][c] = -que[0][0]

    for c in range(c_end-1, -1, -1):
        que = []
        k = h1-h2+1
        for r in range(r_end-1, -1, -1):
            # [le, ri]
            le = r
            ri = min(le+k-1, r_end-1)
            hp.heappush(que, (-Taka_Score[r][c], le))
            while que[0][1] > ri:
                hp.heappop(que)
            Taka_Score[r][c] = -que[0][0]

    ans = 0
    for r in range(1, r_end):
        for c in range(1, c_end):
            ans = max(ans, Aoki_Score[r][c] - Taka_Score[r][c])
    print(ans)


main()
