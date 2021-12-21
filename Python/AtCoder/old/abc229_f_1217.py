# DP
# 頂点iまで見た状態をDP[i]とする
# DP[i][0] = 頂点iを0で染める
# DP[i][1] = 頂点iを1で染める
# DP[i][0] = DP[i-1][0] + A[i] + B[i-1]
#          , DP[i-1][1] + A[i]
# DP[i][1] = DP[i-1][0]
#          , DP[i-1][1] + B[i-1]
# ここで、B[0] = 0とする
# ただし、頂点1を染めた色で場合分けする
# A[n+1] = 0だと思って、DP[n+1]を計算し、頂点1の色とn+1とで矛盾する場合を捨てる

def main():
    INF = float('inf')

    n = int(input())
    A = [0] + list(map(int, input().split())) + [0]
    B = [0] + list(map(int, input().split()))

    node_end = n + 2
    ans = INF
    for node1_col in range(2):
        DP = [[INF] * 2 for _ in range(node_end)]
        # node1の色はnode1_colと同じと仮定する
        if node1_col == 0:
            DP[1][0] = A[1]
        else:
            DP[1][1] = 0
        for node in range(2, node_end):
            dp1 = DP[node-1][0] + A[node] + B[node-1]
            dp2 = DP[node-1][1] + A[node]
            DP[node][0] = min(dp1, dp2)
            dp1 = DP[node-1][0]
            dp2 = DP[node-1][1] + B[node-1]
            DP[node][1] = min(dp1, dp2)
        # n+1は1と同じ色にする
        ans = min(ans, DP[n+1][node1_col])

    print(ans)


main()
