from collections import Counter


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
    # DFSをして、帰りがけの順番を保持する
    order = []
    # 0->見たことがない、1->行きがけの処理をしたことがある、2->帰りがけの処理をしたことがある
    color = [0]*node_end

    for node in range(node_end):
        stk = [~node, node]
        while stk:
            pre = stk.pop()
            if pre >= 0:
                if color[pre] != 0:
                    continue
                # 行きがけの処理
                color[pre] = 1
                for cur in nei_of[pre]:
                    if color[cur] != 0:
                        continue
                    stk.append(~cur)
                    stk.append(cur)
            else:
                if color[~pre] == 2:
                    continue
                # 帰りがけの処理
                order.append(~pre)
                color[~pre] = 2

    # 帰りがけの順番が遅い順に、DFSをする
    color = [0] * node_end
    SCC = [-1] * node_end
    for node in reversed(order):
        stk = [node]
        while stk:
            pre = stk.pop()
            if color[pre]:
                continue
            SCC[pre] = node
            color[pre] = 1
            for cur in rev_nei_of[pre]:
                stk.append(cur)

    cnt_of = Counter(SCC)
    ans = 0
    for cnt in cnt_of.values():
        ans += cnt*(cnt-1)//2
    print(ans)


main()
