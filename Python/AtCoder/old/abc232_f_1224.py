def main():
    n, x, y = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    # Aを置換σした後のコストを求めるのは容易
    # σを全探索する
    # Sを0,...,n-1の部分集合として
    # DP[i][S] := σ(S) = {0,...,i-1}となるすべてのσについての
    # B[:i]と一致するのに必要なコストの最小値とする
    # Sに含まれない各kについて、DP[i+1][S or k]に遷移する
    def popcount(n):
        return bin(n).count('1')

    INF = float('inf')
    ALL = 1 << n
    DP = [INF]*ALL
    DP[0] = 0

    for bit in range(ALL):
        i = popcount(bit)
        if i == n:
            continue
        b_i = B[i]
        for k, a_k in enumerate(A):
            if (bit >> k) & 1:
                continue
            # a_kをiの位置に持っていくように置換する
            # 0～n-1のうち、bitに入っておらず、kより小さいものの個数
            # これが置換に必要な回数
            cnt = popcount((~bit) & ((1 << k) - 1))
            bit_nex = bit ^ (1 << k)
            dp = DP[bit] + abs(a_k - b_i)*x + cnt*y
            DP[bit_nex] = min(DP[bit_nex], dp)

    print(DP[ALL-1])


main()
