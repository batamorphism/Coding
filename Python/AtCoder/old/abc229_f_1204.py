# node0を0で着色
# node1を0または1で着色し、DP
INF = float('inf')


def main():
    n = int(input())
    A = [0] + list(map(int, input().split()))
    B = [0] + list(map(int, input().split()))
    # A[i] = 0 -> iを結ぶ辺の重み
    # B[i] = i -> iを結ぶ辺の重み
    # DP[i][col] = iまで見たときの、iの色がcolであるときの最小重み
    # ただし、i = n+1は、ぐるっと回って戻ってきたnode1とする
    A += [A[1]]

    # node1を0で着色する
    ans = INF
    node1_col = 0
    for node1_col in range(2):
        DP = [[INF]*2 for _ in range(n + 2)]
        DP[0][0] = 0
        DP[1][node1_col] = 0
        for node in range(2, n + 2):
            # node2を0で着色するときは
            # 0 -> iは必ず切断し
            # i-1 -> iは、同じ色なら切断する
            for col in range(2):
                if col == 0:
                    dp1 = DP[node-1][1]+A[node]
                    dp2 = DP[node-1][0]+B[node-1]+A[node]
                else:
                    dp1 = DP[node-1][1]+B[node-1]
                    dp2 = DP[node-1][0]
                DP[node][col] = min(dp1, dp2)
        # DP[n+1][node1_col]が答え
        ans = min(DP[n+1][node1_col], ans)

    print(ans)


main()
