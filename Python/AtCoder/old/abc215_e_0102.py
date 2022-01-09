MOD = 998244353


# S := 既に一塊になっていないコンテストの種類
# DP[コンテストi回目まで][既に出場したコンテストの種類の集合][最後に出場したコンテストの種類] の場合の数
# i番目のコンテストに出場しない場合の数
# DP[i][S][pre] += DP[i-1][S][pre]
# i番目のコンテストに出場するが、前回と同じコンテストの場合の数
# DP[i][S][pre] += DP[i-1][S][pre]  (A[i] == pre)
# i番目のコンテストに出場するが、前回と違うコンテストの場合の数
# DP[i][S U {a_i}][a_i] += DP[i-1][S][pre]  (A[i] != pre)
# i番目のコンテストが初めてのコンテストの場合
# DP[i][{a_i}][a_i] += 1
def main():
    n = int(input())
    text = input()

    def char_to_int(c):
        return ord(c) - ord('A')

    A = [0] + [char_to_int(c) for c in text]

    ALL = 1 << 10
    DP = [[[0]*(10) for _ in range(ALL)] for _ in range(n+2)]

    for i in range(1, n+1):
        a_i = A[i]
        for S in range(ALL):
            for pre in range(10):
                # i番目のコンテストに出場しない場合の数
                DP[i][S][pre] += DP[i-1][S][pre]
                # i番目のコンテストに出場するが、前回と同じコンテスト
                if pre == a_i:
                    DP[i][S][pre] += DP[i-1][S][pre]
                # i番目のコンテストに出場するが、前回と違うコンテスト
                if pre != a_i:
                    if not (S >> a_i) & 1:
                        DP[i][S | (1 << a_i)][a_i] += DP[i-1][S][pre]
                DP[i][S][a_i] %= MOD
        # i番目のコンテストが初のコンテスト
        DP[i][1 << a_i][a_i] += 1

    ans = 0
    for pre in range(10):
        for S in range(ALL):
            ans += DP[n][S][pre]
            ans %= MOD

    print(ans % MOD)


main()
