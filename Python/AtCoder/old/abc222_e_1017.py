import sys
sys.setrecursionlimit(10**9)

mod = 998244353


def main():
    n, m, k = map(int, input().split())
    A = list(map(int, input().split()))
    A = [a-1 for a in A]
    nei_of = [[] for _ in range(n)]
    edge_ind_of = {}
    for i in range(n-1):
        u, v = map(int, input().split())
        nei_of[u-1].append(v-1)
        nei_of[v-1].append(u-1)
        edge_ind_of[(min(u-1, v-1), max(u-1, v-1))] = i

    # Euler Tourで各辺を通る回数を記録
    edge_cnt = [0]*(n-1)
    color = ['w']*n

    def euler_tour(pre_node, to_node):
        ret = 0
        if pre_node == to_node:
            return 1
        for cur_node in nei_of[pre_node]:
            if color[cur_node] != 'w':
                continue
            color[cur_node] = 'g'
            tmp = euler_tour(cur_node, to_node)
            if tmp:
                # このノードは正解のルート
                edge_ind = edge_ind_of[(min(pre_node, cur_node), max(pre_node, cur_node))]
                edge_cnt[edge_ind] += 1
                # print(pre_node, cur_node)
            ret = tmp | ret
        return ret

    for i, fr in enumerate(A[:-1]):
        # print("-----")
        color = ['w']*n
        color[fr] = 'g'
        to = A[i+1]
        if fr == to:
            continue
        euler_tour(fr, to)

    ans = solve(edge_cnt, k)
    print(ans)


def solve(edge_cnt, k):
    # 各辺に+1, -1を付けたときの総和がkとなる組み合わせ
    # 各辺に+2, 0を付けたときの総和がk+nとなる組み合わせ(nは要素合計)
    # ナップザックDP
    # DP[i][s] edge_cntのi番目まで見たときの総和がsとなる組み合わせ数
    n = sum(edge_cnt)
    if n+k < 0:  # kは負値をとれるので注意
        return 0
    DP = [0]*(n+k+1)  # 添え字iを付けると遅くなるので注意。メモリ節約
    DP[0] = 1
    for val in edge_cnt:
        for s in range(n+k, -1, -1):
            if s-val*2 < 0:
                continue
            DP[s] += DP[s-val*2]
            DP[s] %= mod
    return DP[n+k]


main()
