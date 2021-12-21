class LazySeg:
    def __init__(self, n):
        seg_max = 1
        while seg_max <= n:
            seg_max <<= 1
        self.seg_max = seg_max
        self.seg = [0] * (seg_max << 1)
        self.laz = [-1] * (seg_max << 1)

    def _eval(self, node):
        # laz[node]をsegに反映し、laz[child]に転記
        if self.laz[node] == -1:
            return
        self.seg[node] = self.laz[node]
        if node < self.seg_max:
            le = node << 1
            ri = le + 1
            self.laz[le] = self.laz[ri] = self.laz[node]
        self.laz[node] = -1

    def update(self, le, ri, val):
        # [le, ri)をvalに更新
        self._update(le, ri, val, 1, 0, self.seg_max)

    def _update(self, le, ri, val, cur_node, cur_le, cur_ri):
        self._eval(cur_node)
        if le <= cur_le <= cur_ri <= ri:
            # 完全に内側の時は更新
            self.laz[cur_node] = val
            self._eval(cur_node)
            return
        if cur_le >= ri or cur_ri <= le:
            # 範囲外の時は何もしない
            return
        # 一部引っかかっているとき
        mid = (cur_le+cur_ri) // 2
        le_node = cur_node << 1
        ri_node = le_node + 1
        self._update(le, ri, val, le_node, cur_le, mid)
        self._update(le, ri, val, ri_node, mid, cur_ri)
        self.seg[cur_node] = max(self.seg[le_node], self.seg[ri_node])
        return

    def query(self, le, ri):
        # [le, ri) の最大値を返す
        return self._query(le, ri, 1, 0, self.seg_max)

    def _query(self, le, ri, cur_node, cur_le, cur_ri):
        self._eval(cur_node)
        if cur_le >= ri or cur_ri <= le:
            # 範囲外の時は-1を返す
            return -1
        if le <= cur_le and cur_ri <= ri:
            # 完全に内側の時はsegの値を返す
            return self.seg[cur_node]
        # 一部引っかかっているとき
        mid = (cur_le+cur_ri) // 2
        le_node = cur_node << 1
        ri_node = le_node + 1
        le_ret = self._query(le, ri, le_node, cur_le, mid)
        ri_ret = self._query(le, ri, ri_node, mid, cur_ri)
        return max(le_ret, ri_ret)


def main():
    w, n = map(int, input().split())
    lazy = LazySeg(w+10)
    ans_list = []
    for _ in range(n):
        le, ri = map(int, input().split())
        ri += 1
        ans = lazy.query(le, ri) + 1
        lazy.update(le, ri, ans)
        ans_list.append(ans)

    print(*ans_list, sep='\n')


main()
