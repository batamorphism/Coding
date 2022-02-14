import pypyjit
import sys
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')


def main():
    node_end = int(input())
    edge_end = node_end - 1
    nei_of = [[] for _ in range(node_end)]
    for i in range(node_end-1):
        a, b = map(lambda x: int(x)-1, input().split())
        nei_of[a].append((b, i))
        nei_of[b].append((a, i))
    MOD = 10**9 + 7
    REV_2 = (MOD+1)//2

    # 各辺に対し、その辺よりleaf側にある頂点の数を数える
    cnt_of = [0]*edge_end

    def dfs(cur, pre):
        ret = 1
        for nex, edge_i in nei_of[cur]:
            if nex == pre:
                continue
            cnt = dfs(nex, cur)
            cnt_of[edge_i] = cnt
            ret += cnt
        return ret

    dfs(0, -1)

    # Sの頂点数の期待値を求める
    # 頂点数が0又は1の時
    ans = 1 - pow(REV_2, node_end, MOD)
    for edge_ind in range(edge_end):
        leaf_side = cnt_of[edge_ind]
        root_side = node_end - leaf_side
        # leaf側も、root側も、それぞれ1つずつ持てばよい
        ans += (1-pow(REV_2, leaf_side, MOD))*(1-pow(REV_2, root_side, MOD))
        ans %= MOD
    # 最後に、黒の頂点数の期待値を引く
    ans -= node_end * REV_2
    ans %= MOD
    print(ans)


main()
