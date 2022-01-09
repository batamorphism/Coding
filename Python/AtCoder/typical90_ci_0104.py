from itertools import product
import copy
INF = 10**18


# 答えで二分探索
# ワーシャルフロイド
def main():
    node_end, price_max, k = map(int, input().split())
    adj = [list(map(int, input().split())) for _ in range(node_end)]
    change_list = []
    for r, c in product(range(node_end), repeat=2):
        if adj[r][c] == -1:
            change_list.append((r, c))

    # k+1個以上となる最小の1 <= x_loと
    # k個以上となる最小の1 <= x_hiを求める
    ok = 0
    ng = INF
    while ng - ok > 1:
        mid = (ok+ng)//2
        cnt = count_pair(adj, mid, price_max, k, node_end, change_list)
        if cnt >= k+1:
            ok = mid
        else:
            ng = mid
    x_lo = ok

    ok = 0
    ng = INF
    while ng - ok > 1:
        mid = (ok+ng)//2
        cnt = count_pair(adj, mid, price_max, k, node_end, change_list)
        if cnt >= k:
            ok = mid
        else:
            ng = mid
    x_hi = ok

    # print(x_hi, x_lo)
    if x_hi == 0:
        ans = 0
    elif x_lo == 0:
        # 1, ...,x_hiが答え
        ans = x_hi
    else:
        ans = x_hi - x_lo
    if ans > INF//10:
        ans = 'Infinity'
    print(ans)


def change_adj(adj, val, change_list):
    # adj内の変更可能なedgeのコストをvalに変更する
    for r, c in change_list:
        adj[r][c] = val


def wf(adj, node_end):
    dist = copy.deepcopy(adj)
    for k, fr, to in product(range(node_end), repeat=3):
        d1 = dist[fr][to]
        d2 = dist[fr][k] + dist[k][to]
        dist[fr][to] = min(d1, d2)
    return dist


def _count_pair(dist, price_max, node_end):
    # price_max以下で移動可能なペア(fr, to)の個数を数える
    # fr < to
    ret = 0
    for fr in range(node_end):
        for to in range(fr+1, node_end):
            if dist[fr][to] <= price_max:
                ret += 1
    return ret


def count_pair(adj, x, price_max, k, node_end, change_list):
    # xを指定した時に、price_max以下で移動できる都市の数がk以下であることの判定
    change_adj(adj, x, change_list)
    dist = wf(adj, node_end)
    cnt = _count_pair(dist, price_max, node_end)
    return cnt


main()
