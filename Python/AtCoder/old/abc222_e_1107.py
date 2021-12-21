import sys
sys.setrecursionlimit(10**6)

mod = 998244353


def main():
    node_end, m, k = map(int, input().split())
    edge_end = node_end-1
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    tour = []
    for aft in range(1, m):
        bef = aft-1
        tour.append((A[bef], A[aft]))

    nei_of = [[] for _ in range(node_end)]
    for edge_id in range(edge_end):
        u, v = map(int, input().split())
        u -= 1
        v -= 1
        nei_of[u].append((v, edge_id))
        nei_of[v].append((u, edge_id))

    edge_cnt = [0]*(edge_end)
    # fr->toで通った辺の数をカウント

    def dfs(cur, pre, fr, to):
        ret = 0
        if cur == to:
            return 1
        for nex, edge_id in nei_of[cur]:
            if nex == pre:
                continue
            cnt = dfs(nex, cur, fr, to)
            edge_cnt[edge_id] += cnt
            ret += cnt
        return ret

    for fr, to in tour:
        st = fr
        dfs(st, -1, fr, to)

    # print(edge_cnt)
    # print(tour)

    # 各edgeにそれぞれ+1, -1を割り振って合計をkにする
    # 各edgeにそれぞれ+2, 0を割り振って合計をk+sum(edge_cnt)にする
    # ナップザックDP
    # DP[i][k] = i番目まで見て、合計がkちょうどになる組み合わせ数
    # DP[0][0] = 1
    k += sum(edge_cnt)
    if k % 2 != 0:
        print(0)
        return
    if k < 0:
        print(0)
        return

    #DP = [[0]*(edge_end+1) for _ in range(k+1)]
    #DP[0][0] = 1
    DP = [0]*(k+1)
    DP[0] = 1
    for i in range(1, edge_end+1):
        for val in range(k, -1, -2):
            dp1 = DP[val]  # 追加なし
            dp2 = 0
            if (val-edge_cnt[i-1]*2) >= 0:
                dp2 = DP[val-edge_cnt[i-1]*2]  # 追加あり
            dp = dp1+dp2
            dp %= mod
            # print(dp, val, i, val-edge_cnt[i-1]*2, dp1, dp2)
            DP[val] = dp

    print(DP[k])
    # print(DP)
    # print(k)
    # for dp in DP[edge_end]:
        # print(dp)


main()
