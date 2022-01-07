from collections import defaultdict
mod = 10**9 + 7


# 部分列DP
# f = 直近にその文字が出てきた場所
# DP[i] = i番目の文字を使う場合の、部分列の種類数
def main():
    S = '*' + input()
    n = len(S)
    f = defaultdict(lambda: -1)

    DP = [0] * n
    SUM = [0] * n
    DP[0] = 1
    SUM[0] = 1

    # 部分列の種類数は、その文字が初めて出てきた場合
    # 今までの部分列の組み合わせ数の総和

    # その文字が前に出てきたことがある場合
    # それをf[i]として、DP[f[i]]以降の和
    for i, s in enumerate(S[1:], 1):
        fs = f[s]
        if fs == -1:
            # 初めて出てきた
            dp = SUM[i-1]
        else:
            # 前に出てきた
            dp = SUM[i-1] - SUM[fs-1]
        DP[i] = dp
        SUM[i] = SUM[i-1] + dp
        DP[i] %= mod
        SUM[i] %= mod
        f[s] = i

    ans = sum(DP) % mod

    print(ans)


main()
