from collections import defaultdict
mod = 10**9+7


# 選択を入れるDP
def main():
    n = int(input())
    C = [0] + [int(input()) for _ in range(n)]
    n += 1

    # DP[i] = i番目まで見たときの組み合わせの数
    # j = c_iが前回出てきた場所(c_j == c_i)
    # DP[i] = DP[i-1] <- i番目は何もしない
    #       + DP[j] <- iとjでひっくり返す ただしj == i-1の時はなにもしない
    DP = [0] * n
    DP[0] = 1
    d = defaultdict(int)

    for i, c_i in enumerate(C[1:], 1):
        j = d[c_i]
        dp = 0
        dp += DP[i-1]
        if j != 0 and j != i-1:
            dp += DP[j]
        dp %= mod
        DP[i] = dp
        d[c_i] = i

    ans = DP[n-1]
    print(ans)


main()
