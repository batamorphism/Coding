from collections import Counter


# a-zの順に、それぞれの文字が何個あるか見る
# DP[c][n] := 長さnの文字列で、アルファベットのcまで使った物が何個あるか
def main():
    S = [-1] + list(map(c2i, input()))
    cnt_of = Counter(S)
    MOD = 998244353

    comb = [[0] * 5100 for _ in range(5100)]
    # combを前計算
    for n in range(1, 5100):
        comb[n][0] = comb[n][n] = 1
        for r in range(1, n):
            comb[n][r] = (comb[n - 1][r - 1] + comb[n - 1][r]) % MOD

    reorder_comb = [[0] * 5100 for _ in range(5100)]
    for n in range(5100):
        for r in range(n+1):
            reorder_comb[n-r][r] = comb[n][r]

    def comb_(n, r):
        # r = n - const
        # const = n - r
        # となるようにn, rがとられていることを鑑みて、キャッシュが効くようにする
        return reorder_comb[n-r][r]

    # 配るDP
    DP = [[0] * (len(S)+1) for _ in range(27)]
    for c in range(27):
        DP[c][0] = 1
    for nex_c in range(1, 27):
        for cur_n in range(len(S)):
            nex_n_begin = cur_n  # nex_cを0文字追加
            nex_n_end = cur_n + cnt_of[nex_c] + 1  # nex_cをcnt_of[c]個追加する
            nex_n_end = min(nex_n_end, len(S)+1)
            for nex_n in range(nex_n_begin, nex_n_end):
                cnt_of_nex_c = nex_n-cur_n
                # combにメモリキャッシュがうまく効かない
                # dp = DP[nex_c-1][cur_n] * comb[nex_n][cnt_of_nex_c] % MOD
                dp = DP[nex_c-1][cur_n] * reorder_comb[nex_n-cnt_of_nex_c][cnt_of_nex_c] % MOD
                DP[nex_c][nex_n] += dp
                DP[nex_c][nex_n] %= MOD

    ans = (sum(DP[26])-1) % MOD
    print(ans)


def c2i(c):
    return ord(c) - ord('a') + 1


main()
