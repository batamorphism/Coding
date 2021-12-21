# 01knapsack
# DP[item][weight] = itemまで選んだ時の重さweight以下での価値の最大値

def main():
    n, W = map(int, input().split())
    item_list = [tuple(map(int, input().split())) for _ in range(n)]

    DP = [[0]*(W+1) for _ in range(n+1)]
    for item in range(1, n+1):
        v_i, w_i = item_list[item-1]
        for weight in range(W+1):
            dp = DP[item-1][weight]
            if weight-w_i >= 0:
                dp = max(dp, DP[item-1][weight-w_i]+v_i)
            DP[item][weight] = dp

    ans = DP[n][W]
    print(ans)


main()
