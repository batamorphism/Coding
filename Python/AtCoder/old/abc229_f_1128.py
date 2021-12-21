INF = float('inf')


def main():
    n = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))

    ans = INF
    for node1_col in range(2):
        # DP[node][col] = nodeをcolで塗った時のコスト、ただしcol = 0, 1
        DP = [[0] * 2 for _ in range(n + 1)]
        # node = 0は0で塗る
        DP[0][0] = 0
        DP[0][1] = INF
        # node =1 の色は最初に指定する
        DP[1][0] = DP[1][1] = INF
        if node1_col == 0:
            DP[1][0] = A[1]
        else:
            DP[1][1] = 0

        for node in range(2, n + 1):
            # nodeを0で塗る場合
            # node == 1の場合、B[node-1]を考慮する必要はない。0を入れているので問題ない
            dp1 = A[node] + DP[node - 1][0] + B[node-1]
            dp2 = A[node] + DP[node - 1][1]
            DP[node][0] = min(dp1, dp2)
            # nodeを1で塗る場合
            dp1 = DP[node-1][0]
            dp2 = DP[node-1][1] + B[node-1]
            DP[node][1] = min(dp1, dp2)
            # print(node, DP[node][0], DP[node][1])
        # 最後に、DP[n][col]について、col == node1_colならn->1の辺を切る
        DP[n][node1_col] += B[n]
        ans = min(ans, *DP[n])

    print(ans)


main()
