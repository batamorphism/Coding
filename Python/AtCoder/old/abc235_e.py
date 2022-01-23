# クエリ先読み
# クラスカル法では、重みが小さい順に見ていくので
def main():
    node_end , edge_end , query_end = map(int, input().split())
    edge_query_list = []
    # [e_or_q, fr, to, we]からなるリスト
    for _ in range(edge_end):
        fr, to, we = map(int, input().split())
        fr -= 1
        to -= 1
        edge_query_list.append((-1, fr, to, we))

    for q in range(query_end):
        fr, to, we = map(int, input().split())
        fr -= 1
        to -= 1
        edge_query_list.append((q, fr, to, we))

    edge_query_list.sort(key = lambda x: x[3])

    # setup union find
    par = [i for i in range(node_end)]

    def find(x):
        if x == par[x]:
            return x
        par[x] = find(par[x])
        return par[x]

    def union(x, y):
        x = find(x)
        y = find(y)
        if x == y:
            return
        par[x] = y

    def same(x, y):
        return find(x) == find(y)

    ans_list = ['*']*query_end
    for e_or_q, fr, to, we in edge_query_list:
        if e_or_q == -1:
            # これはedge
            # クラスカル法を適用する
            if not same(fr, to):
                union(fr, to)
        else:
            # これはquery
            # クラスカル法を適用しつつ、unionはしない
            if same(fr, to):
                # こいつは最小全域木に含まれない
                ans_list[e_or_q] = 'No'
            else:
                # 含まれる、けどunionはしない
                ans_list[e_or_q] = 'Yes'

    print(*ans_list, sep='\n')


main()
