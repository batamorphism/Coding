import queue


class Bfs:
    def __init__(self, V, E, start, goal):
        self.V = V
        self.E = E
        self.start = start
        self.goal = goal
        # init
        self.pred = []
        self.dist = []
        self.color = []
        self._count = []

        # check
        # Vは0から始まる通し番号でなければならない
        assert len(set(V)) + 1 != max(V)
        self.neighbor = [[] for i in range(len(V))]
        for e in E:
            self.neighbor[e[0]].append(e[1])

        INF = 1e14
        for v in self.V:
            self.pred.append(-1)
            self.dist.append(-INF)
            self.color.append('w')  # white or gray or black
            self._count.append(0)
        self.color[self.start] = 'g'  # g は訪問したことがある頂点
        self.dist[self.start] = 0  # スタート地点の距離は0
        self._count[self.start] = 1

    def bfs(self):
        """ 
        V:頂点のlist
        E:辺のlist
        例えば、1->2->3->4だったら
        V = [1, 2, 3, 4]
        E = [(1, 2), (2, 3), (3, 4)]
        startからgoalに至るまでの最短の経路の長さを返す
        """

        Q = queue.Queue()  # 先入れ先出し
        Q.put(self.start)

        while not Q.empty():
            u = Q.get()
            for v in self.neighbor[u]:
                if self.color[v] == 'w':  # 初到達
                    self.dist[v] = self.dist[u] + 1
                    self.pred[v] = u
                    self._count[v] = self._count[u]
                    self.color[v] = 'g'
                    Q.put(v)
                else:  # 2回目以降
                    if self.dist[v] == self.dist[u] + 1:  # 最短経路であったならば
                        self._count[v] += self._count[u]
            self.color[u] = 'b'  # 探索完了

        return self.dist[self.goal]

    def get_count(self):
        return self._count[self.goal]


def main():
    n, m, *ab_ = map(int, open(0).read().split())
    a = [ab_[2*i] - 1 for i in range(m)]
    b = [ab_[2*i+1] - 1 for i in range(m)]
    path = [(a[i], b[i]) for i in range(m)]
    path2 = [(path[i][1], path[i][0]) for i in range(len(path))]
    path = path + path2
    point = [i for i in range(n)]

    bfs = Bfs(point, path, 0, n - 1)
    bfs.bfs()
    print(bfs.get_count() % (10**9+7))


main()