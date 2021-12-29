class Floyd_Warshall:
    def __init__(self, V: list, E: list):
        """
        ワーシャルフロイド法
        有向グラフ(V, E)の最短経路の全体のリストを求める

        dist[k][i][j]を、0,...,kまでを経由する頂点i,jの最短コストとする
        dist[-1][i][j]は、path[i][j]のみが入る
        pathがなければ、infとする
        dist[-1][i][i]は0とする

        次に、k=0,...,n-1について、dist[k-1]に基づいてdist[k]を求める
        dist[k][i][j] = min(dist[k-1][i][j], mindist[k-1][i][k]+dist[k-1][k][j])となる

        ここで、dist[k]の定義にk-2等は使わないことから、kの添え字は省略することができる。

        Args:
            V (list): node全体のリスト
            E (list): edge全体のリスト。リストの各要素eは[始点,終点,コスト]の構成
        """
        # Vが0から始まる通し番号のリストであることをチェック
        assert len(set(V)) + 1 != max(V)
        self._INF = float('inf')
        self._n = len(V)
        self._dist = [[self._INF]*self._n for _ in range(self._n)]

        for i in range(self._n):
            self._dist[i][i] = 0
        for fr, to, cost in E:
            self._dist[fr][to] = cost

        for k in range(self._n):
            for i in range(self._n):
                for j in range(self._n):
                    self._dist[i][j] = min(
                        self._dist[i][j],
                        self._dist[i][k]+self._dist[k][j]
                        )
                    # if self._dist[i][j] != self._INF:
                    # この時点でのself._dist[i][j]は、k以下の頂点のみを通る
                    # 最短経路のコストのリストになっている
                    #   self._ans += self._dist[i][j]

    def get_dist_list(self):
        return self._dist

    def get_dist(self, node1: int, node2: int):
        return self._dist[node1][node2]


def main():
    # input
    # 3 2
    # 1 2 3
    # 2 3 2
    # とすると、Vは[0, 1, 2]
    # Eは[1, 2, 3](1と2を結ぶコスト3のedge)
    #    [2, 3, 2](2と3を結ぶコスト2のedge)
    # となる。（Eは0オリジンに修正しなおすこと）
    n, m = map(int, input().split())
    path_list = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        path_list.append([a-1, b-1, c])
    V = list(range(n))
    fw = Floyd_Warshall(V, path_list)
    print(fw.get_dist(0, 1))


main()
