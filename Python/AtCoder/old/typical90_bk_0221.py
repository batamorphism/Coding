from collections import Counter


# 行の選び方を全探索
def main():
    r_end, c_end = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(r_end)]

    ALL = 1 << r_end
    ans = -1
    for r_S in range(ALL):
        cnt_of = Counter()
        # 全ての列が同じ値となっている場合、その値:列数*r_Sのサイズを足す
        for c in range(c_end):
            cur_cnt_of = Counter()
            key = -1
            for r in range(r_end):
                if r_S >> r & 1 == 0:
                    continue
                cur_cnt_of[grid[r][c]] += 1
                key = grid[r][c]
            # 全ての行の値が同じであれば、cnt_ofに加算
            if len(cur_cnt_of) == 1:
                cnt_of[key] += cur_cnt_of[key]
        cur_ans = -1
        for key, val in cnt_of.items():
            cur_ans = max(cur_ans, val)
        ans = max(ans, cur_ans)
    print(ans)


def popcount(S):
    return bin(S).count('1')


main()
