import sys
sys.setrecursionlimit(10**6)


def main():
    n, m = map(int, input().split())
    node_end = n + 1
    del n

    edge_list = []
    for _ in range(m):
        co, le, ri = map(int, input().split())
        le -= 1
        edge_list.append((le, ri, co))
    edge_list.sort(key=lambda x: x[2])

    # クラスカル
    par = [i for i in range(node_end)]

    def find(x):
        if par[x] == x:
            return x
        par[x] = find(par[x])
        return par[x]

    def unite(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        par[x] = y

    ans = 0
    cnt = 1  # 木のサイズ
    for le, ri, co in edge_list:
        if find(le) != find(ri):
            ans += co
            cnt += 1
            unite(le, ri)
    if cnt != node_end:
        print(-1)
    else:
        print(ans)


main()
