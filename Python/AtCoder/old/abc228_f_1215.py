import heapq as hp


def main():
    r_end, c_end, t_h, t_w, a_h, a_w = map(int, input().split())
    a_h = min(a_h, t_h)
    a_w = min(a_w, t_w)

    # 累積和は1-indexed
    r_end += 1
    c_end += 1
    A = [[0]*c_end]
    for r in range(1, r_end):
        row = [0] + list(map(int, input().split()))
        A.append(row)

    # 累積和を計算
    for r in range(1, r_end):
        for c in range(1, c_end):
            A[r][c] += A[r][c-1]
    for r in range(1, r_end):
        for c in range(1, c_end):
            A[r][c] += A[r-1][c]

    def getsum(r0, c0, r1, c1):
        return A[r1][c1] - A[r1][c0-1] - A[r0-1][c1] + A[r0-1][c0-1]

    # (r, c)にスタンプを打った時の高橋君のスコアを求める
    Taka_Score = [[0]*c_end for _ in range(r_end)]
    for r0 in range(1, r_end):
        for c0 in range(1, c_end):
            r1 = r0 + t_h - 1
            c1 = c0 + t_w - 1
            r1 = min(r1, r_end-1)
            c1 = min(c1, c_end-1)
            score = getsum(r0, c0, r1, c1)
            Taka_Score[r0][c0] = score

    Aoki_Score = [[0]*c_end for _ in range(r_end)]
    # (r0, c0)にスタンプを打った時の青木君のスコアを求める
    for r0 in range(1, r_end):
        for c0 in range(1, c_end):
            r1 = r0 + a_h - 1
            c1 = c0 + a_w - 1
            r1 = min(r1, r_end-1)
            c1 = min(c1, c_end-1)
            score = getsum(r0, c0, r1, c1)
            Aoki_Score[r0][c0] = score

    # (r0, c0)に高橋君がスタンプを打った時、青木君のスコアの最大値はスライド最大値
    for r0 in range(r_end-1, 0, -1):
        que = []
        for c0 in range(c_end-1, 0, -1):
            le = c0
            ri_max = le + t_w - a_w
            a_le = -Aoki_Score[r0][c0]
            hp.heappush(que, (a_le, le))
            while not que[0][1] <= ri_max:
                hp.heappop(que)
            score = -que[0][0]
            Aoki_Score[r0][c0] = score
    for c0 in range(c_end-1, 0, -1):
        que = []
        for r0 in range(r_end-1, 0, -1):
            le = r0
            ri_max = le + t_h - a_h
            a_le = -Aoki_Score[r0][c0]
            hp.heappush(que, (a_le, le))
            while not que[0][1] <= ri_max:
                hp.heappop(que)
            score = -que[0][0]
            Aoki_Score[r0][c0] = score

    ans = 0
    for r0 in range(1, r_end):
        for c0 in range(1, c_end):
            score = Taka_Score[r0][c0] - Aoki_Score[r0][c0]
            ans = max(ans, score)

    print(ans)


main()
