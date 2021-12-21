# DP[val] val円払うときの、コインの最小の枚数
# DP[val] = min(DP[val-coin]+1)

def main():
    n, m = map(int, input().split())
    val_max = n
    coin_list = list(map(int, input().split()))
    DP = [0] * (val_max+1)

    for val in range(val_max+1):
        if val == 0:
            DP[val] = 0
        else:
            DP[val] = float('inf')
            for coin in coin_list:
                if val-coin >= 0:
                    DP[val] = min(DP[val], DP[val-coin]+1)

    print(DP[val_max])


main()
