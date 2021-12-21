def main():
    # DP[num][wei] 荷物をnum個まで見たときの、重さwei以下での価値の最大値
    n, w = map(int, input().split())
    stuff_list = [list(map(int, input().split())) for _ in range(n)]
    num_end = n
    wei_max = w
    DP = [[0]*(wei_max+1) for _ in range(num_end)]
    for num, stuff in enumerate(stuff_list):
        v, w = stuff
        for wei in range(wei_max+1):
            if wei-w < 0:
                DP[num][wei] = DP[num-1][wei]
                continue
            DP[num][wei] = max(DP[num-1][wei-w]+v, DP[num-1][wei])

    print(DP[-1][-1])


main()
