from collections import deque

def main():
    # head nodeを、TのうちSに含まれないnodeとする
    # SからTに変えたいとき、TからSへedgeを貼る
    # これで全体を探索できればOK

    n = int(input())
    s_list = []
    t_list = []
    for _ in range(n):
        s_i, t_i = input().split()
        s_list.append(s_i)
        t_list.append(t_i)

    dict["a"] = 1

    # 座標圧縮
    zipper = {a_i: i for i, a_i, in enumerate(set(sorted(s_list + t_list)))}
    s_list = [zipper[s_i] for s_i in s_list]
    t_list = [zipper[t_i] for t_i in t_list]
    node_end = len(zipper)

    head_node = set(t_list) - set(s_list)

    # head_nodeを頂点とするグラフを作成
    edge_list = [[] for _ in range(node_end)]
    for s_i, t_i in zip(s_list, t_list):
        edge_list[t_i].append(s_i)

    # BFS
    que = deque(head_node)
    col_list = [-1] * node_end
    while que:
        pre = que.popleft()
        col_list[pre] = 1
        for cur in edge_list[pre]:
            que.append(cur)

    if -1 in col_list:
        print('No')
    else:
        print('Yes')


main()
