def main():
    n, W = map(int, map(int, input().split()))
    stuff_list = []
    for _ in range(n):
        v, w = map(int, map(int, input().split()))
        stuff_list.append((v, w))

    # 重複の許されたナップザック
    # DP[w]: 重さw以下の価値の最大値
    # DP[w] = max(DP[w-ww]+v)
    DP = [0]*(W+1)
    for w in range(W+1):
        dp = 0
        for stuff in stuff_list:
            vv, ww = stuff
            if w-ww >= 0:
                dp = max(DP[w-ww]+vv, dp)
        DP[w] = dp

    print(DP[W])


main()
