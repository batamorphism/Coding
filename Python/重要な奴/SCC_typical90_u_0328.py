class SCC:
    def __init__(self, node_end, nei_of):
        self.node_end = node_end
        self.nei_of = nei_of
        self.group = [-1] * node_end
        self.group_siz = [0] * node_end

        self._scc()

    def _scc(self):
        # 逆向きの辺を定義する
        rev_nei_of = [[] for _ in range(self.node_end)]
        for node in range(self.node_end):
            for nei in self.nei_of[node]:
                rev_nei_of[nei].append(node)

        # dfsの戻り掛けの順番を記録する
        order = []
        used = [False] * self.node_end

        def dfs1(node):
            # 非再帰dfs
            stk = []
            stk.append(~node)  # 帰りがけ
            stk.append(node)
            while stk:
                pre = stk.pop()
                if pre >= 0:  # 行きがけの処理
                    if used[pre]:
                        if stk[-1] != ~pre:
                            raise
                        stk.pop()
                        continue
                    used[pre] = True
                    for cur in self.nei_of[pre]:
                        stk.append(~cur)  # 帰りがけの処理を追加
                        stk.append(cur)  # 行きがけの処理を追加
                else:  # 帰りがけの処理
                    order.append(~pre)

        for node in range(self.node_end):
            if used[node]:
                continue
            dfs1(node)

        def dfs2(node):
            # 非再帰dfs
            stk = []
            stk.append(node)
            while stk:
                pre = stk.pop()
                if self.group[pre] >= 0:
                    continue
                self.group[pre] = node
                for cur in rev_nei_of[pre]:
                    stk.append(cur)  # 行きがけの処理を追加

        # 戻り掛けるのが遅かった順番、つまり中央に近いほうから
        # 逆向きのdfsをする
        for node in reversed(order):
            if self.group[node] >= 0:
                continue
            dfs2(node)

        # group_sizを計算
        for node in range(self.node_end):
            self.group_siz[self.group[node]] += 1

    def get_group(self, node):
        return self.group[node]

    def get_size(self, node):
        return self.group_siz[self.get_group(node)]


# SCC
def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]

    for _ in range(edge_end):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append(to)

    scc = SCC(node_end, nei_of)

    # 各グループの個数をカウントする
    cnt_of = [0] * node_end
    for node in range(node_end):
        cnt_of[scc.get_group(node)] = scc.get_size(node)

    ans = 0
    for cnt in cnt_of:
        ans += cnt * (cnt - 1) // 2

    print(ans)


main()
