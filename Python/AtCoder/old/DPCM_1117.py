# y: 複合化後の音声信号
# C: コードブック
# k:出力系列 今回選ぶもの
# y[n] = y[n-1]+C[k[n]]
# y[0] = 128
y_max = 255
y_min = 0
INF = 10**9


def main():
    ans_list = []
    while True:
        n, m = map(int, input().split())
        if (n, m) == (0, 0):
            break
        C = [int(input()) for _ in range(m)]
        X = [int(input()) for _ in range(n)]

        # DP[ind][y] = X[ind]まで見たときで、末尾がyとなるときの二乗和の最小値
        # DP[ind][y] = DP[ind-1][y-C[x]] + (X[ind] - y)**2
        DP = [[INF]*(y_max+1) for _ in range(n+1)]

        # 初期化
        DP[0][128] = 0

        for pre_ind in range(n):
            for pre_y in range(y_max+1):
                nex_ind = pre_ind + 1
                for c in C:
                    nex_y = pre_y + c
                    nex_y = max(y_min, min(y_max, nex_y))
                    DP[nex_ind][nex_y] = min(DP[nex_ind][nex_y], DP[pre_ind][pre_y] + (X[nex_ind-1] - nex_y)**2)

        ans = min(DP[n])
        ans_list.append(ans)
        # print(ans)

    print(*ans_list, sep='\n')


main()
