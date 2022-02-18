import copy
from itertools import product


def main():
    node_end, price_max, cnt_eq = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(node_end)]
    change_edge = []
    for fr in range(node_end):
        for to in range(node_end):
            if grid[fr][to] == -1:
                change_edge.append((fr, to))

    def change_cost(grid, change_edge, cost):
        for fr, to in change_edge:
            grid[fr][to] = cost

    def wf(grid):
        # gridについて、price_max以下で移動できる辺のペアを求める
        dist = copy.deepcopy(grid)
        for k, fr, to in product(range(node_end), repeat=3):
            d1 = dist[fr][to]
            d2 = dist[fr][k] + dist[k][to]
            dist[fr][to] = min(d1, d2)
        cnt = 0
        for fr in range(node_end):
            for to in range(fr+1, node_end):
                if dist[fr][to] <= price_max:
                    cnt += 1
        return cnt

    # 答えで2分探索
    # ただし、 1 <= x
    INF = 10**16
    ok = 0
    ng = INF
    while ng - ok > 1:
        mid = (ok + ng)//2
        change_cost(grid, change_edge, mid)
        cnt = wf(grid)
        if cnt >= cnt_eq:
            ok = mid
        else:
            ng = mid
    geq = ok

    ok = 0
    ng = INF
    while ng - ok > 1:
        mid = (ok + ng)//2
        change_cost(grid, change_edge, mid)
        cnt = wf(grid)
        if cnt > cnt_eq:
            ok = mid
        else:
            ng = mid
    gt = ok

    # (gt, geq] と、 [1, inf)の共通部分の個数を考えればよい
    # (gt, geq] と、 (0, inf)の共通部分の個数を考えればよい
    if geq < 1:  # 共通部分を持たない
        ans = 0
    elif gt >= INF - 1:  # 共通部分を持たない
        ans = 0
    elif geq == INF - 1:
        ans = 'Infinity'
    else:  # 共通部分を持つ
        hi = geq
        lo = gt
        ans = hi-lo

    print(ans)


main()
