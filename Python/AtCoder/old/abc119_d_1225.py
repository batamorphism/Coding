class BIT:
    def __init__(self, n):
        self.bit_end = n+10
        self.bit_dat = [0] * self.bit_end

    def add(self, pos, val):
        pos += 1
        while pos < self.bit_end:
            self.bit_dat[pos] += val
            pos += (pos & -pos)

    def getsum(self, pos):
        ret = 0
        pos += 1
        while pos > 0:
            ret += self.bit_dat[pos]
            pos -= (pos & -pos)
        return ret


def main():
    a_end, b_end, q_end = map(int, input().split())
    A = [int(input()) for _ in range(a_end)]
    B = [int(input()) for _ in range(b_end)]
    Q = [int(input()) for _ in range(q_end)]

    ABQ = [0]+A+B+Q
    Zipper = {a: i for i, a in enumerate(sorted(set(ABQ)))}
    UnZipper = {i: a for i, a in enumerate(sorted(set(ABQ)))}

    A = [Zipper[a] for a in A]
    B = [Zipper[a] for a in B]
    Q = [Zipper[a] for a in Q]

    bit_end = len(ABQ) + 10
    A_bit = BIT(bit_end)
    B_bit = BIT(bit_end)
    for a in A:
        A_bit.add(a, 1)
    for b in B:
        B_bit.add(b, 1)

    INF = float('inf')
    for q in Q:
        # qに近いAとBを取ってきて、距離を求める
        # qより小さい最大のaとbをlo_a, lo_bとする
        q_unzip = UnZipper[q]
        a_cnt = A_bit.getsum(q)
        lo_a = bisect_lo(a_cnt, A_bit)
        hi_a = bisect_hi(a_cnt, A_bit)
        b_cnt = B_bit.getsum(q)
        lo_b = bisect_lo(b_cnt, B_bit)
        hi_b = bisect_hi(b_cnt, B_bit)
        lo_a_unzip = -INF
        lo_b_unzip = -INF
        hi_a_unzip = INF
        hi_b_unzip = INF
        if lo_a != -1:
            lo_a_unzip = UnZipper[lo_a]
        if lo_b != -1:
            lo_b_unzip = UnZipper[lo_b]
        if hi_a != -1:
            hi_a_unzip = UnZipper[hi_a]
        if hi_b != -1:
            hi_b_unzip = UnZipper[hi_b]
        ans = INF
        ans = min(ans, abs(min(lo_a_unzip, lo_b_unzip)-q_unzip))
        ans = min(ans, abs(max(hi_a_unzip, hi_b_unzip)-q_unzip))
        ans = min(ans, abs(lo_a_unzip - q_unzip) + abs(lo_a_unzip - hi_b_unzip))
        ans = min(ans, abs(hi_b_unzip - q_unzip) + abs(lo_a_unzip - hi_b_unzip))
        ans = min(ans, abs(lo_b_unzip - q_unzip) + abs(lo_b_unzip - hi_a_unzip))
        ans = min(ans, abs(hi_a_unzip - q_unzip) + abs(lo_b_unzip - hi_a_unzip))
        print(ans)


def bisect_lo(a_cnt, A_bit):
    ok = -1
    ng = A_bit.bit_end-1
    # ok < a_cntとなる最大のokを求める
    while (ng - ok) > 1:
        mid = (ok+ng)//2
        if A_bit.getsum(mid) < a_cnt:
            ok = mid
        else:
            ng = mid
    ok += 1
    if ok == 0:
        ok = -1
    return ok


def bisect_hi(a_cnt, A_bit):
    ok = -1
    ng = A_bit.bit_end-1
    # ok <= a_cntとなる最大のokを求める
    while (ng - ok) > 1:
        mid = (ok+ng)//2
        if A_bit.getsum(mid) <= a_cnt:
            ok = mid
        else:
            ng = mid
    ok += 1
    if ok == A_bit.bit_end-1:
        ok = -1
    return ok


main()
