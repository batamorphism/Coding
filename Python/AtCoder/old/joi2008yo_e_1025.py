def main():
    r_end, c_end = map(int, input().split())
    table = [list(map(int, input().split())) for _ in range(r_end)]
    # 各行のひっくり返し方を1つ決めれば
    # 各列のひっくり返し方は貪欲に決まる
    # -> 0と1とで多いほうを選べばよい
    ALL = 1 << r_end
    ans = 0
    for bit in range(ALL):
        r_turned = [0]*r_end
        for r in range(r_end):
            if bit >> r & 1:
                r_turned[r] = 1
        cnt = 0
        for c in range(c_end):
            cnt_0 = 0
            cnt_1 = 0
            for r in range(r_end):
                if table[r][c] ^ r_turned[r]:
                    cnt_1 += 1
                else:
                    cnt_0 += 1
            cnt += max(cnt_0, cnt_1)
        ans = max(cnt, ans)
    print(ans)


main()
