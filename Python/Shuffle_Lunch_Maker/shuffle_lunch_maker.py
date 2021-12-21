import PySimpleGUI as sg  # GUIを作成するライブラリ
import networkx as nx
import random


def main():
    # sg.theme('Default')   # デザインテーマの設定

    # ウィンドウに配置するコンポーネント
    layout = [[sg.Text('作成するグループ数'), sg.InputText(3, size=5, key='color_num'), sg.Checkbox('乱数を使用する', key='use_random', default=True), sg.Checkbox('結果をソート', key='use_sort', default=False)],
            [sg.Text('参加者一覧'), sg.InputText(default_text="Aさん,Bさん,Cさん,Dさん,Eさん,Fさん,Gさん", key='node_list')],
            [sg.Text('禁則: 一緒にしたくない人のリスト')],
            [sg.Multiline(default_text="Aさん,Bさん,Cさん\nDさん,Eさん\nDさん,Fさん", size=(80, 10), key='bad_list')],
            [sg.Text('結果')],
            [sg.Multiline(size=(80, 10), key='op1')],
            [sg.Button('Run'), sg.Button('Cancel')]]

    # ウィンドウの生成
    window = sg.Window('Shuffle_Lunch_Maker_ver1.0', layout)

    # イベントループ
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == 'Cancel':
            break
        elif event == 'Run':
            values['op1'] = ''
            try:
                # get input
                node_list = list(values['node_list'].split(','))
                bad_list_ = list(values['bad_list'].split('\n'))
                bad_list_ = [bad for bad in bad_list_ if bad]  # 空行を削除
                bad_list = [list(bad.split(',')) for bad in bad_list_]
                color_num = int(values['color_num'])
                use_random = values['use_random']
                use_sort = values['use_sort']

                # solve
                group = []
                group = solver(node_list, bad_list, color_num, use_random, use_sort)

                # 出力結果をGUIに反映する
                op1_list = []
                for g in group:
                    op1_list.append(','.join(g) + '\n')
                op1 = ''.join(op1_list)
                values['op1'] = op1
                window.Element('op1').update(values['op1'])

            except Exception as e:
                values['op1'] = e
                window.Element('op1').update(values['op1'])
                continue

    window.close()


def solver(node_list, bad_list, color_num, use_random=True, use_sort=False):
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
    if use_random:
        random.shuffle(node_list)

    # setup graph
    G = nx.Graph()
    G.add_nodes_from(node_list)

    # 各bad_list内で、部分グラフが完全グラフとなる
    # つまり、bad_list内の各nodeは互いに異なる色になる
    for group in bad_list:
        for fr in group:
            if not G.has_node(fr):
                raise Exception('error: do not have ' + str(fr))
            for to in group:
                if not G.has_node(to):  # O(1)
                    raise Exception('error: do not have ' + str(to))
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
    if use_sort:
        for g in group:
            g.sort()
        group.sort()

    return group


main()