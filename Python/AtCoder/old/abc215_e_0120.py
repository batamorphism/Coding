# S:=今まで出たコンテスト
# x:=最後に出たコンテスト
def main():
    n = int(input())
    A = [0] + list(map(char2int, input()))
    a_end = 10
    ALL = 1 << a_end
    MOD = 998244353

    DP = [[[0] * a_end for _ in range(ALL)] for _ in range(n+2)]
    # DP[i][S][x]
    for i in range(1, n+1):
        a_i = A[i]
        DP[i][1 << a_i][a_i] += 1
        for cur_S in range(ALL):
            for lst in range(a_end):
                # i番目のコンテストに出場しない
                DP[i][cur_S][lst] += DP[i-1][cur_S][lst]
                # i番目のコンテストに出場するが、前回と同じ
                if a_i == lst:
                    DP[i][cur_S][lst] += DP[i-1][cur_S][lst]
                # i番目のコンテストに出場するが、前回と違う
                if a_i != lst:
                    if not cur_S >> a_i & 1:
                        nex_S = cur_S | 1 << a_i
                        DP[i][nex_S][a_i] += DP[i-1][cur_S][lst]
                DP[i][cur_S][a_i] %= MOD

    ans = 0
    for cur_S in range(ALL):
        for x in range(a_end):
            ans += DP[n][cur_S][x]
            ans %= MOD
    print(ans)


def char2int(c):
    return ord(c) - ord('A')


main()
