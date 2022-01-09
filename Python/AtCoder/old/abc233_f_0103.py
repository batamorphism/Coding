from collections import deque
import sys
import random
sys.setrecursionlimit(10**6)
INF = 1001


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

        self._par[x] = y

    def same(self, x, y):
        """
        xとyが同じグループかを比較する
        """
        return self.find(x) == self.find(y)


# 操作可能なペアをedgeとする
# nodeの末尾からソートしていく -> 末尾は一度ソートされたらもうソートしなおす必要がない
# 末尾のnodeをiとする
# iの現在いる位置をR[i]とする(Pの逆)
# r_iとiとをswapする
# r_iとiのrootからのpathを取って、共通部分を消していけば、最短のswapが求まる
def main():
    # input
    node_end = int(input())
    P = list(map(lambda x: int(x)-1, input().split()))
    R = [-1]*node_end
    for i, p_i in enumerate(P):
        R[p_i] = i
    """
    node_end = 1000
    P = list(reversed(range(node_end)))
    R = [-1]*node_end
    for i, p_i in enumerate(P):
        R[p_i] = i
    """

    uf = UnionFind(node_end)
    edge_end = int(input())
    nei_of = [[] for _ in range(node_end)]
    edge_list = []
    for i in range(edge_end):
        a, b = map(lambda x: int(x)-1, input().split())
        # 木にするため、a, bがすでに連結の場合は飛ばす
        edge_list.append((a, b))
        if uf.same(a, b):
            continue
        uf.union(a, b)
        nei_of[a].append((b, i))
        nei_of[b].append((a, i))

    """
    nei_of = [[] for _ in range(node_end)]
    edge_end = 2*10**5
    edge_list = []
    for i in range(edge_end):
        a = random.randint(0, node_end-1)
        b = random.randint(0, node_end-1)
        # 木にするため、a, bがすでに連結の場合は飛ばす
        edge_list.append((a, b))
        if uf.same(a, b):
            continue
        uf.union(a, b)
        nei_of[a].append((b, i))
        nei_of[b].append((a, i))
    """

    ans = []
    dist = [INF]*node_end
    par_of = [(-1, -1) for _ in range(node_end)]  # par_of[node] = nodeの親, そのedge

    for i, p_i in enumerate(P):
        if i != p_i:
            if not solve(P, R, nei_of, i, ans, node_end, edge_list, dist, par_of):
                print(-1)
                return

    print(len(ans))
    print(*ans)


def solve(P, R, nei_of, root_i, ans, node_end, edge_list, dist, par_of) -> bool:
    # iをrootとした部分木について
    # 末尾からソートしていく
    # ソートできない場合はFalseを返す
    if dist[root_i] != INF:
        raise
    sub_tree = []
    # dist = [INF]*node_end  # ここを毎回生成するのは遅い
    dist[root_i] = 0
    que = deque([root_i])
    while que:
        pre = que.popleft()
        sub_tree.append(pre)
        pre_d = dist[pre]
        cur_d = pre_d + 1
        for cur, edge_i in nei_of[pre]:
            if dist[cur] > cur_d:
                dist[cur] = cur_d
                par_of[cur] = (pre, edge_i)
                que.append(cur)

    sub_tree.sort(key=lambda x: dist[x], reverse=True)
    for node in sub_tree:
        # 深い順に要素を入れ替える
        if node == P[node]:
            continue
        swap_node = R[node]  # P[swap_node] = node
        if dist[swap_node] == INF:
            return False
        # nodeとswap_nodeと最短経路を求める
        # swap_node -> nodeのpathを取ってくれば、その順にswapすればswap_nodeをnodeに持ってこれる
        path = get_path(swap_node, node, par_of)
        if not path:
            return False
        # swap_nodeをnodeに持ってくる
        for edge_i in path:
            ans.append(edge_i+1)
            a, b = edge_list[edge_i]
            R[P[a]], R[P[b]] = R[P[b]], R[P[a]]
            P[a], P[b] = P[b], P[a]
    for s in sub_tree:
        if P[s] != s:
            raise
    return True


def get_path(fr, to, par_of):
    root_2_fr = deque()
    root_2_to = deque()
    for node, path in zip([fr, to], [root_2_fr, root_2_to]):
        while par_of[node][0] != -1:
            node, edge_i = par_of[node]
            path.appendleft(edge_i)

    while root_2_fr and root_2_to:
        if root_2_fr[0] == root_2_to[0]:
            root_2_fr.popleft()
            root_2_to.popleft()
        else:
            break  # FUCK YOU!!!!

    for node in reversed(root_2_fr):
        yield node

    for node in root_2_to:
        yield node

    """
    ret = list(reversed(root_2_fr)) + list(root_2_to)
    return ret
    """


main()
