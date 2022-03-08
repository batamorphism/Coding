import sys
sys.setrecursionlimit(10**6)
cnt = 0


# 強連結成分分解
def main():
    node_end, edge_end = map(int, input().split())
    edge_list = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(edge_end)]

    nei_of = [[] for _ in range(node_end)]
    rev_nei_of = [[] for _ in range(node_end)]
    order = [-1] * node_end

    for fr, to in edge_list:
        nei_of[fr].append(to)
        rev_nei_of[to].append(fr)

    # 帰りがけに番号を振る
    done = [False]*node_end

    def dfs(pre):
        global cnt
        done[pre] = True
        for cur in nei_of[pre]:
            if done[cur]:
                continue
            dfs(cur)
        order[pre] = cnt
        cnt += 1

    for node in range(node_end):
        if done[node]:
            continue
        dfs(node)

    # orderが小さい順に深さ優先探索
    # sub treeのノードの数を数える
    done2 = [False]*node_end

    def dfs2(pre):
        ret = 1
        done2[pre] = True
        for cur in rev_nei_of[pre]:
            if done2[cur]:
                continue
            val = dfs2(cur)
            ret += val
        return ret

    node_list = [i for i in range(node_end)]
    node_list.sort(key=lambda x: order[x], reverse=True)
    ans = 0
    for node in node_list:
        if done2[node]:
            continue
        cnt = dfs2(node)
        ans += cnt*(cnt - 1)//2

    print(ans)


main()
