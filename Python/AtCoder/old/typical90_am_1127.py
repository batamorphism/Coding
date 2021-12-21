import sys
sys.setrecursionlimit(10**6)
# 各edgeに対し
# edgeより後に含むnode数をxとして
# n*(n-x)が貢献度となる


def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]
    for edge_ind in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append((b, edge_ind))
        nei_of[b].append((a, edge_ind))

    # node_cnt_of[edge_ind] = そのedgeより前に含まれるnodeの数
    node_cnt_of = [0] * (n-1)

    def dfs(cur, pre):
        ret = 1
        for nex, edge_ind in nei_of[cur]:
            if nex == pre:
                continue
            tmp = dfs(nex, cur)
            node_cnt_of[edge_ind] = tmp
            ret += tmp
        return ret

    dfs(0, -1)

    ans = 0
    for edge_ind in range(n-1):
        ans += node_cnt_of[edge_ind] * (n-node_cnt_of[edge_ind])

    print(ans)


main()
