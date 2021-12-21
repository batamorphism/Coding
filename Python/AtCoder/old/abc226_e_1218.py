# なもりグラフ
# 連結成分ごとに部分グラフS_iを考える
# S_iがすべてなもりグラフであれば、2**len(S)が答え
# そうでなければ、0が答え
# なもりグラフは、n辺n頂点のグラフであるから
# UnionFIndで辺と頂点の個数を管理する
import sys
sys.setrecursionlimit(10**6)
mod = 998244353


def main():
    # input
    node_end, edge_end = map(int, input().split())
    edge_list = []
    for _ in range(edge_end):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge_list.append((a, b))

    # setup UnionFind
    par = [i for i in range(node_end)]
    node_cnt_of = [1 for _ in range(node_end)]
    edge_cnt_of = [0 for _ in range(node_end)]

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        # 辺x->yを追加する
        x = find(x)
        y = find(y)
        if x == y:
            edge_cnt_of[y] += 1
            return
        par[x] = y
        node_cnt_of[y] += node_cnt_of[x]
        edge_cnt_of[y] += edge_cnt_of[x] + 1

    def get_node_cnt(x):
        x = find(x)
        return node_cnt_of[x]

    def get_edge_cnt(x):
        x = find(x)
        return edge_cnt_of[x]

    # calc node_cnt and edge_cnt
    for fr, to in edge_list:
        union(fr, to)

    # calc ans
    namori_set = set()
    for node in range(node_end):
        par_node = find(node)
        if par_node not in namori_set:
            node_cnt = get_node_cnt(node)
            edge_cnt = get_edge_cnt(node)
            if node_cnt == edge_cnt:
                namori_set.add(par_node)
            else:
                print(0)
                return

    ans = pow(2, len(namori_set), mod)
    print(ans)


main()
