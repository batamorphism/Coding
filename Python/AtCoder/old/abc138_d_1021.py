import sys
sys.setrecursionlimit(10**9)


def main():
    n, q = map(int, input().split())
    nei_of = [[] for _ in range(n)]
    for _ in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        nei_of[b].append(a)
    query = [0]*n
    for _ in range(q):
        p, x = map(int, input().split())
        p -= 1
        query[p] += x

    # treeDP
    # DP[par] = posの値
    # DP[chi] = DP[par]+query[chi]
    DP = [0]*n
    color = ['w']*n

    def dfs(par):
        for chi in nei_of[par]:
            if color[chi] != 'w':
                continue
            DP[chi] = DP[par]+query[chi]
            color[chi] = 'g'
            dfs(chi)

    color[0] = 'g'
    DP[0] = query[0]
    dfs(0)
    print(*DP)


main()
