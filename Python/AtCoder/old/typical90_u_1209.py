import sys
from collections import deque
sys.setrecursionlimit(10**6)


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    rev_of = [[] for _ in range(node_end)]

    for _ in range(edge_end):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append(b)
        rev_of[b].append(a)

    # 強連結成分分解
    # 帰りがけにnodeをqueに左から追加していく
    que = deque()
    scc = []
    color = ['w']*node_end

    def dfs1(pre):
        for cur in nei_of[pre]:
            if color[cur] == 'w':
                color[cur] = 'g'
                dfs1(cur)
        que.appendleft(pre)

    for node in range(node_end):
        if color[node] == 'w':
            color[node] = 'g'
            dfs1(node)

    def dfs2(pre):
        for cur in rev_of[pre]:
            if color[cur] == 'w':
                color[cur] = 'g'
                dfs2(cur)
        scc.append(pre)

    color = ['w']*node_end
    scc_list = []
    # 逆向きにdfsしていく
    for node in que:
        if color[node] == 'w':
            color[node] = 'g'
            dfs2(node)
            scc_list.append(scc[:])
            scc = []

    # print(scc_list)
    ans = 0
    for scc in scc_list:
        n = len(scc)
        ans += n*(n-1)//2

    print(ans)


main()
