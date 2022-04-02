class SegTree:

    def __init__(self, n):
        self.node_end = 1
        # 2のべき乗にする
        while self.node_end < n+1:
            self.node_end *= 2

        self.INF = (10**9*+1)*501
        self.tree = [-self.INF] * (2 * self.node_end)

    def query(self, le, ri):
        # [le, ri)の最大値を求める
        le += 1
        ri += 1

        # 足した先は0-indexed
        le += self.node_end
        ri += self.node_end
        ans = -self.INF
        while le < ri:
            if le % 2 == 1:
                ans = max(ans, self.tree[le])
                le += 1
            le //= 2

            if ri % 2 == 1:
                ri -= 1
                ans = max(ans, self.tree[ri])
            ri //= 2
        return ans

    def update(self, pos, val):
        pos += 1
        pos += self.node_end
        while pos >= 1:
            self.tree[pos] = max(self.tree[pos], val)
            pos //= 2


# セグ木
def main():
    max_w, n = map(int, input().split())

    item_list = []
    for _ in range(n):
        le, ri, val = map(int, input().split())
        item_list.append((le, ri, val))

    # DP[w] = 合計の重さがwの時の最大の価値
    sg = SegTree(max_w+1)
    sg.update(0, 0)
    # DP = [-INF]*(max_w+1)
    # DP[0] = 0
    for le, ri, val in item_list:
        # 貰うDP
        for cur_w in reversed(range(max_w+1)):
            # [cur_w-ri, cur_w-le]から貰う
            max_pre_w = sg.query(max(cur_w-ri, 0), min(cur_w-le, max_w)+1)
            sg.update(cur_w, max_pre_w+val)
            """
            max_pre_w = -INF
            for pre_w in range(max(cur_w-ri, 0), min(cur_w-le, max_w)+1):
                max_pre_w = max(max_pre_w, DP[pre_w] + val)
            DP[cur_w] = max(DP[cur_w], max_pre_w)
            """

    # ans = DP[max_w]
    ans = sg.query(max_w, max_w+1)
    if ans < 0:
        ans = -1
    print(ans)


main()
