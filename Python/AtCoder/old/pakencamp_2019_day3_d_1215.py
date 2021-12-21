# DP
# もらうDPは1-indexed
# DP[i][c] = i列目まで、色cで塗った時のコスト
# DP[0][*] = 0
# DP[i][c] = DP[i-1][c1] + cost[i][c1]

def main():
    INF = float('inf')
    n = int(input())
    S = [['*']*(n+1)]
    for r in range(1, 6):
        row = ['*'] + list(input())
        S.append(row)

    d = {'#': 0, 'R': 1, 'B': 2, 'W': 3}
    c_list = ['#', 'R', 'B', 'W']

    # calc_cost
    cost = [[INF]*4 for _ in range(n+1)]
    for i in range(1, n+1):
        column = []
        for r in range(1, 6):
            column.append(S[r][i])
        for c in range(1, 4):
            cost[i][c] = 5 - column.count(c_list[c])

    DP = [[0]*4 for _ in range(n+1)]

    for i in range(1, n+1):
        for c_i in c_list:
            dp = INF
            for c in c_list:
                if c == c_i:
                    continue
                dp = min(dp, DP[i-1][d[c]] + cost[i][d[c_i]])
            DP[i][d[c_i]] = dp
    ans = min(DP[n])
    print(ans)


main()
