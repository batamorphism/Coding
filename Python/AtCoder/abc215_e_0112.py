from collections import defaultdict
MOD = 998244353


# 今まで出たコンテストの種類をSとする
# i番目のコンテストの種類をx_iとする
# x_i not in pre_Sならば、DP[i][S]に加算
# x_i in pre_Sならば、x_j != x_iとなる最大のjを探し、DP[j][pre_S / {x]]を加算
def main():
    n = int(input())
    tex = list(input())
    tex = [char2int(c) for c in tex]
    A = [-1] + tex

    c_end = 10
    ALL = 1 << c_end
    DP = [[[0]*c_end for _ in range(ALL)] for _ in range(n+2)]
    for i in range(1, n+1):
        a_i = A[i]
        for S in range(ALL):
            for pre in range(c_end):
                DP[i][S][pre] += DP[i-1][S][pre]
                if pre == a_i:
                    DP[i][S][pre] += DP[i-1][S][pre]
                if pre != a_i:
                    if not have(S, a_i):
                        nex_S = S ^ (1 << a_i)
                        DP[i][nex_S][a_i] += DP[i-1][S][pre]
                DP[i][S][pre] %= MOD
        DP[i][1 << a_i][a_i] += 1

    ans = 0
    for pre in range(c_end):
        for S in range(ALL):
            ans += DP[n][S][pre]
            ans %= MOD

    print(ans)


def have(S, x):
    return (S >> x) & 1


def remove(S, x):
    return S ^ (1 << x)


def char2int(c):
    return ord(c) - ord('A')


main()
