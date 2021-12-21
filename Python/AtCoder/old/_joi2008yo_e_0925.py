def main():
    # 行に対して全パターン試し
    # 列に対して1か0大きいほうを計算しmax(count(0), count(1))
    # その総和が最大になるものを計算する
    r_cnt, c_cnt = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(r_cnt)]
    # r_rev[r] : r行目を反転
    ans = 0
    for bit in range(1 << r_cnt):
        r_rev = [False]*r_cnt
        for r in range(r_cnt):
            if (bit >> r & 1):
                r_rev[r] = True
        cnt = 0
        for c in range(c_cnt):
            cnt_0 = 0
            cnt_1 = 0
            for r in range(r_cnt):
                if matrix[r][c] == 0:
                    if r_rev[r]:
                        cnt_1 += 1
                    else:
                        cnt_0 += 1
                else:
                    if r_rev[r]:
                        cnt_0 += 1
                    else:
                        cnt_1 += 1
            cnt += max(cnt_0, cnt_1)
        ans = max(cnt, ans)
    print(ans)



main()
