# DP[node][0] = nodeが0の時の最小値
# DP[node][1] = nodeが1の時の最小値
def main():
    node_end = int(input())
    node_end += 1
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    WH = 0
    BL = 1

    INF = float('inf')
    ans = INF
    for col_1 in range(2):
        DP = [[INF] * 2 for _ in range(node_end+1)]
        # node:0 の色は0で固定
        DP[0][WH] = 0
        DP[0][BL] = INF
        # node:1 の色はcol_1
        if col_1 == WH:
            # 0と同じ色なので、Aをカット
            DP[1][col_1] = A[0]
        else:
            # 違う色なので、手当不要
            DP[1][col_1] = 0
        for node in range(2, node_end):
            # nodeが白の時
            col = WH
            dp1 = DP[node - 1][WH] + B[node-2] + A[node-1]  # 同じ色なので、Bをカット、0と同じなのでAもカット
            dp2 = DP[node - 1][BL] + A[node-1]  # 違う色なので、手当不要
            DP[node][col] = min(dp1, dp2)
            # nodeが黒の時
            col = BL
            dp1 = DP[node - 1][WH]
            dp2 = DP[node - 1][BL] + B[node-2]
            DP[node][col] = min(dp1, dp2)

        node = node_end-1
        if col_1 == WH:
            # nodeがWHの時は、1とnodeをカット
            dp = DP[node][WH] + B[node-1]
            ans = min(ans, dp)
            # nodeがBLの時は、何もしない
            dp = DP[node][BL]
            ans = min(ans, dp)
        else:
            # 黒->白
            dp = DP[node][WH]
            ans = min(ans, dp)
            dp = DP[node][BL] + B[node-1]
            ans = min(ans, dp)

    print(ans)


main()
