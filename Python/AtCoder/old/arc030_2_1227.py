import sys
sys.setrecursionlimit(10**6)


# 木は辺で
# 各辺について、両端に宝石が1つ以上あれば、答えに2加算
# 各辺より先にある宝石の数をcntとし、cnt != 0 and cnt != totalであれば、答えに2加算
def main():
    node_end, st_node = map(int, input().split())
    st_node -= 1

    stone_node = list(map(int, input().split()))
    stone_node[st_node] = 1
    total = sum(stone_node)
    nei_of = [[] for _ in range(node_end)]

    for i in range(node_end-1):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append((i, b))
        nei_of[b].append((i, a))

    cnt_of = [0] * (node_end - 1)

    def dfs(cur, pre):
        ret = 0
        for ind, nex in nei_of[cur]:
            if nex == pre:
                continue
            cnt = dfs(nex, cur)
            # 戻り掛けに数える
            cnt_of[ind] = cnt
            ret += cnt
        # 戻り掛けに追加する
        if stone_node[cur]:
            ret += 1
        return ret

    dfs(st_node, -1)
    # print(cnt_of)
    ans = 0
    for cnt in cnt_of:
        if cnt != 0 and cnt != total:
            ans += 2
    print(ans)


main()
