import sys
sys.setrecursionlimit(10**8)

# 深さ優先探索には、スタックによる方法と、再帰による方法がある
# ただ探索するだけなら、どちらでもよい
# しかし、探索した後戻ってくる途中でも調べたいならば、スタックによる実装よりも再帰による実装のほうが楽


def main():

    # input
    n = int(input())
    A = []
    B = []
    for _ in range(n-1):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    # init
    to = [[] for _ in range(n+1)]
    for i in range(n-1):
        to[A[i]].append(B[i])
        to[B[i]].append(A[i])

    for i in range(1, n+1):
        to[i].sort()

    color = ['w'] * (n+1)

    # DFS
    ans = []
    color[1] = 'g'
    dfs(1, ans, color, to)
    print(*ans)


def dfs(u, ans, color, to):
    # 往路
    # 初めて来たときの処理
    ans.append(u)
    for v in to[u]:
        if color[v] == 'w':  # 完全未訪問
            color[v] = 'g'
            dfs(v, ans, color, to)
            # 帰路
            # 戻ってきたときの処理
            ans.append(u)
        elif color[v] == 'g':  # 一度はきたことある
            # 再訪問
            # 再訪問時の処理
            pass
        else:  # 全て探索済み
            pass
    color[u] = 'b'  # 各枝に対してすべて探索した


main()
