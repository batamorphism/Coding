
def main():
    n, m = map(int, input().split())
    # s = "00000" n文字
    # T = *001100*だったら
    # T = 0010100 に変換(次のbitと同じかどうか)
    # (L, R)は、L bitを反転、R+1 bitを反転となる
    # 全ての1bitが偶数個あるTに対し、置換できるようになればよく
    # これは、各bitをnodeとしたグラフが連結になればよい
    node_end = n+1  # 1桁増える
    edge_list = []
    for _ in range(m):
        c, le, ri = map(int, input().split())
        le -= 1
        ri -= 1
        ri += 1
        edge_list.append((c, le, ri))

    # union-find
    par = [i for i in range(node_end)]

    def same(x, y):
        return find(x) == find(y)

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
        return

    def count_head_node():
        ret = 0
        for node, parent in enumerate(par):
            if node == parent:
                ret += 1
        return ret

    # クラスカル法
    cost = 0
    edge_list.sort()
    for c, le, ri in edge_list:
        if same(le, ri):
            continue
        cost += c
        union(le, ri)
    if count_head_node() != 1:
        print(-1)
    else:
        print(cost)


main()
