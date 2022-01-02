def main():
    r_end, c_end, n = map(int, input().split())
    st_r, st_c = map(lambda x: int(x)-1, input().split())
    Taka = list(input())
    Aoki = list(input())

    # 逆から考える Aokiが勝つ領域を求める
    # 独立に考える
    # Takaは負ける領域を1マス縮められる
    # Aokiは勝てる領域を1マス拡大できる
    # 領域が尽きたらTakaの勝ち、初期値が領域を含んでいたらAokiの勝ち
    INF = float('inf')

    # 横向き
    def solve(c_end, L, R):
        aoki_win_min = 0
        aoki_win_max = c_end-1
        for i in range(n-1, -1, -1):
            if Aoki[i] == L:
                aoki_win_max += 1
                aoki_win_max = min(aoki_win_max, c_end-1)
            elif Aoki[i] == R:
                aoki_win_min -= 1
                aoki_win_min = max(aoki_win_min, 0)
            if aoki_win_max < aoki_win_min:
                return INF, -INF
            if Taka[i] == L:
                aoki_win_min += 1
            elif Taka[i] == R:
                aoki_win_max -= 1
            if aoki_win_max < aoki_win_min:
                return INF, -INF
        return aoki_win_min, aoki_win_max

    # 横向き
    aoki_win_min_c, aoki_win_max_c = solve(c_end, 'L', 'R')
    aoki_win_min_r, aoki_win_max_r = solve(r_end, 'U', 'D')
    if aoki_win_min_r <= st_r <= aoki_win_max_r:
        if aoki_win_min_c <= st_c <= aoki_win_max_c:
            print('YES')
            return
    print('NO')


main()
