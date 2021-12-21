import sys
sys.setrecursionlimit(10**6)


def main():
    n, m = map(int, input().split())
    nei_of = [[] for _ in range(n)]
    rev_nei_of = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        rev_nei_of[b].append(a)

    # SCC
    # 帰りがけに通った順番を記録
    order = []
    color = ['w']*n

    def dfs1(pre):
        for cur in nei_of[pre]:
            if color[cur] == 'w':
                color[cur] = 'g'
                dfs1(cur)
        order.append(pre)

    for node in range(n):
        if color[node] == 'w':
            color[node] = 'g'
            dfs1(node)

    # Setup Union Find
    par = [i for i in range(n)]
    siz = [1] * n

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
        siz[y] += siz[x]
        return

    def same(x, y):
        return find(x) == find(y)

    def get_size(x):
        return siz[find(x)]

    # DFS2 逆順にDFSを行う
    color2 = ['w']*n

    def dfs2(pre):
        for cur in rev_nei_of[pre]:
            if color2[cur] == 'w':
                color2[cur] = 'b'
                union(pre, cur)  # preとcurは同じ強連結成分に属する
                dfs2(cur)

    for node in reversed(order):
        if color2[node] == 'w':
            color2[node] = 'b'
            dfs2(node)

    # 各強連結成分ごとのサイズを取得する
    css_siz = [0] * n
    for node in range(n):
        css_node = find(node)
        css_size = get_size(css_node)
        css_siz[css_node] = css_size

    ans = 0
    for s in css_siz:
        # s*(s-1)//2が追加される
        ans += s*(s-1)//2

    print(ans)


main()
