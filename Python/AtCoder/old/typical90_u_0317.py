import sys
sys.setrecursionlimit(10**7)


def main():
    node_end, edge_end = map(int, input().split())
    nei_of = [[] for _ in range(node_end)]
    rev_nei_of = [[] for _ in range(node_end)]

    for _ in range(edge_end):
        fr, to = map(lambda x: int(x) - 1, input().split())
        nei_of[fr].append(to)
        rev_nei_of[to].append(fr)

    # 戻り掛けにスタックに登録
    stk = []

    first_step(stk, node_end, nei_of)
    cnt_list = second_step(stk, rev_nei_of)

    ans = 0
    for cnt in cnt_list:
        ans += (cnt-1)*cnt//2
    print(ans)


def second_step(stk, rev_nei_of):
    done = [False]*len(stk)

    def dfs(node):
        # 非再帰でok
        cnt = 0
        que = [node]
        while que:
            pre = que.pop()
            if done[pre]:
                continue
            done[pre] = True
            for cur in rev_nei_of[pre]:
                if done[cur]:
                    continue
                que.append(cur)
            cnt += 1
        return cnt

    cnt_list = []

    # 逆向きにdfs
    while stk:
        node = stk.pop()
        if done[node]:
            continue
        cnt = dfs(node)
        cnt_list.append(cnt)
    return cnt_list


def first_step(stk, node_end, nei_of):
    done = [False]*node_end

    # 戻り掛けにスタックに登録
    def dfs(pre):
        done[pre] = True
        for cur in nei_of[pre]:
            if done[cur]:
                continue
            dfs(cur)
        stk.append(pre)

    for node in range(node_end):
        if done[node]:
            continue
        dfs(node)


main()
