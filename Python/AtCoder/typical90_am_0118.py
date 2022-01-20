# 木は辺
# 答えへの貢献度
# 各辺について、その辺より上の点の数をcntとし、cnt*(n-cnt)を答えに加算
import sys
sys.setrecursionlimit(10**6)


def main():
    node_end = int(input())
    edge_end = node_end - 1
    nei_of = [[] for _ in range(node_end)]

    for i in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append((to, i))
        nei_of[to].append((fr, i))

    cnt_of = [0]*edge_end

    def dfs(cur, pre):
        ret = 1
        for nex, edge_i in nei_of[cur]:
            if nex == pre:
                continue
            cnt_nex = dfs(nex, cur)
            cnt_of[edge_i] = cnt_nex
            ret += cnt_nex
        return ret

    dfs(0, -1)
    ans = 0
    for cnt in cnt_of:
        ans += cnt*(node_end-cnt)
    print(ans)


main()
