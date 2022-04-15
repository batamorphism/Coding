def main():
    node_end = int(input())
    node_end += 1
    A = [0] + list(map(int, input().split())) + [0]
    B = [0] + list(map(int, input().split()))

    # DP
    # DP[node][col] := 頂点nodeを見た状態で、
    # 頂点nodeをcolに染めた場合の、コストの最小値
    # node=0のcolは0として一般性を失わない
    # node=1が0の場合と、1の場合で分けて考える
    INF = float('inf')
    ans = INF

    for node1_col in range(2):
        col_of = [-1]*node_end
        col_of[0] = 0
        col_of[1] = node1_col
        dp = [INF]*2
        if node1_col == 0:
            dp[node1_col] = A[1]
        else:
            dp[node1_col] = 0

        # 配るDP
        for cur_node in range(1, node_end):
            new_dp = [INF]*2
            nex_node = cur_node+1
            for cur_col in range(2):
                # cur_colと同じ色に染めるためには、
                # cur_col == 0の場合は、A[nex_node]を切断し、B[cur_node]を切断する
                # cur_col == 1の場合は、B[cur_node]を切断する
                nex_col = cur_col
                if cur_col == 0:
                    new_dp[nex_col] = min(new_dp[nex_col], dp[cur_col] + A[nex_node] + B[cur_node])
                else:
                    new_dp[nex_col] = min(new_dp[nex_col], dp[cur_col] + B[cur_node])
                # cur_colと違う色に染めるためには
                # cur_col == 1の場合は、A[nex_node]を切断し
                # cur_col == 0の場合は、何もしない
                nex_col = cur_col ^ 1
                if cur_col == 0:
                    new_dp[nex_col] = min(new_dp[nex_col], dp[cur_col])
                else:
                    new_dp[nex_col] = min(new_dp[nex_col], dp[cur_col]+A[nex_node])
            dp = new_dp[:]

        # A[nex_node]は最終的に0としているので、A[0]のダブルカウントは発生しない
        # node1_colと矛盾するものは破棄する
        ans = min(ans, dp[node1_col])
    print(ans)


main()
