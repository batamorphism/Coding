import sys
sys.setrecursionlimit(10**6)


# 遅延セグ木
class LazySegTree:
    def __init__(self, n):
        self.seg_max = 1
        while self.seg_max < n:
            self.seg_max <<= 1
        self.data = [0] * (2 * self.seg_max)
        self.lazy = [-1] * (2 * self.seg_max)

    def _eval(self, node):
        # nodeにいるlazyを評価する
        val = self.lazy[node]
        if val == -1:
            return
        self.data[node] = val
        if node < self.seg_max:
            le = node << 1
            ri = le + 1
            self.lazy[le] = self.lazy[ri] = val
        self.lazy[node] = -1

    def query(self, le, ri):
        # [a, b)の最大値を返す
        return self._query(le, ri, 1, 0, self.seg_max)

    def _query(self, le, ri, node, node_le, node_ri):
        ret = -1
        self._eval(node)
        # [node_le, node_ri) in [le, ri)ならば、その値を返す
        if le <= node_le <= node_ri <= ri:
            return self.data[node]
        # [node_le, node_ri)が[le, ri)と重複がないならば、何もしない
        if node_le >= ri or node_ri <= le:
            return -1
        # それ以外は、部分的に重複している
        mid = (node_le + node_ri) >> 1
        child_le = node << 1
        child_ri = child_le + 1
        ret = self._query(le, ri, child_le, node_le, mid)
        ret = max(self._query(le, ri, child_ri, mid, node_ri), ret)
        return ret

    def update(self, le, ri, val):
        # [le, ri)をvalに更新する
        self._update(le, ri, val, 1, 0, self.seg_max)

    def _update(self, le, ri, val, node, node_le, node_ri):
        self._eval(node)
        # [node_le, node_ri) in [le, ri)ならば、その値を更新する
        if le <= node_le <= node_ri <= ri:
            self.lazy[node] = val
            self._eval(node)
            return
        # [node_le, node_ri)が[le, ri)と重複がないならば、何もしない
        if node_le >= ri or node_ri <= le:
            return
        # それ以外は、部分的に重複している
        mid = (node_le + node_ri) >> 1
        child_le = node << 1
        child_ri = child_le + 1
        self._update(le, ri, val, child_le, node_le, mid)
        self._update(le, ri, val, child_ri, mid, node_ri)
        self.data[node] = max(self.data[child_le], self.data[child_ri])


def main():
    w, n = map(int, input().split())
    query_list = []
    ri_max = 0
    for _ in range(n):
        le, ri = map(int, input().split())
        ri += 1
        query_list.append((le, ri))
        ri_max = max(ri_max, ri)

    seg_tree = LazySegTree(ri_max)

    for query in query_list:
        le, ri = query
        val = seg_tree.query(le, ri)
        print(val+1)
        seg_tree.update(le, ri, val+1)


main()
