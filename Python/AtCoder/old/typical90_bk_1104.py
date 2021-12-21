# 縦の選び方=256通り
# それ毎にw*hのマスを捜査=4*10000通り
# -> 10**7くらい
# 縦に全部同じになっている数値があれば、その数値に対して答えを加算する
def main():
    r_end, c_end = map(int, input().split())
    P = [list(map(int, input().split())) for _ in range(r_end)]

    # bit全探索
    ALL = 1 << r_end
    ans = 0
    for bit in range(ALL):
        if bit == 0:
            continue
        row = []
        for r in range(r_end):
            if (bit >> r) & 1:
                row.append(r)

        # 各P[r][c]に対して、縦に全部同じ数字だった場合、マスの数を加算する
        cnt = {}
        for c in range(c_end):
            p = P[row[0]][c]
            is_same = True
            for r in row:
                if P[r][c] != p:
                    is_same = False
                    break
            if is_same:
                cnt[p] = cnt.get(p, 0) + len(row)

        # print(bin(bit), p, row, cnt)
        # 各cntのうち最大の者が答え
        for val in cnt.values():
            ans = max(ans, val)

    print(ans)


main()
