import networkx as nx
import random
# import matplotlib.pyplot as plt


def main():
    # input
    n = 55
    node_list = list(range(n**2))
    bad_list = []
    for i in range(n):
        bad = [n*j + i for j in range(n)]
        bad_list.append(bad)
        bad = [n*i + j for j in range(n)]
        bad_list.append(bad)
    color_num = n*2+1

    # solve
    try:
        group = solver(node_list, bad_list, color_num)
    except Exception as e:
        print(e)
        return

    # 標準出力で返す
    for g in group:
        print(*g, sep=',')


def solver(node_list, bad_list, color_num):
    """前回同じだった人同士や、同じ所属同士の人が一緒にならないようなグループをcolor_num個生成する
    各グループには、色:0～color_num-1が採番される。

    Args:
        node_list (list): 人全体のリスト
        bad_list (list): 一緒になってはいけない人のリスト
        color_num (int): 作成するグループ数
    Returns:
        list: list[col] = そのcolが採番された人のリスト
    """

    # 結果が毎回同じになってしまわないように、シャッフルする
    random.shuffle(node_list)

    # setup graph
    G = nx.Graph()
    G.add_nodes_from(node_list)

    # 各bad_list内で、部分グラフが完全グラフとなる
    # つまり、bad_list内の各nodeは互いに異なる色になる
    for group in bad_list:
        for fr in group:
            if not G.has_node(fr):
                raise Exception('error: node_list have ' + str(fr))
            for to in group:
                if fr == to:
                    continue
                G.add_edge(fr, to)

    # solve coloring
    try:
        colored = nx.algorithms.coloring.equitable_color(G, color_num)
    except nx.NetworkXException as e:
        raise e
    # nx.draw(G, node_color=list(colored.values()), node_size=10, width=0.2)
    # plt.show()

    # output
    # group[col] = colに採番された人のリスト
    group = [[] for _ in range(color_num)]
    for key, val in colored.items():
        group[val].append(key)
    for g in group:
        g.sort()
    group.sort()

    return group


main()
