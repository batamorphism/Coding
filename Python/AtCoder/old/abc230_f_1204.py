from collections import defaultdict
mod = 998244353


def main():
    n = int(input())
    A = [0] + list(map(int, input().split()))

    # DP[i]を、Aのi番目まで見たときの作れる数列の種類数
    # DP[i+1]は、新たにA[i+1]が使えるようになったことで
    # (1) iまで使って作った数列の末尾にA[i+1]を足さず、[A[i+1]]を生成する
    # (2) iまで使って作った数列の末尾にA[i+1]を足す
    # これは、DP[i+1] = DP[i]*2

    # A[i+1]を追加する前の数列が長さ0以上で、末尾の要素が0であったときに、
    # その分ダブルカウントとなる
    # DP[i]のうち長さ2以上で末尾の要素が0である数列の種類数を求めて、これを除く
    # A[k+1]+...+A[i]=0を満たすi未満の数kの最大値をf(i)とする
    # これは、A[1]+...+A[k]がsum(A[:i+1])と一致することを指す
    # これをもちいて、DP[f(i)]がダブルカウントされてる種類数

    # fの前計算
    f = [0]*(n+1)
    d = defaultdict(int)
    sum_a = 0
    for i, a in enumerate(A):
        sum_a += a
        f[i] = d[sum_a]  # A[i]までの合計と一致する、Aの部分和のindex
        d[sum_a] = i

    DP = [0]*(n+1)
    DP[1] = 1
    # 配るDP
    for i in range(1, n):
        DP[i+1] = (DP[i]*2 - DP[f[i]]) % mod

    print(DP[n])


main()
