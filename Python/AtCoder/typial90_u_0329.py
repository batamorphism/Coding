def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    rev_nei_of = [[] for _ in range(node_end)]
    for _ in range(edge_end):
        fr, to = map(int, input().split())
        fr -= 1
        to -= 1
        nei_of[fr].append(to)
        rev_nei_of[to].append(fr)

    # SCC
    # 帰りがけの順番でキューに追加
    used = [False] * node_end
    used_return = [False] * node_end
    order = []

    def dfs(root):
        stk = []
        stk.append(~root)
        stk.append(root)
        while stk:
            pre = stk.pop()
            if pre >= 0:
                # 行きがけ
                if used[pre]:
                    if stk[-1] != ~pre:
                        raise
                    stk.pop()
                    continue
                used[pre] = True
                for cur in nei_of[pre]:
                    stk.append(~cur)
                    stk.append(cur)
            else:
                # 帰りがけ
                used_return[~pre] = True
                order.append(~pre)

    for node in range(node_end):
        if used[node]:
            continue
        dfs(node)

    # 帰りがけの順番の逆順でdfsする
    group_of = [-1]*node_end
    used = [False]*node_end

    def dfs2(root):
        stk = []
        stk.append(root)
        while stk:
            pre = stk.pop()
            if used[pre]:
                continue
            used[pre] = True
            group_of[pre] = root
            for cur in rev_nei_of[pre]:
                stk.append(cur)

    for node in reversed(order):
        if used[node]:
            continue
        dfs2(node)

    cnt_of = [0]*node_end
    for node in range(node_end):
        cnt_of[group_of[node]] += 1

    ans = 0
    for cnt in cnt_of:
        ans += cnt*(cnt-1)//2

    print(ans)


main()
