def main():
    n = int(input())
    A = [1] + list(map(lambda x: int(x)+1, input().split()))
    B = [1] + list(map(lambda x: int(x)+1, input().split()))
    n += 1

    MOD = 998244353
    b_end = 3010
    DP = [0]*b_end
    DP[1] = 1
    for b in range(1, b_end):
        DP[b] += DP[b-1]
        DP[b] %= MOD

    # 貰うDP
    for nex_i in range(1, n):
        new_DP = [0]*b_end
        pre_i = nex_i - 1
        a_pre_i = A[pre_i]
        b_pre_i = B[pre_i]
        a_nex_i = A[nex_i]
        b_nex_i = B[nex_i]

        for nex_c in range(a_nex_i, b_nex_i+1):
            pre_c_begin = a_pre_i
            pre_c_max = min(b_pre_i, nex_c)
            new_DP[nex_c] = (DP[pre_c_max] - DP[pre_c_begin-1])
            # 区間和を高速化する
            # 累積和
            """
            for nex_c in range(nex_c_begin, nex_c_end):
                new_DP[nex_c] += DP[pre_c]
            """
        for b in range(b_end):
            DP[b] = new_DP[b] % MOD
        for b in range(1, b_end):
            DP[b] += DP[b-1]
            DP[b] %= MOD

    ans = DP[-1]
    print(ans)


main()
