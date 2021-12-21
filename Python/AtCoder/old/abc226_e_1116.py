import sys
sys.setrecursionlimit(10**6)
mod = 998244353

# 各連結成分について、すべてがn辺n頂点であれば、2**連結成分の個数が答え
# そうでなければ0が答え


def main():
    n, m = map(int, input().split())
    nei_of = [[]for _ in range(n)]

    for _ in range(m):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        nei_of[u].append(v)
        nei_of[v].append(u)

    color = ['w']*n

    def dfs(pre):
        node_cnt = 1
        edge_cnt = 0
        for cur in nei_of[pre]:
            edge_cnt += 1
            if color[cur] == 'w':
                color[cur] = 'g'
                n, e = dfs(cur)
                node_cnt += n
                edge_cnt += e
        return node_cnt, edge_cnt

    ans = 1
    for node in range(n):
        if color[node] == 'w':
            color[node] = 'g'
            node_cnt, edge_cnt = dfs(node)
            edge_cnt //= 2
            if node_cnt == edge_cnt:
                ans *= 2
                ans %= mod
            else:
                ans = 0
                break

    print(ans)


main()
