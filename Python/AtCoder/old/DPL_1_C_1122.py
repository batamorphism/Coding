# DP[w] = 重さw以下で最も高い価値
# DP[w] = max(DP[w], DP[w-w_i] + v_i)
def main():
    n, W = map(int, input().split())
    item_list = [tuple(map(int, input().split())) for _ in range(n)]
    DP = [0]*(W+1)
    for w in range(W+1):
        dp = DP[w]
        for v_i, w_i in item_list:
            if w-w_i < 0:
                continue
            dp = max(dp, DP[w-w_i]+v_i)
        DP[w] = dp

    print(DP[W])


main()
