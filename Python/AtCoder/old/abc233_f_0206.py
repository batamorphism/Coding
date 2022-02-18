from collections import deque
import sys
sys.setrecursionlimit(10**6)


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]

    def find(self, x):
        if x == self.par[x]:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.par[x] = y

    def is_same(self, x, y):
        return self.find(x) == self.find(y)


# 操作のedgeを張る
# 遠い順から、要素を確定していく
def main():
    node_end = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    m = int(input())
    nei_of = [[] for _ in range(node_end)]
    edge_list = []
    # 木になるように、edgeを張る
    uf = UnionFind(node_end)
    for i in range(m):
        a, b = map(lambda x: int(x)-1, input().split())
        edge_list.append((a, b))
        if uf.is_same(a, b):
            continue
        uf.union(a, b)
        nei_of[a].append((b, i))
        nei_of[b].append((a, i))
    del uf

    INF = float('inf')
    rev_P = [-1]*node_end
    for i, p_i in enumerate(P):
        rev_P[p_i] = i
    # 親のnodeと、そのedgeのindex
    par_of = [(-1, -1)]*node_end
    dist = [INF]*node_end

    def solve(i):
        # p_iをiに持ってくる
        # iを含む部分木について処理する
        sub_tree = []
        dist[i] = 0
        que = deque([i])
        while que:
            pre = que.popleft()
            sub_tree.append(pre)
            pre_d = dist[pre]
            cur_d = pre_d + 1
            for cur, edge_i in nei_of[pre]:
                if dist[cur] <= cur_d:
                    continue
                dist[cur] = cur_d
                que.append(cur)
                par_of[cur] = (pre, edge_i)

        # sub_treeについて、ソートしていく
        # distが大きい順に見ていく
        sub_tree.sort(key=lambda x: dist[x], reverse=True)
        for goal in sub_tree:
            start = rev_P[goal]
            # startをgoalに持っていけばよい
            path = get_path(start, goal, par_of)
            for edge_i in path:
                a, b = edge_list[edge_i]
                P[a], P[b] = P[b], P[a]
                rev_P[P[a]], rev_P[P[b]] = rev_P[P[b]], rev_P[P[a]]
                ans.append(edge_i+1)
        for x in sub_tree:
            if x != P[x]:
                return False
        return True

    ans = []
    for i in range(node_end):
        p_i = P[i]
        if i != p_i:
            is_ok = solve(i)
            if not is_ok:
                print(-1)
                return

    if [i for i, p_i in enumerate(P) if i != p_i]:
        print(-1)
        return

    print(len(ans))
    print(*ans)


def get_path(start, goal, par_of):
    # startからgoalへのpathを返す
    if start == goal:
        return []

    start_2_root = deque()
    cur_node = start
    while True:
        nex_node, edge_i = par_of[cur_node]
        if nex_node == -1:
            break
        start_2_root.append(edge_i)
        cur_node = nex_node

    goal_2_root = deque()
    cur_node = goal
    while True:
        nex_node, edge_i = par_of[cur_node]
        if nex_node == -1:
            break
        goal_2_root.append(edge_i)
        cur_node = nex_node

    while True:
        if not start_2_root:
            break
        if not goal_2_root:
            break
        if start_2_root[-1] != goal_2_root[-1]:
            break
        start_2_root.pop()
        goal_2_root.pop()

    # return start_2_root + goal_2_root[::-1]
    yield from start_2_root
    yield from reversed(goal_2_root)


main()
