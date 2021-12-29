class UnionFind:
    """
    UnionFind
    同じグループに入るかの判定、およびグループがいくつあるかの判定
    各グループはグラフ（木）で表現する
    AとBとをまとめる=AとBの間に辺を張る
    同じグループに入るかの判定は、要素をさかのぼって根が同じかを見ればよい
    """

    def __init__(self, n):
        """
        n: 頂点数
        """
        self._node_end = n
        self._par = [i for i in range(n)]
        self._siz = [1 for i in range(n)]

    def find(self, x):
        """
        xの代表元を返す
        """
        if self._par[x] == x:
            return x
        self._par[x] = self.find(self._par[x])
        return self._par[x]

    def union(self, x, y):
        """
        xとyとを同じグループとしてみなす
        """
        # self._add_tree(x)
        # self._add_tree(y)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return

        # siz[x] <= siz[y]にする
        if self._siz[x] > self._siz[y]:
            x, y = y, x

        # サイズが大きいほうが親
        self._par[x] = y
        self._siz[y] += self._siz[x]

    def same(self, x, y):
        """
        xとyが同じグループかを比較する
        """
        return self.find(x) == self.find(y)

    # 以降、おまけ機能
    def members(self, x):
        """
        xと同じグループに属するメンバーをすべてリストで列挙する
        遅い
        """
        x = self.find(x)
        ret = []
        for node in range(self._node_end):
            if self.find(node) == x:
                ret.append(node)
        return ret

    def roots(self):
        """
        全ての連結成分の代表元をリストで返す
        遅い
        """
        ret = set()
        for node in range(self._node_end):
            root = self.find(node)
            ret.add(root)
        return list(ret)

    def count_groups(self):
        """
        グラフの連結成分の個数を返す
        遅い
        """
        return len(self.roots())

    def size(self, x):
        """
        xが属するグループの要素の数を返す
        """
        x = self.find(x)
        return self._siz[x]


def main():
    u = UnionFind(10)

    u.union(0, 1)
    u.union(0, 2)
    print(u.count_groups())
    print(u.same(0, 2))
    print(u.same(0, 3))
    print(u.members(0))
    print(u.members(3))


main()
