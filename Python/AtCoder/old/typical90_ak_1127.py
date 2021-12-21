INF = 10**9*500+1


class SegTree:
    def __init__(self, n_):
        self.seg_max = 1
        while self.seg_max < n_:
            self.seg_max *= 2
        self.data = [-INF]*(self.seg_max*2)

    def query(self, le, ri):
        # [le, ri)の最大値を返す
        ret = -INF
        le += self.seg_max
        ri += self.seg_max
        while le < ri:
            if le & 1:
                ret = max(ret, self.data[le])
                le += 1
            le >>= 1
            if ri & 1:
                ri -= 1
                ret = max(ret, self.data[ri])
            ri >>= 1
        return ret

    def update(self, pos, val):
        pos += self.seg_max
        self.data[pos] = val
        pos >>= 1
        while pos > 0:
            self.data[pos] = max(self.data[pos*2], self.data[pos*2+1])
            pos >>= 1


def main():
    W, N = map(int, input().split())
    # 1-indexed
    item_list = [(-1, -1, -1)]
    for _ in range(N):
        lo_i, hi_i, v_i = map(int, input().split())
        item_list.append((lo_i, hi_i, v_i))

    seg_tree = SegTree(W+1)
    seg_tree.update(0, 0)
    for i in range(1, N+1):
        lo_i, hi_i, v_i = item_list[i]
        for w in range(W, -1, -1):
            dp1 = seg_tree.query(w, w+1)
            # max(DP[i-1][w-hi_i] + v_i, ..., DP[i-1][w-lo_i] + v_i)を求めたい
            dp2 = -INF
            w_lo = max(w-hi_i, 0)
            w_hi = w-lo_i
            if w_hi >= 0:
                dp2 = seg_tree.query(w_lo, w_hi+1)
            dp = max(dp1, dp2+v_i)
            # print(i, w, dp1, dp2, dp2+v_i, dp)
            seg_tree.update(w, dp)

    ans = seg_tree.query(W, W+1)
    if ans < 0:
        ans = -1
    print(ans)


main()
