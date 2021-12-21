def main():
    n = int(input())
    item_list = [(-1, -1, -1)]
    for _ in range(n):
        day, cost, val = map(int, input().split())
        item_list.append((day, cost, val))

    item_list.sort()

    end = 5001
    # 仕事iまで見た状態で、今までx日しか仕事していない
    DP = [[0]*(end) for _ in range(n+1)]

    for i in range(1, n+1):
        day_i, cost_i, val_i = item_list[i]
        for x in range(end):
            # i番目の仕事をしない場合
            dp1 = DP[i-1][x]
            # i番目の仕事をする場合
            # i-1番目の仕事が終わった時点で、まだx-cost_i日しか仕事をしていない
            # かつ、xがday_i以下
            dp2 = 0
            if x-cost_i >= 0 and x <= day_i:
                dp2 = DP[i-1][x-cost_i] + val_i
            dp = max(dp1, dp2)
            DP[i][x] = dp

    ans = max(DP[n])
    print(ans)


main()
