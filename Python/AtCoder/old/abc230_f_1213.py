mod = 998244353
from collections import defaultdict
# 数列Aに区切りを入れて、それらを足し合わせる操作を考える
# 合計して0になる区間が問題
# a_iまで見たときの組み合わせ数をDP[i]とする
# a_i-1とa_iに区切りを入れるとき
# dp = DP[i-1]
# 区切りを入れないとき、
# dp = DP[i-1]
# ただしこれだと重複が生じる
# a_iを追加する前の数列が長さ2以上で、末尾の要素が0であったときに限り
# b_1, .., b_k-1, 0 にa_iを足すと
# b_1, .., b_k-1, 0, a_i
# b_1, .., b_k-1, 0 + a_i
# b_1, .., b_k-1 + 0, a_i
# で重複が発生する
# f(i)を、a_f(i) + ... + a_i = 0となる添え字とすると
# DP[i+1] = 2*DP[i] - DP[f(i)]


def main():
    n = int(input())
    A = [0] + list(map(int, input().split()))

    DP = [0]*(n+1)
    DP[1] = 1

    # set f
    f = [0]*(n+1)
    d = defaultdict(int)
    sum_a = 0
    for i in range(n+1):
        sum_a += A[i]
        f[i] = d[sum_a]
        d[sum_a] = i

    for i in range(2, n+1):
        DP[i] = (2*DP[i-1]-DP[f[i-1]]) % mod

    ans = DP[n]
    print(ans)


main()
