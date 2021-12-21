import sys
sys.setrecursionlimit(10**6)

# 木は辺で考える
# 答えへの貢献度
# ある辺の貢献度は、その辺よりも小さい辺の数をcntとして
# cnt*(n-cnt)となる

def main():
    n = int(input())
    nei_of = [[] for _ in range(n)]

    for i in range(n-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append((b, i))
        nei_of[b].append((a, i))

    cnt_child_of = [0] * (n-1)

    def dfs(cur, pre):
        ret = 1
        for nex, edge_ind in nei_of[cur]:
            if nex == pre:
                continue
            cnt = dfs(nex, cur)
            # 戻り掛けに数える
            cnt_child_of[edge_ind] = cnt
            ret += cnt
        return ret

    dfs(0, -1)
    # print(cnt_child_of)
    ans = 0
    for edge_ind in range(n-1):
        cnt_child = cnt_child_of[edge_ind]
        ans += cnt_child * (n-cnt_child)
    print(ans)


main()
