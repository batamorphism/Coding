# 貢献度を考える
# 木は枝の数+1
import sys
from functools import lru_cache
sys.setrecursionlimit(10**6)
mod = 10**9 + 7
rev2 = (mod+1)//2  # mod*rev2 = 1となる数


def main():
    # input
    input = sys.stdin.readline
    n = int(input())
    nei_of = [[] for _ in range(n)]

    # set variables
    node_end = n
    edge_end = n-1
    for edge_ind in range(edge_end):
        a, b = map(int, input().split())
        a -= 1
        b -= 1
        nei_of[a].append((b, edge_ind))
        nei_of[b].append((a, edge_ind))

    # calc
    # cnt_of[edge_ind] = 各edge_indに対し、そのedge_indより深いnodeの数
    # dfs
    cnt_of = [0] * edge_end

    def dfs(cur, pre):
        ret = 1
        for nex, edge_ind in nei_of[cur]:
            if nex == pre:
                continue
            cnt_of[edge_ind] = dfs(nex, cur)  # 戻りがけにカウント
            ret += cnt_of[edge_ind]
        return ret

    dfs(0, -1)

    # 部分木Sが、edge_indを持つ確率は、
    # 黒く塗られた頂点がedge_indの両方にあるときなので
    # 1 - rev2**(cnt_of[edge_ind]) - (rev2**(node_end-cnt_of[edge_ind]))
    # 部分木Sが、edge_indを持つ場合の貢献度は、1
    # ただし、貢献度の初期値は、黒く塗られた頂点が1つの時は1、0の時は0であるので、
    # 1-rev2**(node_end)
    # これで、部分木Sの持っているnodeの数の期待値s_cntが求められた

    # 2**node_end通りの塗り方それぞれについて、
    # 部分木Sが一意に定まり
    # 部分木Sに含まれないnodeの個数の期待値は、not_s_cnt = node_end - s_cntで、これは常に白
    # 全体の白いnodeの期待値は、node_end*rev2なので、
    # 部分木Sに含まれる白いnodeの期待値は、node_end*rev2 - not_s_cnt
    s_cnt = 1-modpow(rev2, node_end, mod)
    for edge_ind in range(edge_end):
        ans_of_edge_ind = 1
        ans_of_edge_ind += - modpow(rev2, (cnt_of[edge_ind]), mod)
        ans_of_edge_ind += - modpow(rev2, (node_end-cnt_of[edge_ind]), mod)
        ans_of_edge_ind += + modpow(rev2, node_end, mod)
        s_cnt += ans_of_edge_ind
        s_cnt %= mod

    not_s_cnt = node_end - s_cnt
    ans = node_end*rev2 - not_s_cnt
    ans %= mod
    print(ans)


@lru_cache(maxsize=None)
def modpow(a, b, mod):
    return pow(a, b, mod)


main()
