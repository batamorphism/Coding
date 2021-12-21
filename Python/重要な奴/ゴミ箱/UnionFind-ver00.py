class UnionFind:
    """
    UnionFind
    同じグループに入るかの判定、およびグループがいくつあるかの判定
    各グループはグラフ（木）で表現する
    AとBとをまとめる=AとBの間に辺を張る
    同じグループに入るかの判定は、要素をさかのぼって根が同じかを見ればよい

    経路圧縮：上向きにさかのぼって再帰的に値を調べる際に、調べたら辺を根に直接つなぎなおす
    1-2-3-4 という枝があった場合、4の根を調べる(root(4)を実行する）と、
    1
    ├2
    ├3
    └4という枝に貼りなおす
    ただし、unionするときは特段つなぎ直さない為、root関数を実行しない限りは、経路圧縮されない

    ランク:木の高さをもっておき、低いほうを高いほうにつなげる
    こうすることで、rootで再帰する回数を極力少なくできる

    union(x, y):xとyを要素に加えつつ、xとyを同じ要素とみなす
    union(x, x)で単純に要素を追加することも可

    is_same(x, y):xとyが同じ要素かを判定する

    count_groups():グループの数を数え上げる
    members(x):xが含まれるグループの要素を洗い出す
    roots():根をすべて洗い出す.
    size(x):xを含むグループの要素を返す
    """
    class State:  # グラフの状態を示すインナークラス
        def __init__(self):
            self.parents = {}
            self.rank = {}

    def __init__(self):
        self.st = self.State()

    def _add_tree(self, x):
        if not(x in self.st.parents):
            # self.st.parents[x] = x
            self.st.parents[x] = -1  # 各要素の親要素の番号、ただし根の場合は-(そのグループの要素数)
            self.st.rank[x] = 1  # 根の場合は各グループの階層の深さ

    def root(self, x):
        """
        要素xに対し根(グラフの一番上にくる要素)を返す
        """
        if (self.st.parents[x] < 0):  # is root
            return x
        else:
            # 経路圧縮:さかのぼって根を探し出して、張りなおす
            self.st.parents[x] = self.root(self.st.parents[x])  # 再帰
            return self.st.parents[x]
            # 本当はこの時、rank(深さ)が浅くなるケースがあるのでrankを変更する余地があるのだが
            # かえって、rankを調べなおすのに時間がかかるので、変更しない

    def union(self, x, y):
        """
        xとyとを同じグループとしてみなす
        つまり、xとyとで小さい方のグループを大きいほうにつなげる
        すなわち、xの根の親を、yの根とする。
        """
        self._add_tree(x)
        self._add_tree(y)
        x = self.root(x)
        y = self.root(y)
        if x == y:  # 初めから根が共通している場合は何もしない
            return

        if self.st.rank[x] < self.st.rank[y]:  # ランクが小さいほうをランクが大きいほうにつなげる
            self.st.parents[y] += self.st.parents[x]  # yが根になる。yの要素数はxの要素数だけ増加
            self.st.parents[x] = y   # xのほうがランクが小さいので、xをyの下につなげる
        else:
            self.st.parents[x] += self.st.parents[y]  # 上と逆の操作
            self.st.parents[y] = x

        # rankが上がるのは、つなぐ側とつながれる側のrankが同じだった場合
        # rankが同じ場合、xを根とするので、xのランクが1上昇
        if self.st.rank[x] == self.st.rank[y]:
            self.st.rank[x] += 1

    def is_same(self, x, y):
        """
        xとyが同じグループかを比較する
        """
        self._add_tree(x)
        self._add_tree(y)
        return self.root(x) == self.root(y)

    # 以降、おまけ機能
    def members(self, x):
        """
        xと同じグループに属するメンバーをすべて洗い出す
        """
        x = self.root(x)
        return [i for i in self.st.parents.keys if self.root(i) == x]

    def roots(self):
        """
        全ての根をリストで返す
        """
        return [i for i, (key_, x) in enumerate(self.st.parents.items()) if x < 0]

    def count_groups(self):
        """
        グラフの連結成分の個数を返す
        """
        return len(self.roots())

    def size(self, x):
        """
        xが属するグループの要素の数を返す
        """
        return -self.st.parents[self.root(x)]


def main():
    n, q, *pabs = map(int, open(0).read().split())
    pab = [pabs[i:i+3] for i in range(0, len(pabs), 3)]
    u = UnionFind()

    for i in range(q):
        p = pab[i][0]
        a = pab[i][1]
        b = pab[i][2]

        if p == 0:  # 連結クエリの場合
            u.union(a, b)
        else:
            if u.is_same(a, b):
                print('Yes')
            else:
                print('No')


main()
