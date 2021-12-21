import sys
sys.setrecursionlimit(10**6)

mod = 998244353


def main():
    # 入力
    node_end, edge_end = map(int, input().split())
    edge_list = []
    for _ in range(edge_end):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        edge_list.append((a, b))

    # Setup Union Find
    par = [i for i in range(node_end)]
    loop_cnt = [0]*node_end

    def find(x):
        if par[x] == x:
            return x
        else:
            par[x] = find(par[x])
            return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        par[x] = y
        loop_cnt[y] = loop_cnt[x]+loop_cnt[y]

    def same(x, y):
        return find(x) == find(y)

    for edge in edge_list:
        u, v = edge
        if same(u, v):
            # uとvを足すとループが一個追加
            loop_cnt[find(u)] += 1
        union(u, v)  # 常に辺は追加

    cnt = set()
    for node in range(node_end):
        par_node = find(node)
        par_loop_cnt = loop_cnt[par_node]
        if par_loop_cnt == 1:
            if par_node not in cnt:
                cnt.add(par_node)
        if par_loop_cnt != 1:  # 駄目なパターンが出たら答えはもう0
            print(0)
            return

    ans = pow(2, len(cnt), mod)
    ans %= mod
    print(ans)


main()
