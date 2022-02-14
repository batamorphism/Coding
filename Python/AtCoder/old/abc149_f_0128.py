import sys
sys.setrecursionlimit(10**6)


# 木は辺で考える
# edgeがSに含まれる<->edgeの両端より先に含まれる点に黒が含まれる
# Sの内側（境界除く)に含まれるnodeの数の期待値を求め、その半分が答え
# w w w 0, 0
# w w b 1, 0
# w b w 1, 0
# w b b 2, 0
# b w w 1, 0
# b w b 3, 1
# b b w 2, 0
# b b b 3, 0
# Sの期待値は、13/8
# 穴あき度の期待値は、1/8
# 穴あき度は、黒く塗られた頂点の個数を引けばよい
# 12/8 - 3/2 = 0
def main():
    MOD = 10**9 + 7
    rev_2 = (MOD+1)//2
    node_end = int(input())
    edge_end = node_end - 1
    nbh_of = [[] for _ in range(node_end)]
    for i in range(edge_end):
        a, b = map(lambda x: int(x)-1, input().split())
        nbh_of[a].append((b, i))
        nbh_of[b].append((a, i))

    # 各edgeについて、
    # そのedgeよりleaf側にあるnodeの数を数える
    cnt_of = [0]*edge_end

    def dfs(cur, pre):
        ret = 1
        for nex, ind in nbh_of[cur]:
            if nex == pre:
                continue
            cnt = dfs(nex, cur)
            # 戻り掛けに数える
            cnt_of[ind] += cnt
            ret += cnt
        return ret

    dfs(0, -1)

    s_node_cnt = 0
    # edge毎に、Sのnode数への貢献度を数える
    # edgeがない場合、nodeは全てがw出ない限り+1
    s_node_cnt += 1 - pow(rev_2, node_end, MOD)
    for edge_ind, cnt_child_node in enumerate(cnt_of):
        cnt_parent_node = node_end - cnt_child_node
        # childに黒が一つ以上ある、かつ、parentに黒が一つ以上ある場合
        # +1
        prob = (1-pow(rev_2, cnt_child_node, MOD)) * (1-pow(rev_2, cnt_parent_node, MOD))
        s_node_cnt += prob
        s_node_cnt %= MOD

    # Sの要素数から、黒の平均値を引けば答え
    ans = s_node_cnt - node_end*rev_2
    ans %= MOD
    print(ans)


main()
