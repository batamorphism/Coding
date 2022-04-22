import sys
sys.setrecursionlimit(10**6)


def main():
    node_end = int(input())
    edge_end = node_end - 1
    nei_of = [[] for _ in range(node_end)]

    for i in range(edge_end):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append((to, i))
        nei_of[to].append((fr, i))

    # cnt_of[edge_id] = そのedgeよりleaf側にある頂点の数
    cnt_of = [0] * edge_end

    def dfs(cur, pre):
        ret = 1
        for nex, edge_id in nei_of[cur]:
            if nex == pre:
                continue
            cnt = dfs(nex, cur)
            cnt_of[edge_id] = cnt
            ret += cnt
        return ret

    dfs(0, -1)

    ans = 0
    for cnt in cnt_of:
        ans += cnt*(node_end-cnt)
    print(ans)


main()
