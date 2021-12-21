# 片方を止めて片方を高速に処理するのが定石
def main():
    S = input()
    n = len(S)
    S = S[::-1]
    S = [0] + [int(s) for s in S]
    # Tを、Sのi文字目まで見たときのmod2019上の値とする
    T = [0] * (n + 1)
    p = 1
    for i in range(1, n+1):
        T[i] = (T[i-1] + S[i]*p) % 2019
        p *= 10
        p %= 2019

    # T[hi] = T[lo]となる(hi, lo) ( 0 <= lo < hi <= n)の組み合わせ数が答え
    DP = [0]*2019
    ans = 0
    for i in range(n+1):
        t_i = T[i]
        ans += DP[t_i]
        DP[t_i] += 1

    print(ans)


main()
