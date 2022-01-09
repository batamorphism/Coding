import sys
sys.setrecursionlimit(10**6)


class LazySegTree:
    # 1-indexedのseg_tree
    def __init__(self, n):
        self.seg_max = 1
        while self.seg_max < n:
            self.seg_max <<= 2
        self.seg = [0]*(2*self.seg_max)
        self.laz = [-1]*(2*self.seg_max)

    def update(self, le, ri, val):
        # [le, ri)をvalで更新
        self._sub_update(le, ri, val, 1, 0, self.seg_max)

    def _sub_update(self, le, ri, val, cur_node, cur_le, cur_ri):
        self._eval(cur_node)
        if le <= cur_le and cur_ri <= ri:
            # 完全に内側の時
            self.laz[cur_node] = val
            self._eval(cur_node)
            return
        elif cur_ri <= le or ri <= cur_le:
            # 完全にはみ出しているとき
            return
        else:
            # 一部が内側の時
            mid = (cur_le+cur_ri)//2
            self._sub_update(le, ri, val, 2*cur_node, cur_le, mid)
            self._sub_update(le, ri, val, 2*cur_node+1, mid, cur_ri)
            self.seg[cur_node] = max(self.seg[2*cur_node], self.seg[2*cur_node+1])
            return

    def _eval(self, node):
        # 遅延評価
        # 親から子に伝播
        if self.laz[node] == -1:
            return

        if node*2+1 < 2*self.seg_max:
            self.laz[node*2] = self.laz[node]
            self.laz[node*2+1] = self.laz[node]
        self.seg[node] = self.laz[node]
        self.laz[node] = -1

    def query(self, le, ri):
        # [a, b)の最大値を返す
        return self._sub_query(le, ri, 1, 0, self.seg_max)

    def _sub_query(self, le, ri, cur_node, cur_le, cur_ri):
        self._eval(cur_node)
        if le <= cur_le and cur_ri <= ri:
            # 完全の内側の時
            return self.seg[cur_node]
        elif cur_ri <= le or ri <= cur_le:
            # 完全にはみ出しているとき
            return -1
        else:
            mid = (cur_le+cur_ri)//2
            val_le = self._sub_query(le, ri, 2*cur_node, cur_le, mid)
            val_ri = self._sub_query(le, ri, 2*cur_node+1, mid, cur_ri)
            return max(val_le, val_ri)


def main():
    # [Li, Ri]のmaxを求めて、それをdpとして出力する
    # その後、[Li, Ri]をdp+1に更新する
    w, n = map(int, input().split())
    seg_tree = LazySegTree(w+1)
    ans_list = []
    for _ in range(n):
        le, ri = map(int, input().split())
        ri += 1
        # [le, ri)のmaxを求める
        dp = seg_tree.query(le, ri)
        dp += 1
        # print(le, ri, dp)
        ans_list.append(dp)
        seg_tree.update(le, ri, dp)

    print(*ans_list, sep='\n')


main()
