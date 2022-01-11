import sys
from collections import deque
from collections import defaultdict
sys.setrecursionlimit(10**6)
INF = float('inf')


# 要素が深いものからswapして確定していく
def main():
    n = int(input())
    P = list(map(lambda x:int(x)-1, input().split()))
    rev_P = [-1]*n
    for i, p_i in enumerate(P):
        rev_P[p_i] = i

    # setup union find
    par = [i for i in range(n)]

    def find(x):
        if par[x] == x:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        par[x] = y

    def same(x, y):
        return find(x) == find(y)

    m = int(input())
    edge_list = []
    nei_of = [[] for _ in range(n)]
    # 連結になっている辺は追加しない
    for edge_i in range(m):
        a, b = map(lambda x:int(x)-1, input().split())
        edge_list.append((a, b))
        if not same(a, b):
            nei_of[a].append((b, edge_i))
            nei_of[b].append((a, edge_i))
            union(a, b)

    ans = []

    def solve(i):
        # iを含む連結成分について、要素をそろえる
        dist = [INF]*n
        # iを含む連結成分について、iからの距離を求める
        root = i
        dist[root] = 0
        que = deque()
        que.append(root)
        sub_tree = []
        par_of = defaultdict(lambda: -1)
        while que:
            pre = que.popleft()
            sub_tree.append(pre)
            pre_d = dist[pre]
            cur_d = pre_d + 1
            for cur, edge_i in nei_of[pre]:
                if dist[cur] <= cur_d:
                    continue
                dist[cur] = cur_d
                par_of[cur] = (pre, edge_i)
                que.append(cur)

        def get_path(fr, to):
            # frからtoに至るまでのpathを求める
            fr_2_root = []
            while par_of[fr] != -1:
                fr_2_root.append(par_of[fr][1])
                fr = par_of[fr][0]
            to_2_root = []
            while par_of[to] != -1:
                to_2_root.append(par_of[to][1])
                to = par_of[to][0]
            while True:
                if not fr_2_root:
                    break
                if not to_2_root:
                    break
                if fr_2_root[-1] != to_2_root[-1]:
                    break
                fr_2_root.pop()
                to_2_root.pop()
            ret = fr_2_root + to_2_root[::-1]
            return ret

        # sub_treeを深い順にソートする
        sub_tree.sort(key=lambda x:dist[x], reverse=True)

        for j in sub_tree:
            # Pのj番目の要素をjにする
            pos = rev_P[j]
            if not same(j, pos):
                return False
            # posをjまで持ってくればよい
            # pos -> jまでのrootが答え
            pos_2_j = get_path(pos, j)
            for edge_i in pos_2_j:
                ans.append(edge_i+1)
                a, b = edge_list[edge_i]
                rev_P[P[a]], rev_P[P[b]] = rev_P[P[b]], rev_P[P[a]]
                P[a], P[b] = P[b], P[a]

        for j in sub_tree:
            if j != P[j]:
                raise
        return True

    for i, p in enumerate(P):
        if i != p:
            flg = solve(i)
            if not flg:
                print(-1)
                return

    print(len(ans))
    print(*ans)


main()
