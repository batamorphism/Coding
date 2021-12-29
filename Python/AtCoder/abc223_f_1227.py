import sys
sys.setrecursionlimit(10**6)


# 葉から葉へ交換する
# a - root - b - c
# で、aとcをswapするには
# 左から順に置換していくと
# root - b - c - a
# 右から2番目から置換していくと
# c - root - b- a
# したがって、a -> cを結ぶedgeを(e0, e1, ..., en)として
# e0, e1, ..., enでaをcに持っていける
class UnionFind:
    def __init__(self, n):
        self.n = n
        self.par = [i for i in range(n)]

    def find(self, x):
        if self.par[x] == x:
            return x
        self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        self.par[x] = y

    def same(self, x, y):
        return self.find(x) == self.find(y)


def main():
    node_end = int(input())
    uf = UnionFind(node_end)
    P = list(map(lambda x: int(x)-1, input().split()))
    pos = [0] * node_end
    for i, p_i in enumerate(P):
        pos[p_i] = i
    edge_end = int(input())
    edge_list = []
    nei_of = [[] for _ in range(node_end)]
    for i in range(edge_end):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        if not uf.same(a, b):
            uf.union(a, b)
            nei_of[a].append((b, i))
            nei_of[b].append((a, i))
        edge_list.append((a, b))

    dep = [0]*node_end
    ans = []
    done = [False]*node_end
    par_of = [(0, 0)]*node_end  # (node, edge_ind)

    def solve(root):
        # 各rootの部分木Sを求める
        # 部分木Sの深さを求める
        # 深さが深い順に、swapしていく
        sub_tree = []

        def dfs(pre):
            done[pre] = True
            sub_tree.append(pre)
            for cur, ind in nei_of[pre]:
                if done[cur]:
                    continue
                dep[cur] = dep[pre] + 1
                par_of[cur] = (pre, ind)
                dfs(cur)

        dfs(root)
        sub_tree.sort(key=lambda x: dep[x], reverse=True)
        for to in sub_tree:
            fr = pos[to]  # 移動先
            if fr == to:
                continue
            if not uf.same(fr, to):
                print(-1)
                exit()
            fr_root_path = calc_path(fr, root, par_of)
            to_root_path = calc_path(to, root, par_of)
            # fr_to_path = complex_path(fr_root_path, to_root_path)
            for edge_ind in complex_path(fr_root_path, to_root_path):
                ans.append(edge_ind + 1)
                a, b = edge_list[edge_ind]
                P[a], P[b] = P[b], P[a]
                pos[P[a]], pos[P[b]] = pos[P[b]], pos[P[a]]
        for s in sub_tree:
            if P[s] != s:
                raise

    for root in range(node_end):
        if P[root] == root:
            continue
        solve(root)
    # print(P)
    print(len(ans))
    print(*ans)


def calc_path(st, en, par_of):
    ret = []
    fr = st
    while fr != en:
        to, ind = par_of[fr]
        ret.append(ind)
        fr = to
    return ret


def complex_path(fr_path: list, to_path: list):
    # 末尾が同じ間、fr_path, to_pathをpopしていく
    # 最後に逆向きにくっつける
    while fr_path and to_path and fr_path[-1] == to_path[-1]:
        fr_path.pop()
        to_path.pop()
    for i in fr_path:
        yield i
    for i in reversed(to_path):
        yield i


main()
