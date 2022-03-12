import sys
import pypyjit
sys.setrecursionlimit(10**6)
pypyjit.set_param('max_unroll_recursion=-1')
# Sのサイズの平均から
# 黒く塗られた頂点数の平均を引けばよい
MOD = 10**9 + 7
rev_2 = (MOD+1) // 2


def rev(val):
    return pow(val, MOD-2, MOD)


def main():
    node_end = int(input())
    edge_end = node_end-1
    nei_of = [[] for _ in range(node_end)]
    for i in range(edge_end):
        fr, to = map(lambda x: int(x)-1, input().split())
        nei_of[fr].append((to, i))
        nei_of[to].append((fr, i))

    # 答えの貢献度
    # 木は辺で考える
    # cnt_of[edge_id] = edgeより葉側にいる頂点の数
    cnt_of = [0]*edge_end

    def dfs(cur, pre):
        ret = 1
        for nex, edge_id in nei_of[cur]:
            if nex == pre:
                continue
            cnt = dfs(nex, cur)
            ret += cnt
            cnt_of[edge_id] = cnt
        return ret

    dfs(0, -1)

    # Sのサイズの平均を求める
    # 頂点数が0の場合
    s_siz = 0
    # 頂点数が1の場合
    # s_siz += 1 - (1/2) ** node_end
    s_siz += 1 - pow(rev_2, node_end, MOD)
    for edge in range(edge_end):
        # edgeがSに含まれる確率は、
        # leaf側にもroot側にも、頂点が1つ以上ある確率
        cnt_leaf = cnt_of[edge]
        cnt_root = node_end - cnt_leaf
        # prob = (1 - (1/2)**cnt_leaf) * (1 - (1/2)**cnt_root)
        prob = (1 - pow(rev_2, cnt_leaf, MOD)) * (1 - pow(rev_2, cnt_root, MOD))
        s_siz += prob
        s_siz %= MOD
    # 答えは、黒の頂点数の平均を引いたもの
    # ans = s_siz - node_end*(1/2)
    ans = s_siz - node_end*rev_2
    ans %= MOD
    print(ans)


main()
