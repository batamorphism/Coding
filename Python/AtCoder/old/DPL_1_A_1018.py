def main():
    n, m = map(int, input().split())
    coin_list = list(map(int, input().split()))
    coin_list = [0] + coin_list
    # DP[num][val] num枚使って、val円となる最小の枚数
    # numは潰す
    # DP[val] = val円となる最小の枚数
    MAX_VAL = n
    # MAX_NUM = m
    INF = 10**9
    DP = [0]*(MAX_VAL+1)
    for val in range(0, MAX_VAL+1):
        for num, coin in enumerate(coin_list):
            if val == 0:
                DP[val] = 0
                continue
            if num == 0:
                DP[val] = INF
                continue

            cnt = INF
            if val-coin >= 0:
                cnt = DP[val-coin]+1
            DP[val] = min(cnt, DP[val])

    print(DP[-1])


main()
