# 遅延セグ木
class LazySegTree:
    INF = float('inf')

    def __init__(self, n):
        i = 1
        while i <= n:
            i *= 2
        self.node_end = i
        self.tree = [0] * (self.node_end * 2 + 1)
        self.lazy = [-1] * (self.node_end * 2 + 1)

    def _eval(self, node):
        # nodeを遅延評価
        if self.lazy[node] == -1:
            return
        self.tree[node] = self.lazy[node]
        if node < self.node_end:
            self.lazy[node * 2] = self.lazy[node]
            self.lazy[node * 2 + 1] = self.lazy[node]
        self.lazy[node] = -1

    def _update(self, le, ri, node, cur_le, cur_ri, val):
        # 区間[le, ri)をvalに更新
        self._eval(node)
        # [cur_le, cur_ri) in [le, ri)の場合は、更新ロジックに入る
        if le <= cur_le and cur_ri <= ri:
            self.lazy[node] = val
            self._eval(node)
            return
        # [cur_le, cur_ri) と[le, ri)に共通部分がない場合は、終了
        if cur_ri <= le or ri <= cur_le:
            return
        # 左側の区間
        nex_le = cur_le
        nex_ri = cur_le + (cur_ri - cur_le) // 2
        self._update(le, ri, node * 2, nex_le, nex_ri, val)
        # 右側の区間
        nex_le = cur_le + (cur_ri - cur_le) // 2
        nex_ri = cur_ri
        self._update(le, ri, node * 2 + 1, nex_le, nex_ri, val)
        self.tree[node] = max(self.tree[node * 2], self.tree[node * 2 + 1])

    def update(self, le, ri, val):
        head_node = 1
        self._update(le, ri, head_node, 0, self.node_end, val)

    def _query(self, le, ri, node, cur_le, cur_ri):
        # [le, ri) の最大値を求める
        ret = -self.INF
        self._eval(node)
        # [cur_le, cur_ri) in [le, ri)の場合は、値取得ロジックに入る
        if le <= cur_le and cur_ri <= ri:
            ret = max(ret, self.tree[node])
            return ret
        # [cur_le, cur_ri) と[le, ri)に共通部分がない場合は、終了
        if cur_ri <= le or ri <= cur_le:
            return ret
        # 左側の区間
        nex_le = cur_le
        nex_ri = cur_le + (cur_ri - cur_le) // 2
        ret_le = self._query(le, ri, node * 2, nex_le, nex_ri)
        # 右側の区間
        nex_le = cur_le + (cur_ri - cur_le) // 2
        nex_ri = cur_ri
        ret_ri = self._query(le, ri, node * 2 + 1, nex_le, nex_ri)
        ret = max(ret, ret_le, ret_ri)
        return ret

    def query(self, le, ri):
        head_node = 1
        return self._query(le, ri, head_node, 0, self.node_end)

    def debug(self):
        # 各nodeの値を全て出力
        for node in range(self.node_end):
            self._eval(node)
        dat = []
        for node in range(self.node_end):
            dat.append(self.tree[self.node_end+node])
        print(dat)


def main():
    w, n = map(int, input().split())
    seg_tree = LazySegTree(w)
    ans_list = []
    for i in range(n):
        le, ri = map(int, input().split())
        ri += 1
        ans = seg_tree.query(le, ri)
        seg_tree.update(le, ri, ans + 1)
        ans_list.append(ans+1)
    print(*ans_list)


main()
