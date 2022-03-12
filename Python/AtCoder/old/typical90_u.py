import sys
sys.setrecursionlimit(10**6)


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    rev_nei_of = [[] for _ in range(node_end)]

    for _ in range(edge_end):
        a, b = map(lambda x: int(x)-1, input().split())
        nei_of[a].append(b)
        rev_nei_of[b].append(a)

    que = []
    done = [False]*node_end
    # dfsの戻り掛け順にキューに登録

    def dfs(pre):
        done[pre] = True
        for cur in nei_of[pre]:
            if done[cur]:
                continue
            dfs(cur)
        que.append(pre)

    for node in range(node_end):
        if not done[node]:
            dfs(node)

    done2 = [False]*node_end

    def dfs2(pre):
        done2[pre] = True
        ret = 1
        for cur in rev_nei_of[pre]:
            if done2[cur]:
                continue
            ret += dfs2(cur)
        return ret

    # 逆順に、つまり中央部からdfsをしていく
    ans = 0
    for node in reversed(que):
        if not done2[node]:
            cnt = dfs2(node)
            ans += (cnt*(cnt-1))//2
    print(ans)


main()
