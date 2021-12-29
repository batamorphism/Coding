# セグメント木
class SegTree:
    def __init__(self, n):
        self.seg_size = 1
        while self.seg_size <= n:
            self.seg_size <<= 1
        # self.INF = float('inf')
        self.INF = 10**9*500 + 10
        self.seg_tree = [-self.INF]*(2*self.seg_size)

    def update(self, pos, val):
        # pos は 0-indexed
        pos += self.seg_size
        self.seg_tree[pos] = val
        pos >>= 1
        while pos > 0:
            chi_le = pos << 1
            chi_ri = chi_le + 1
            self.seg_tree[pos] = max(self.seg_tree[chi_le], self.seg_tree[chi_ri])
            pos >>= 1

    def query(self, le, ri):
        # [le, ri)の最大値
        le += self.seg_size
        ri += self.seg_size
        ret = -self.INF
        while le < ri:
            if le & 1:
                ret = max(ret, self.seg_tree[le])
                le += 1
            le >>= 1
            if ri & 1:
                ri -= 1
                ret = max(ret, self.seg_tree[ri])
            ri >>= 1
        return ret


def main():
    w_max, n = map(int, input().split())
    w_end = w_max + 1

    seg_tree = SegTree(w_end+10)
    seg_tree.update(0, 0)
    for _ in range(n):
        lo, hi, v = map(int, input().split())
        for w in range(w_end-1, -1, -1):
            # dp1 = DP[i-1][w]
            dp1 = seg_tree.query(w, w+1)
            dp2 = seg_tree.query(max(w-hi, 0), max(w-lo+1, 0)) + v
            dp = max(dp1, dp2)
            seg_tree.update(w, dp)

    ans = seg_tree.query(w_end-1, w_end)
    if ans < 0:
        ans = -1
    print(ans)


main()
