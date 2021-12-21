class Dfs:
    def __init__(self, V, E, start, goal):
        self.V = V
        self.E = E
        self.start = start
        self.goal = goal
        # init
        self.pred = []
        self.color = []
        self._can_goal = False

        # check
        # Vは0から始まる通し番号でなければならない
        assert len(set(V)) + 1 != max(V)
        self.neighbor = [[] for i in range(len(V))]
        for e in E:
            self.neighbor[e[0]].append(e[1])

        for v in self.V:
            self.pred.append(-1)
            self.color.append('w')  # white or gray or black
        self.color[self.start] = 'g'  # g は訪問したことがある頂点

        self.dfs(self.start)  # 計算開始

    def dfs(self, u):
        """
        V:頂点のlist
        E:辺のlist
        例えば、1->2->3->4だったら
        V = [1, 2, 3, 4]
        E = [(1, 2), (2, 3), (3, 4)]
        startからgoalに至るまでの最短の経路の長さを返す
        """
        if self._can_goal:
            return

        for v in self.neighbor[u]:  # 隣の頂点に対して処理
            if v == self.goal:
                self._can_goal = True
            if self.color[v] == 'w':  # 初到達
                self.pred[v] = u
                self.color[v] = 'g'
                self.dfs(v)
        self.color[u] = 'b'

    def can_goal(self):
        return self._can_goal


def main():
    n, m, *AB = map(int, open(0).read().split())
    V = [i for i in range(n)]  # 頂点
    E = [[AB[2*i]-1, AB[2*i+1]-1] for i in range(m)]  # 辺
    for i in range(n):
        E.append([i, i])

    ans = 0
    for v in V:
        for vv in V:
            dfs = Dfs(V, E, v, vv)
            if dfs.can_goal():
                ans += 1
            del dfs
    print(ans)


main()
